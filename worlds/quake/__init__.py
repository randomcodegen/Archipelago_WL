import io
import json
import math
from pathlib import Path
from .levels import E1
from typing import Any, Dict, List, Optional, Set, Tuple

# Compatibility across Python versions
try:
    from importlib.resources import files
except ImportError:
    from importlib_resources import files  # noqa

from BaseClasses import ItemClassification, MultiWorld, Region
from worlds.AutoWorld import World

from . import resources
from .base_classes import Q1Item, Q1Level, LocationDef
from .id import GAME_ID, local_id, net_id
from .items import all_items, item_groups
from .levels import all_episodes, all_levels
from .options import Difficulty, Q1Options
from .rules import Rules

with files(resources).joinpath("id_map.json").open() as id_file:
    game_ids = json.load(id_file)


class Q1World(World):
    """
    Quake 1 Randomizer
    """

    game = "Quake 1"
    game_id = GAME_ID
    game_full_name = "Quake 1"

    item_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["items"].items()
    }
    location_name_to_id = {
        name: net_id(loc_id) for name, loc_id in game_ids["locations"].items()
    }
    item_name_groups = item_groups
    id_checksum = game_ids["checksum"]
    options_dataclass = Q1Options
    options: Q1Options

    def __init__(self, world: MultiWorld, player: int):
        self.included_levels: List[Q1Level] = []
        self.starting_levels: List[Q1Level] = []
        self.used_locations: Set[str] = set()
        # Add the id checksum of our location and item ids for consistency check with clients
        self.slot_data: Dict[str, Any] = {
            "checksum": self.id_checksum,
            "settings": {"dynamic": {}, "maximum": {}},
        }
        self.rules: Optional[Rules] = None
        # Filled later from options
        # self.fuel_per_pickup: Dict[str, int] = {}
        self._target_density: Optional[int] = None

        super().__init__(world, player)

    @classmethod
    def local_id(cls, ap_id: int) -> int:
        return local_id(ap_id)

    @classmethod
    def net_id(cls, short_id: int) -> int:
        return net_id(short_id)

    @property
    def target_density(self) -> int:
        """
        Cached version of _target_density, so we don't constantly calculate it
        """
        if self._target_density is None:
            density = self.get_option("location_density")
            if density == self.options.location_density.option_balanced:
                # bump up the value by 1 if secret areas are not enabled
                if not self.get_option("include_secrets") and self.get_option(
                    "goal"
                ) in (
                    self.options.goal.option_beat_all_levels,
                    self.options.goal.option_beat_all_bosses,
                ):
                    density += 1
            self._target_density = density
        return self._target_density

    def use_location(self, location: Optional[LocationDef] = None) -> bool:
        """
        Specify if a certain location should be included, based on world settings
        """
        if location is None:
            return False
        if location.density > self.target_density:
            print(
                "Ignoring location ",
                location.name,
                " because density is ",
                location.density,
            )
            return False
        if (
            location.classname == "trigger_secret"
            and self.get_option("goal")
            in (
                self.options.goal.option_beat_all_levels,
                self.options.goal.option_beat_all_bosses,
            )
            and not self.get_option("include_secrets")
        ):
            return False
        return True

    def get_option(self, option_name: str) -> Any:
        return getattr(self.multiworld, option_name)[self.player].value

    def calculate_levels(self):
        level_count = self.get_option("level_count")
        # total number of starting levels to include, based on the total count
        # TODO: Grab max episode levels dynamically
        if level_count < E1.maxlevel:
            start_count = 1
        elif level_count < 14:
            start_count = 2
        elif level_count < 24:
            start_count = 3
        else:
            start_count = 4
        shuffle_start = self.get_option("shuffle_starting_levels")
        goal_bosses = (
            self.get_option("goal") == self.options.goal.option_beat_all_bosses
        )

        level_candidates = []

        # Shuffle episodes so we pick random start levels
        episode_options = [1, 2, 3, 4]
        self.multiworld.random.shuffle(episode_options)
        for episode_id in episode_options:
            if self.get_option(f"episode{episode_id}"):
                episode = all_episodes[episode_id - 1]
                if not shuffle_start and len(self.starting_levels) < start_count:
                    # add the first level to the starting levels, and the rest into the randomize pool
                    # TODO: Test if this works on every generation
                    # special case for solo worlds and episode 1 only
                    if (
                        self.multiworld.players == 1
                        and episode_id == 1
                        and self.get_option("episode1")
                        and not self.get_option("episode2")
                        and not self.get_option("episode3")
                        and not self.get_option("episode4")
                    ):
                        choice = self.multiworld.random.randrange(1, E1.maxlevel)
                        self.starting_levels.append(episode.levels[choice])
                        self.included_levels.append(episode.levels[choice])
                        episode.levels.pop(choice)
                        episode_pool = episode.levels[: episode.maxlevel - 1]
                    else:
                        self.starting_levels.append(episode.levels[0])
                        self.included_levels.append(episode.levels[0])
                        episode_pool = episode.levels[1 : episode.maxlevel]
                else:
                    episode_pool = episode.levels[: episode.maxlevel]
                # If our goal is to kill bosses, include the boss levels!
                if goal_bosses:
                    for level in episode_pool:
                        if level.has_boss:
                            self.included_levels.append(level)
                # extend our candidate pool to pull from with all remaining eligible levels
                level_candidates.extend(
                    [
                        level
                        for level in episode_pool
                        if level not in self.included_levels
                    ]
                )
        # randomize the levels so we can pull from them
        self.multiworld.random.shuffle(level_candidates)
        # if we have random starting levels, sample them from the start of the shuffled list
        # this conveniently excludes boss levels from being immediately unlocked in all bosses mode!
        if shuffle_start:
            self.starting_levels = level_candidates[:start_count]
        # and then fill the included levels to the desired count
        self.included_levels.extend(
            level_candidates[: level_count - len(self.included_levels)]
        )

    def define_dynamic_item_props(self, item_name: str, new_props: Dict[str, Any]):
        """
        Creates a dynamic item definition entry with updated props.

        This is useful for dynamically scaling numeric values of items based on difficulty settings
        """
        item = all_items[item_name]
        item_data = {
            "name": item.name,
            "type": item.type,
        }
        if item.persistent:
            item_data["persistent"] = True
        if item.unique:
            item_data["unique"] = True
        if item.silent:
            item_data["silent"] = True
        item_data.update(**item.props)
        item_data.update(**new_props)

        self.slot_data["settings"]["dynamic"][str(item.ap_id)] = item_data

    DIFF_TO_FACTOR_MAPPING = {
        Difficulty.option_easy: 1,
        Difficulty.option_medium: 0.5,
        Difficulty.option_hard: 0.25,
        Difficulty.option_extreme: 0.125,
    }

    def generate_early(self) -> None:
        # Difficulty settings
        # Adds a mult factor for healing items based on difficulty
        factor = self.DIFF_TO_FACTOR_MAPPING.get(self.get_option("difficulty"))
        self.define_dynamic_item_props("Small Medkit", {"factor": factor})
        self.define_dynamic_item_props("Large Medkit", {"factor": factor})
        self.define_dynamic_item_props("Megahealth", {"factor": factor})

        # Configure rules
        self.rules = Rules(self)

        # Generate level pool
        self.calculate_levels()

        # Initial level unlocks
        for level in self.starting_levels:
            self.multiworld.start_inventory[self.player].value[level.unlock] = 1
        for level in self.included_levels:
            if self.get_option("area_maps") == self.options.area_maps.option_start_with:
                self.multiworld.start_inventory[self.player].value[level.map] = 1
        self.slot_data["settings"]["difficulty"] = self.get_option("skill_level")
        self.slot_data["settings"]["lock"] = {}
        if self.get_option("unlock_abilities"):
            self.slot_data["settings"]["lock"].update(
                {
                    "crouch": True,
                    "jump": True,
                    # TODO: Implement walk/run
                    # "run": True,
                    "dive": True,
                    "grenadejump": True,
                    "rocketjump": True,
                }
            )
        if self.get_option("damage_remover_abilities"):
            self.slot_data["settings"]["lock"].update(
                {
                    "rocketdmgsaver": True,
                    "grenadedmgsaver": True,
                }
            )
        if self.get_option("unlock_interact"):
            self.slot_data["settings"]["lock"].update(
                {
                    "door": True,
                    "button": True,
                }
            )
        self.slot_data["settings"]["no_save"] = not self.get_option("allow_saving")

    def create_regions(self):
        self.used_locations = set()
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        for level in self.included_levels:
            level_region = level.create_region(self)
            self.used_locations |= level.used_locations
            menu_region.connect(level_region, None, self.rules.level(level))
        self.slot_data["locations"] = [
            self.location_name_to_id[loc] for loc in self.used_locations
        ]
        self.slot_data["levels"] = [
            self.item_name_to_id[level.unlock] for level in self.included_levels
        ]

        goal_exits = self.get_option("goal") in {
            self.options.goal.option_beat_all_levels,
            self.options.goal.option_all,
        }
        goal_secrets = self.get_option("goal") in {
            self.options.goal.option_collect_all_secrets,
            self.options.goal.option_all,
        }
        goal_bosses = (
            self.get_option("goal") == self.options.goal.option_beat_all_bosses
        )
        goal_counts = {"Exit": 0, "Secret": 0, "Boss": 0}
        for level in self.included_levels:
            for location in level.locations.values():
                if location.name not in self.used_locations:
                    continue
                if goal_exits and location.classname == "trigger_changelevel":
                    goal_counts["Exit"] += 1
                elif goal_secrets and location.classname == "trigger_secret":
                    goal_counts["Secret"] += 1
                elif (
                    goal_bosses
                    and location.classname == "trigger_changelevel"
                    and level.has_boss
                ):
                    goal_counts["Boss"] += 1
        goal_percentage = self.get_option("goal_percentage")
        if goal_percentage < 100:
            for goal_type in ("Exit", "Secret", "Boss"):
                goal_counts[goal_type] = math.ceil(
                    0.01 * goal_percentage * goal_counts[goal_type]
                )

        self.slot_data["goal"] = {
            "Exit": {"id": self.item_name_to_id["Exit"], "count": goal_counts["Exit"]},
            "Secret": {
                "id": self.item_name_to_id["Secret"],
                "count": goal_counts["Secret"],
            },
            "Boss": {"id": self.item_name_to_id["Boss"], "count": goal_counts["Boss"]},
        }
        self.multiworld.completion_condition[self.player] = (
            self.rules.count("Exit", goal_counts["Exit"])
            & self.rules.count("Secret", goal_counts["Secret"])
            & self.rules.count("Boss", goal_counts["Boss"])
        )

    AMMO_NAMES = (
        "Shells",
        "Spikes",
        "Rockets",
        "Batteries",
    )

    def create_item(self, item: str, progression: bool = False) -> Q1Item:
        item_def = all_items.get(item)
        if progression:
            classification = ItemClassification.progression
        elif item_def.progression:
            classification = ItemClassification.progression
        elif item_def.persistent:
            classification = ItemClassification.useful
        elif item_def.type == "trap":
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        ret = Q1Item(item, classification, self.item_name_to_id[item], self.player)
        return ret

    def create_event(self, event_name: str) -> Q1Item:
        return Q1Item(event_name, ItemClassification.progression, None, self.player)

    def get_filler_item_name(self) -> str:
        # This should never be required with the item pool calculations, so we don't need any junk ratio logic here
        return "Nothing"

    def create_junk(self, count: int) -> List[Q1Item]:
        difficulty = self.get_option("difficulty")
        # TODO: Create difficulty based distribution of items
        if difficulty == self.options.difficulty.option_extreme:
            ratios = {
                "Nothing": 40,
                "Mini Heal (+1)": 40,
                "Mini Ammo (+1)": 40,
                "Small Medkit": 30,
                "Large Medkit": 10,
                "Megahealth": 1,
                "Quad Damage": 1,
                "Invulnerability": 1,
                "Biosuit": 1,
                "Invisibility": 1,
                "Backpack": 1,
            }
            trap_ratios = {
                "Low Health Trap": 6,
                "Death Trap": 6,
                "Enemy Trap": 3,
                "Mouse Trap": 3,
                "Sound Trap": 1,
                "Jump Trap": 1,
            }
        elif difficulty == self.options.difficulty.option_hard:
            ratios = {
                "Nothing": 30,
                "Mini Heal (+1)": 30,
                "Mini Ammo (+1)": 30,
                "Small Medkit": 30,
                "Large Medkit": 10,
                "Megahealth": 2,
                "Quad Damage": 2,
                "Invulnerability": 2,
                "Biosuit": 2,
                "Invisibility": 2,
                "Backpack": 2,
            }
            trap_ratios = {
                "Low Health Trap": 4,
                "Death Trap": 4,
                "Enemy Trap": 3,
                "Mouse Trap": 3,
                "Sound Trap": 2,
                "Jump Trap": 2,
            }
        elif difficulty == self.options.difficulty.option_medium:
            ratios = {
                "Small Medkit": 40,
                "Large Medkit": 20,
                "Megahealth": 3,
                "Quad Damage": 3,
                "Invulnerability": 3,
                "Biosuit": 3,
                "Invisibility": 3,
                "Backpack": 3,
            }
            trap_ratios = {
                "Low Health Trap": 2,
                "Death Trap": 2,
                "Enemy Trap": 3,
                "Mouse Trap": 3,
                "Sound Trap": 3,
                "Jump Trap": 3,
            }
        else:
            ratios = {
                "Small Medkit": 50,
                "Large Medkit": 30,
                "Megahealth": 10,
                "Quad Damage": 5,
                "Invulnerability": 5,
                "Biosuit": 5,
                "Invisibility": 5,
                "Backpack": 5,
            }
            trap_ratios = {
                "Low Health Trap": 1,
                "Death Trap": 1,
                "Enemy Trap": 4,
                "Mouse Trap": 4,
                "Sound Trap": 8,
                "Jump Trap": 8,
            }
        # create sample lists
        pool = []
        for key, value in ratios.items():
            pool += [key] * value
        trap_pool = []
        for key, value in trap_ratios.items():
            trap_pool += [key] * value
        # and just generate items at the appropriate ratios
        trap_count = math.floor((self.get_option("trap_percentage") / 100.0) * count)
        return [
            self.create_item(self.multiworld.random.choice(pool))
            for _ in range(count - trap_count)
        ] + [
            self.create_item(self.multiworld.random.choice(trap_pool))
            for _ in range(trap_count)
        ]

    def create_item_list(self, item_list: List[str]) -> List[Q1Item]:
        return [self.create_item(item) for item in item_list]

    # TODO: Update this when all episodes are mapped
    HEALTH_DIFF_TO_REQ_MAPPING = {
        Difficulty.option_easy: {
            "Small Medkit": (2, 20),
            "Large Medkit": (2, 20),
            "Megahealth": (2, 20),
        },
        Difficulty.option_medium: {
            "Small Medkit": (4, 15),
            "Large Medkit": (4, 15),
            "Megahealth": (4, 15),
        },
        Difficulty.option_hard: {
            "Small Medkit": (8, 10),
            "Large Medkit": (8, 10),
            "Megahealth": (8, 10),
        },
        Difficulty.option_extreme: {
            "Small Medkit": (10, 10),
            "Large Medkit": (10, 10),
            "Megahealth": (10, 10),
        },
    }

    def generate_health(self, inv_type: str) -> Tuple[List[Q1Item], List[Q1Item]]:
        required, total = self.HEALTH_DIFF_TO_REQ_MAPPING.get(
            self.get_option("difficulty"), self.options.difficulty.option_medium
        )[inv_type]
        required_list = [self.create_item(inv_type, True) for _ in range(required)]
        # Fill pool with capacity up to total amount
        useful_list = [
            self.create_item(inv_type) for _ in range(total - len(required_list))
        ]
        return required_list, useful_list

    INV_DIFF_TO_REQ_MAPPING = {
        Difficulty.option_easy: {
            "Quad Damage": (0, 5),
            "Invulnerability": (0, 5),
            "Biosuit": (0, 5),
            "Invisibility": (0, 5),
            "Backpack": (0, 5),
        },
        Difficulty.option_medium: {
            "Quad Damage": (0, 3),
            "Invulnerability": (0, 3),
            "Biosuit": (0, 3),
            "Invisibility": (0, 3),
            "Backpack": (0, 3),
        },
        Difficulty.option_hard: {
            "Quad Damage": (0, 2),
            "Invulnerability": (0, 2),
            "Biosuit": (0, 2),
            "Invisibility": (0, 2),
            "Backpack": (0, 2),
        },
        Difficulty.option_extreme: {
            "Quad Damage": (0, 1),
            "Invulnerability": (0, 1),
            "Biosuit": (0, 1),
            "Invisibility": (0, 1),
            "Backpack": (0, 1),
        },
    }

    def generate_inventories(
        self, inv_type: str, prog_override_amount: int = 0
    ) -> Tuple[List[Q1Item], List[Q1Item]]:
        required, total = self.INV_DIFF_TO_REQ_MAPPING.get(
            self.get_option("difficulty"), self.options.difficulty.option_medium
        )[inv_type]

        # One base item and rest is capacity, unless we have progressive inventories
        progressive = self.get_option("progressive_inventories")
        if progressive:
            main_name = f"Progressive {inv_type}"
            cap_name = main_name
        else:
            main_name = inv_type
            cap_name = f"{inv_type} Capacity"
        required_list = [self.create_item(main_name, True)] + [
            self.create_item(cap_name, True)
            for _ in range(required - 1 + prog_override_amount)
        ]
        # Fill pool with capacity up to total amount
        useful_list = [
            self.create_item(cap_name) for _ in range(total - len(required_list))
        ]
        return required_list, useful_list

    # TODO: Adjust this with new values for Quake
    # Tuples of starting max and target max
    DIFF_TO_MAX_MAPPING = {
        Difficulty.option_easy: {
            "Shells": (25, 100),
            "Spikes": (50, 200),
            "Rockets": (10, 100),
            "Batteries": (50, 200),
        },
        Difficulty.option_medium: {
            "Shells": (25, 100),
            "Spikes": (50, 200),
            "Rockets": (10, 100),
            "Batteries": (50, 200),
        },
        Difficulty.option_hard: {
            "Shells": (25, 100),
            "Spikes": (50, 200),
            "Rockets": (10, 100),
            "Batteries": (50, 200),
        },
        Difficulty.option_extreme: {
            "Shells": (25, 100),
            "Spikes": (50, 200),
            "Rockets": (10, 100),
            "Batteries": (50, 200),
        },
    }

    def useful_items_per_difficulty(self, available_slots: int) -> List[Q1Item]:
        if available_slots <= 0:
            # Out of space already, can abort
            return []

        ret_items = {}
        # We want about 35% of remaining slots to be filled with ammo expansions, so calculated the amount we get
        # for each of the 4 ammo types
        expansions_per_ammo = math.ceil(available_slots * 0.035)
        for ammo_type in self.AMMO_NAMES:
            start, target = self.DIFF_TO_MAX_MAPPING.get(
                self.get_option("difficulty"), self.options.difficulty.option_medium
            )[ammo_type]
            self.slot_data["settings"]["maximum"][ammo_type.lower()] = start
            difference = target - start
            if difference <= 0:
                continue
            capacity_per = math.ceil(float(difference) / expansions_per_ammo)
            count = math.ceil(float(difference) / capacity_per)
            # configure the capacity for each upgrade dynamically
            self.define_dynamic_item_props(
                f"{ammo_type} Capacity",
                {"capacity": capacity_per, "ammo": math.ceil(capacity_per / 2.0)},
            )
            # and add the right count to our pool
            if self.get_option("progressive_weapons"):
                ret_items[f"Progressive {ammo_type}"] = count
            else:
                ret_items[f"{ammo_type} Capacity"] = count

        # Is there a good comprehension for this?
        ret = []
        for key, count in ret_items.items():
            ret += [self.create_item(key) for _ in range(count)]
        return ret

    def create_items(self):
        itempool = []  # Absolutely mandatory progression items
        useful_items = (
            []
        )  # Stuff that should be in the world if there's enough locations
        used_locations = self.used_locations.copy()
        # Place goal items and level keys
        # ToDo remove this code duplications
        goal_exits = self.get_option("goal") in {
            self.options.goal.option_beat_all_levels,
            self.options.goal.option_all,
        }
        goal_secrets = self.get_option("goal") in {
            self.options.goal.option_collect_all_secrets,
            self.options.goal.option_all,
        }
        goal_bosses = (
            self.get_option("goal") == self.options.goal.option_beat_all_bosses
        )
        for level in self.included_levels:
            for location in level.locations.values():
                if (
                    goal_exits
                    and location.name in self.used_locations
                    and location.classname == "trigger_changelevel"
                ):
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Exit"))
                    used_locations.remove(location.name)
                elif (
                    goal_secrets
                    and location.name in self.used_locations
                    and location.classname == "trigger_secret"
                ):
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Secret"))
                    used_locations.remove(location.name)
                elif (
                    goal_bosses
                    and location.name in self.used_locations
                    and location.classname == "trigger_changelevel"
                    and level.has_boss
                ):
                    self.multiworld.get_location(
                        location.name, self.player
                    ).place_locked_item(self.create_item("Boss"))
                    used_locations.remove(location.name)
            # create and fill event items
            for event in level.events:
                prefixed_event = f"{level.prefix} {event}"
                self.multiworld.get_location(
                    prefixed_event, self.player
                ).place_locked_item(self.create_event(prefixed_event))
            itempool += [self.create_item(item) for item in level.items]
            if level.unlock not in self.multiworld.start_inventory[self.player].value:
                itempool.append(self.create_item(level.unlock))
            if self.get_option("area_maps") == self.options.area_maps.option_unlockable:
                useful_items.append(self.create_item(level.map))

        if self.get_option("unlock_abilities"):
            itempool += self.create_item_list(
                [
                    "Jump",
                    "Dive",
                    "Grenade Jump",
                    "Rocket Jump",
                ]
            )

        if self.get_option("unlock_interact"):
            itempool += self.create_item_list(["Door", "Button", "Shoot Switch"])

        if self.get_option("damage_remover_abilities"):
            itempool += self.create_item_list(
                ["Grenade Damage Remover", "Rocket Damage Remover"]
            )

        # Add progression items
        progressive_weapons = self.get_option("progressive_weapons")
        # Place explosive weapons into the required itempool
        if progressive_weapons:
            itempool += self.create_item_list(
                [
                    "Progressive Grenade Launcher",
                    "Progressive Rocket Launcher",
                ]
            )
        else:
            itempool += self.create_item_list(["Grenade Launcher", "Rocket Launcher"])
        # TODO: Implement this part if required
        # Get progression inventory based on difficulty settings
        required, useful = self.generate_health("Small Medkit")
        itempool += required
        useful_items += useful
        required, useful = self.generate_health("Large Medkit")
        itempool += required
        useful_items += useful
        required, useful = self.generate_health("Megahealth")
        itempool += required
        useful_items += useful
        """
        required, useful = self.generate_inventories("Jetpack")
        itempool += required
        useful_items += useful
        required, useful = self.generate_inventories("Scuba Gear")
        """
        # Invulnerability or Biosuit is required for some locations
        need_invuln = False
        need_bio = False
        for level in self.included_levels:
            if level.must_invuln:
                need_invuln = True
            if level.must_bio:
                need_bio = True
        if need_invuln:
            itempool.append(self.create_item("Invulnerability", True))
        if need_bio:
            itempool.append(self.create_item("Biosuit", True))
        inventory_items = [
            "Quad Damage",
            "Invulnerability",
            "Biosuit",
            "Invisibility",
            "Backpack",
        ]
        for itemname in inventory_items:
            required, useful = self.generate_inventories(itemname)
            itempool += required
            useful_items += useful

        # Can fail now if we don't even have enough slots for our required items
        if len(itempool) > len(used_locations):
            raise RuntimeError(
                "Not enough locations for all mandatory items with these settings!"
            )

        # Add one copy of each remaining weapon to the pool
        if progressive_weapons:
            useful_items += self.create_item_list(
                [
                    "Progressive Super Shotgun",
                    "Progressive Nailgun",
                    "Progressive Super Nailgun",
                    "Progressive Thunderbolt",
                ]
            )
        else:
            useful_items += self.create_item_list(
                ["Super Shotgun", "Nailgun", "Super Nailgun", "Thunderbolt"]
            )

        # count out remaining slots left to be filled
        open_slots = len(used_locations) - (len(itempool) + len(useful_items))
        useful_items += self.useful_items_per_difficulty(open_slots)

        if len(itempool) + len(useful_items) > len(used_locations):
            discarded = len(itempool) + len(useful_items) - len(used_locations)
            print(
                f"Had to discard {discarded} useful items from the pool: Not enough locations available"
            )

        # Add as much useful stuff as can fit
        # shuffle up the useful items so random ones get discarded if required
        self.multiworld.random.shuffle(useful_items)
        itempool.extend(useful_items[: len(used_locations) - len(itempool)])

        # Add filler
        itempool += self.create_junk(len(used_locations) - len(itempool))

        self.multiworld.itempool += itempool

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.slot_data

    # Used to supply the Universal Tracker with level shuffle data
    def interpret_slot_data(self, slot_data: Dict[str, Any]):
        menu_region = self.multiworld.get_region("Menu", self.player)
        unlocklist = slot_data["levels"]
        for level in all_levels:
            if self.item_name_to_id[level.unlock] in unlocklist:
                level_region = level.create_region(self)
                menu_region.connect(level_region, None, self.rules.level(level))
