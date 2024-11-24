from typing import Dict

from ..base_classes import ItemDef
from ..id import net_id
from ..levels import all_levels

automap_base_id = 1600
unlock_base_id = 1700
key_base_id = 1800

# Filled step by step below for readability
item_groups = {}

dynamic_level_items = {}

for level in all_levels:
    # automap
    automap = ItemDef(
        f"{level.prefix} Automap",
        net_id(automap_base_id),
        "automap",
        {"levelnum": level.levelnum, "volumenum": level.volumenum},
        persistent=True,
        unique=True,
    )
    automap_base_id += 1
    dynamic_level_items[automap.name] = automap

    # unlock
    unlock = ItemDef(
        f"{level.prefix} Unlock",
        net_id(unlock_base_id),
        "map",
        {},
        persistent=True,
        unique=True,
        progression=True,
    )
    unlock_base_id += 1
    dynamic_level_items[unlock.name] = unlock

    # keys
    for color in level.keys:
        if color == "Silver":
            flags = 1
        elif color == "Gold":
            flags = 2
        else:
            continue
        key = ItemDef(
            f"{level.prefix} {color} Key",
            net_id(key_base_id),
            "key",
            {"flags": flags, "levelnum": level.levelnum, "volumenum": level.volumenum},
            persistent=True,
            unique=True,
            progression=True,
        )
        key_base_id += 1
        dynamic_level_items[key.name] = key

goal_items = {
    "Exit": ItemDef(
        "Exit", net_id(100), "goal", {}, silent=True, persistent=True, progression=True
    ),
    "Secret": ItemDef(
        "Secret",
        net_id(101),
        "goal",
        {},
        silent=True,
        persistent=True,
        progression=True,
    ),
    "Boss": ItemDef(
        "Boss",
        net_id(102),
        "goal",
        {},
        silent=True,
        persistent=True,
        progression=True,
    ),
}

junk_items = {
    "Nothing": ItemDef("Nothing", net_id(0), "filler", {}, silent=True),
    "Mini Heal (+1)": ItemDef(
        "Mini Heal (+1)",
        net_id(403),
        "health",
        {"heal": 1, "overheal": True},
    ),
    "Mini Ammo (+1)": ItemDef(
        "Mini Ammo (+1)",
        net_id(404),
        "ammo",
        {"amount": 1},
    ),
}

weapons = {
    "Super Shotgun": ItemDef(
        "Super Shotgun",
        net_id(201),
        "weapon",
        {"weaponnum": 3, "ammo": 30},
        unique=True,
        persistent=True,
    ),
    "Nailgun": ItemDef(
        "Nailgun",
        net_id(202),
        "weapon",
        {"weaponnum": 4, "ammo": 50},
        unique=True,
        persistent=True,
    ),
    "Super Nailgun": ItemDef(
        "Super Nailgun",
        net_id(203),
        "weapon",
        {"weaponnum": 5, "ammo": 50},
        unique=True,
        persistent=True,
    ),
    "Grenade Launcher": ItemDef(
        "Grenade Launcher",
        net_id(204),
        "weapon",
        {"weaponnum": 6, "ammo": 5},
        unique=True,
        persistent=True,
        progression=True,
    ),
    "Rocket Launcher": ItemDef(
        "Rocket Launcher",
        net_id(205),
        "weapon",
        {"weaponnum": 7, "ammo": 5},
        unique=True,
        persistent=True,
        progression=True,
    ),
    "Thunderbolt": ItemDef(
        "Thunderbolt",
        net_id(206),
        "weapon",
        {"weaponnum": 8},
        unique=True,
        persistent=True,
    ),
}

