from BaseClasses import Region

from ..base_classes import Q1Level


class E1M4(Q1Level):
    name = "The Grisly Grotto"
    levelnum = 3
    volumenum = 0
    keys = ["Silver"]
    location_defs = [
        {
            "id": 11,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 33,
            "name": "Yellow Armor (33)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Large Medkit (34)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Large Medkit (35)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Large Medkit (46)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Silver Key (47)",
            "classname": "item_key1",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Large Medkit (58)",
            "classname": "item_health",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Small Medkit (59)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 60,
            "name": "Spikes (60)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Spikes (61)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 67,
            "name": "Large Medkit (67)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 68,
            "name": "Shells (68)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 87,
            "name": "Shells (87)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 88,
            "name": "Large Medkit (88)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 89,
            "name": "Large Medkit (89)",
            "classname": "item_health",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 90,
            "name": "Shells (90)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 91,
            "name": "Large Medkit (91)",
            "classname": "item_health",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 92,
            "name": "Small Medkit (92)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 106,
            "name": "Large Medkit (106)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 107,
            "name": "Large Medkit (107)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 110,
            "name": "Yellow Armor (110)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 113,
            "name": "Small Medkit (113)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 114,
            "name": "Spikes (114)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 115,
            "name": "Small Medkit (115)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 120,
            "name": "Shells (120)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 121,
            "name": "Large Medkit (121)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 122,
            "name": "Rockets (122)",
            "classname": "item_rockets",
            "spawnflags": 1025.0,
            "density": 0,
        },
        {
            "id": 123,
            "name": "Spikes (123)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 124,
            "name": "Spikes (124)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 132,
            "name": "Shells (132)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 133,
            "name": "Large Medkit (133)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 134,
            "name": "Shells (134)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 138,
            "name": "Supernailgun (138)",
            "classname": "weapon_supernailgun",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 139,
            "name": "Spikes (139)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 140,
            "name": "Shells (140)",
            "classname": "item_shells",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 148,
            "name": "Shells (148)",
            "classname": "item_shells",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 149,
            "name": "Spikes (149)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 158,
            "name": "Spikes (158)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        # TODO: Figure out how to catch this client-sided
        # This secret is not actively triggered by the player, shoot buttons activate it
        # {
        #    "id": 160,
        #    "name": "Secret (160)",
        #    "classname": "trigger_secret",
        #    "spawnflags": 0.0,
        # },
        {
            "id": 168,
            "name": "Large Medkit (168)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Large Medkit (169)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 176,
            "name": "Large Medkit (176)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 177,
            "name": "Secret (177)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 182,
            "name": "Secret Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 185,
            "name": "Spikes (185)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 216,
            "name": "Rockets (216)",
            "classname": "item_rockets",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 217,
            "name": "Shells (217)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 218,
            "name": "Small Medkit (218)",
            "classname": "item_health",
            "spawnflags": 2305.0,
            "density": 0,
        },
        {
            "id": 219,
            "name": "Spikes (219)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 220,
            "name": "Spikes (220)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 221,
            "name": "Biosuit (221)",
            "classname": "item_artifact_envirosuit",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 227,
            "name": "Secret (227)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 229,
            "name": "Spikes (229)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 230,
            "name": "Spikes (230)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 231,
            "name": "Shells (231)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 232,
            "name": "Shells (232)",
            "classname": "item_shells",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 236,
            "name": "Spikes (236)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 240,
            "name": "Grenadelauncher (240)",
            "classname": "weapon_grenadelauncher",
            "spawnflags": 0.0,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Large Medkit (34)",
                "Large Medkit (35)",
                "Small Medkit (218)",
                "Shells (232)",
            ],
        )

        past_spawn_door_area = self.region(
            "Past Spawn Door",
            [
                "Yellow Armor (33)",
                "Shells (90)",
                "Spikes (236)",
                "Large Medkit (46)",
                "Biosuit (221)",
                "Spikes (185)",
            ],
        )
        self.connect(ret, past_spawn_door_area, r.can_door)

        self.restrict("Yellow Armor (33)", r.can_shootswitch)

        lake_platform_area = self.region(
            "Lake Platform",
            [
                "Silver Key (47)",
                "Large Medkit (133)",
                "Shells (148)",
                "Shells (134)",
                "Spikes (139)",
                "Spikes (149)",
            ],
        )
        self.connect(
            past_spawn_door_area,
            lake_platform_area,
            ((((r.can_rj_hard) | (r.can_gj_extr & r.can_jump))) | r.can_dive),
        )

        lake_cave_area = self.region(
            "Lake Secret Cave",
            [
                "Secret (227)",
                "Rockets (216)",
            ],
        )
        self.connect(past_spawn_door_area, lake_cave_area, r.can_dive)

        lake_underwater_area = self.region(
            "Lake Underwater Area",
            [
                "Large Medkit (91)",
                "Small Medkit (92)",
                "Large Medkit (67)",
                "Shells (68)",
                "Supernailgun (138)",
                "Spikes (220)",
                "Spikes (219)",
                # past elevator
                "Small Medkit (115)",
                "Large Medkit (58)",
                "Small Medkit (59)",
                "Spikes (60)",
                "Spikes (61)",
                "Spikes (230)",
            ],
        )
        self.connect(past_spawn_door_area, lake_underwater_area, r.can_dive)
        # inside via button press
        self.connect(lake_underwater_area, lake_platform_area, r.can_button)

        castle_area = self.region(
            "Castle Area",
            [
                "Shells (87)",
                "Large Medkit (88)",
                "Large Medkit (89)",
                "Spikes (229)",
            ],
        )
        self.connect(past_spawn_door_area, castle_area, r.can_dive)

        castle_upper_outside_area = self.region(
            "Castle Upper Outside Area",
            [
                "Shells (120)",
                "Shells (231)",
                "Large Medkit (121)",
                "Exit",
            ],
        )

        castle_inside_area = self.region(
            "Castle Inside Area",
            [
                "Spikes (114)",
                "Spikes (123)",
                "Spikes (124)",
                "Yellow Armor (110)",
                "Shells (132)",
                "Shells (140)",
                "Shells (217)",
                "Small Medkit (113)",
                "Large Medkit (106)",
                "Large Medkit (107)",
            ],
        )
        self.restrict("Yellow Armor (110)", r.can_button)

        # rj/gj from the water sloped surface
        self.connect(
            castle_area,
            castle_inside_area,
            self.silver_key | (r.can_jump & ((r.can_rj_hard) | (r.can_gj_extr))),
        )

        self.connect(castle_inside_area, castle_upper_outside_area, r.can_door)

        # this only spawns on hard+ difficulty because a monster opens the closet
        self.restrict("Shells (217)", r.skill("hard") | r.skill("nightmare"))

        castle_inside_sides_area = self.region(
            "Castle Inside Sides Area",
            [
                "Rockets (122)",
                "Spikes (158)",
                "Large Medkit (168)",
                "Large Medkit (169)",
            ],
        )
        self.connect(
            castle_inside_area,
            castle_inside_sides_area,
            r.can_button
            | (r.can_jump & ((r.can_rj & r.difficulty("medium")) | (r.can_gj_hard))),
        )

        # secret cave needs buttons pressed
        lake_super_secret = self.region(
            "Lake Super Secret Area",
            [
                "Secret (177)",
                "Grenadelauncher (240)",
                "Large Medkit (176)",
                "Secret Exit",
            ],
        )
        self.connect(castle_inside_sides_area, lake_super_secret, r.can_button)

        return ret