progressive_weapons = {
    "Progressive Shotgun": ItemDef(
        "Progressive Shotgun",
        net_id(241),
        "progressive",
        {"items": [221]},
        silent=True,
        persistent=True,
    ),
    "Progressive Super Shotgun": ItemDef(
        "Progressive Super Shotgun",
        net_id(242),
        "progressive",
        {"items": [201, 221]},
        silent=True,
        persistent=True,
    ),
    "Progressive Nailgun": ItemDef(
        "Progressive Nailgun",
        net_id(242),
        "progressive",
        {"items": [202, 222]},
        unique=True,
        persistent=True,
    ),
    "Progressive Super Nailgun": ItemDef(
        "Progressive Super Nailgun",
        net_id(243),
        "progressive",
        {"items": [203, 222]},
        unique=True,
        persistent=True,
    ),
    "Progressive Grenade Launcher": ItemDef(
        "Progressive Grenade Launcher",
        net_id(244),
        "progressive",
        {"items": [204, 223]},
        silent=True,
        persistent=True,
        progression=True,
    ),
    "Progressive Rocket Launcher": ItemDef(
        "Progressive Rocket Launcher",
        net_id(245),
        "progressive",
        {"items": [205, 223]},
        silent=True,
        persistent=True,
        progression=True,
    ),
    "Progressive Thunderbolt": ItemDef(
        "Progressive Thunderbolt",
        net_id(246),
        "progressive",
        {"items": [206, 224]},
        silent=True,
        unique=True,
        persistent=True,
    ),
}

weapon_capacity = {
    "Shells Capacity": ItemDef(
        "Shells Capacity",
        net_id(221),
        "ammo",
        {"weaponnum": 3, "capacity": 10, "ammo": 10},
        persistent=True,
    ),
    "Spikes Capacity": ItemDef(
        "Spikes Capacity",
        net_id(222),
        "ammo",
        {"weaponnum": 5, "capacity": 50, "ammo": 25},
        persistent=True,
    ),
    "Rockets Capacity": ItemDef(
        "Rockets Capacity",
        net_id(223),
        "ammo",
        {"weaponnum": 7, "capacity": 5, "ammo": 10},
        persistent=True,
    ),
    "Batteries Capacity": ItemDef(
        "Batteries Capacity",
        net_id(224),
        "ammo",
        {"weaponnum": 8, "capacity": 50, "ammo": 25},
        persistent=True,
    ),
}

ammo = {
    "Shells Ammo": ItemDef(
        "Shells Ammo",
        net_id(261),
        "ammo",
        {"weaponnum": 3, "ammo": 15},
    ),
    "Spikes Ammo": ItemDef(
        "Spikes Ammo",
        net_id(262),
        "ammo",
        {"weaponnum": 5, "ammo": 100},
    ),
    "Rockets Ammo": ItemDef(
        "Rockets Ammo",
        net_id(263),
        "ammo",
        {"weaponnum": 7, "ammo": 10},
    ),
    "Batteries Ammo": ItemDef(
        "Batteries Ammo",
        net_id(264),
        "ammo",
        {"weaponnum": 8, "ammo": 25},
    ),
}

item_groups["Super Shotgun"] = {"Super Shotgun", "Progressive Super Shotgun"}
item_groups["Nailgun"] = {"Nailgun", "Progressive Nailgun"}
item_groups["Super Nailgun"] = {"Super Nailgun", "Progressive Super Nailgun"}
item_groups["Grenade Launcher"] = {"Grenade Launcher", "Progressive Grenade Launcher"}
item_groups["Rocket Launcher"] = {"Rocket Launcher", "Progressive Rocket Launcher"}
item_groups["Thunderbolt"] = {"Thunderbolt", "Progressive Thunderbolt"}

abilities = {
    "Jump": ItemDef(
        "Jump",
        net_id(350),
        "ability",
        {"enables": "jump"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Dive": ItemDef(
        "Dive",
        net_id(351),
        "ability",
        {"enables": "dive"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Door": ItemDef(
        "Door",
        net_id(354),
        "ability",
        {"enables": "door"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Button": ItemDef(
        "Button",
        net_id(355),
        "ability",
        {"enables": "button"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Shoot Switch": ItemDef(
        "Shoot Switch",
        net_id(356),
        "ability",
        {"enables": "shootswitch"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Grenade Jump": ItemDef(
        "Grenade Jump",
        net_id(357),
        "ability",
        {"enables": "grenadejump"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Rocket Jump": ItemDef(
        "Rocket Jump",
        net_id(358),
        "ability",
        {"enables": "rocketjump"},
        persistent=True,
        unique=True,
        progression=True,
    ),
    "Grenade Damage Remover": ItemDef(
        "Grenade Damage Remover",
        net_id(359),
        "ability",
        {"enables": "grenadedmgremover"},
        persistent=True,
        unique=True,
        progression=False,
    ),
    "Rocket Damage Remover": ItemDef(
        "Rocket Damage Remover",
        net_id(360),
        "ability",
        {"enables": "rocketdmgremover"},
        persistent=True,
        unique=True,
        progression=False,
    ),
}

healing_items = {
    "Small Medkit": ItemDef(
        "Small Medkit",
        net_id(400),
        "health",
        {"heal": 15},
        persistent=True,
        silent=True,
    ),
    "Large Medkit": ItemDef(
        "Large Medkit",
        net_id(401),
        "health",
        {"heal": 25},
        persistent=True,
        silent=True,
    ),
    "Megahealth": ItemDef(
        "Megahealth",
        net_id(402),
        "health",
        {"heal": 100},
        persistent=True,
        silent=True,
    ),
    "Green Armor": ItemDef(
        "Green Armor",
        net_id(404),
        "armor",
        {"armor": 100},
        persistent=True,
        silent=True,
    ),
    "Yellow Armor": ItemDef(
        "Yellow Armor",
        net_id(405),
        "armor",
        {"armor": 150},
        persistent=True,
        silent=True,
    ),
    "Red Armor": ItemDef(
        "Red Armor",
        net_id(406),
        "armor",
        {"armor": 200},
        persistent=True,
        silent=True,
    ),
}

inventory_items = {
    "Quad Damage": ItemDef(
        "Quad Damage",
        net_id(301),
        "inventory",
        {"invnum": 0, "capacity": 1},
        persistent=True,
        unique=True,
    ),
    "Invulnerability": ItemDef(
        "Invulnerability",
        net_id(302),
        "inventory",
        {"invnum": 1, "capacity": 1},
        persistent=True,
        unique=True,
    ),
    "Biosuit": ItemDef(
        "Biosuit",
        net_id(303),
        "inventory",
        {"invnum": 2, "capacity": 1},
        persistent=True,
        unique=True,
    ),
    "Invisibility": ItemDef(
        "Invisibility",
        net_id(304),
        "inventory",
        {"invnum": 3, "capacity": 1},
        persistent=True,
        unique=True,
    ),
    "Backpack": ItemDef(
        "Backpack",
        net_id(305),
        "inventory",
        {"invnum": 4, "capacity": 1},
        persistent=True,
        unique=True,
    ),
}

inventory_items_capacity = {
    "Quad Damage Capacity": ItemDef(
        "Quad Damage Capacity",
        net_id(321),
        "invcapacity",
        {"invnum": 0, "capacity": 1},
        persistent=True,
    ),
    "Invulnerability Capacity": ItemDef(
        "Invulnerability Capacity",
        net_id(322),
        "invcapacity",
        {"invnum": 1, "capacity": 1},
        persistent=True,
    ),
    "Biosuit Capacity": ItemDef(
        "Biosuit Capacity",
        net_id(323),
        "invcapacity",
        {"invnum": 2, "capacity": 1},
        persistent=True,
    ),
    "Invisibility Capacity": ItemDef(
        "Invisibility Capacity",
        net_id(324),
        "invcapacity",
        {"invnum": 3, "capacity": 1},
        persistent=True,
    ),
    "Backpack Capacity": ItemDef(
        "Backpack Capacity",
        net_id(325),
        "invcapacity",
        {"invnum": 4, "capacity": 1},
        persistent=True,
    ),
}

inventory_items_progressive = {
    "Progressive Quad Damage": ItemDef(
        "Progressive Quad Damage",
        net_id(341),
        "progressive",
        {"items": [301, 321]},
        persistent=True,
        silent=True,
    ),
    "Progressive Invulnerability": ItemDef(
        "Progressive Invulnerability",
        net_id(342),
        "progressive",
        {"items": [302, 322]},
        persistent=True,
        silent=True,
    ),
    "Progressive Biosuit": ItemDef(
        "Progressive Biosuit",
        net_id(343),
        "progressive",
        {"items": [303, 323]},
        persistent=True,
        silent=True,
    ),
    "Progressive Invisibility": ItemDef(
        "Progressive Invisibility",
        net_id(344),
        "progressive",
        {"items": [304, 324]},
        persistent=True,
        silent=True,
    ),
    "Progressive Backpack": ItemDef(
        "Progressive Backpack",
        net_id(345),
        "progressive",
        {"items": [305, 325]},
        persistent=True,
        silent=True,
    ),
}

# TODO: Create item groups and progressive items
item_groups["Biosuit"] = {"Biosuit", "Progressive Biosuit"}
item_groups["Biosuit Capacity"] = {"Biosuit", "Biosuit Capacity", "Progressive Biosuit"}
item_groups["Quad Damage"] = {"Quad Damage", "Progressive Quad Damage"}
item_groups["Quad Damage Capacity"] = {
    "Quad Damage",
    "Quad Damage Capacity",
    "Progressive Quad Damage",
}
item_groups["Invulnerability"] = {"Invulnerability", "Progressive Invulnerability"}
item_groups["Invulnerability Capacity"] = {
    "Invulnerability",
    "Invulnerability Capacity",
    "Progressive Invulnerability",
}
item_groups["Invisibility"] = {"Invisibility", "Progressive Invisibility"}
item_groups["Invisibility Capacity"] = {
    "Invisibility",
    "Invisibility Capacity",
    "Progressive Invisibility",
}
item_groups["Backpack"] = {"Backpack", "Progressive Backpack"}
item_groups["Backpack Capacity"] = {
    "Backpack",
    "Backpack Capacity",
    "Progressive Backpack",
}

traps = {
    "Low Health Trap": ItemDef(
        "Low Health Trap",
        net_id(500),
        "trap",
        {"trap": "lowhealth", "duration": 1, "grace": 1500},
        silent=True,
    ),
    "Death Trap": ItemDef(
        "Death Trap",
        net_id(501),
        "trap",
        {"trap": "death", "duration": 1, "grace": 5000},
        silent=True,
    ),
    "Enemy Trap": ItemDef(
        "Enemy Trap",
        net_id(502),
        "trap",
        {"trap": "enemy", "duration": 1, "grace": 200},
        silent=True,
    ),
    "Mouse Trap": ItemDef(
        "Mouse Trap",
        net_id(503),
        "trap",
        {"trap": "mouse", "duration": 200, "grace": 2000},
        silent=True,
    ),
    "Sound Trap": ItemDef(
        "Sound Trap",
        net_id(504),
        "trap",
        {"trap": "sound", "duration": 200, "grace": 2000},
        silent=True,
    ),
    "Jump Trap": ItemDef(
        "Jump Trap",
        net_id(505),
        "trap",
        {"trap": "jump", "duration": 200, "grace": 2000},
        silent=True,
    ),
}

# These don't have defined values and exist solely to be replaced by unique, seed specifically generated items
dynamic_items = {
    f"Dynamic{i +1}": ItemDef(
        f"Dynamic{i + 1}", net_id(600 + i), "filler", {}, silent=True
    )
    for i in range(16)
}

all_items: Dict[str, ItemDef] = {
    **junk_items,
    **goal_items,
    **weapons,
    **progressive_weapons,
    **weapon_capacity,
    **ammo,
    **healing_items,
    **inventory_items,
    **inventory_items_capacity,
    **inventory_items_progressive,
    **abilities,
    **dynamic_level_items,
    **traps,
    **dynamic_items,
}
