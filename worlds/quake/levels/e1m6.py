from BaseClasses import Region

from ..base_classes import Q1Level


class E1M6(Q1Level):
    name = "The Door To Chthon"
    levelnum = 5
    volumenum = 0
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 10,
            "name": "Gold Key (10)",
            "classname": "item_key2",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Silver Key (25)",
            "classname": "item_key1",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Supernailgun (43)",
            "classname": "weapon_supernailgun",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 56,
            "name": "Large Medkit (56)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Large Medkit (57)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Large Medkit (58)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 59,
            "name": "Large Medkit (59)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 61,
            "name": "Megahealth (61)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 78,
            "name": "Megahealth (78)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 101,
            "name": "Shells (101)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 105,
            "name": "Rockets (105)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 106,
            "name": "Shells (106)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 117,
            "name": "Large Medkit (117)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 141,
            "name": "Secret (141)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 168,
            "name": "Rockets (168)",
            "classname": "item_rockets",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Secret (169)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 174,
            "name": "Secret (174)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 175,
            "name": "Spikes (175)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 205,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 208,
            "name": "Large Medkit (208)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 209,
            "name": "Shells (209)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 210,
            "name": "Spikes (210)",
            "classname": "item_spikes",
            "spawnflags": 3073.0,
            "density": 0,
        },
        {
            "id": 211,
            "name": "Large Medkit (211)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 212,
            "name": "Large Medkit (212)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 213,
            "name": "Rockets (213)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 214,
            "name": "Large Medkit (214)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 215,
            "name": "Large Medkit 215)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 219,
            "name": "Quad Damage (219)",
            "classname": "item_artifact_super_damage",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 220,
            "name": "Megahealth (220)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 221,
            "name": "Yellow Armor (221)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 224,
            "name": "Secret (224)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 225,
            "name": "Spikes (225)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 226,
            "name": "Large Medkit (226)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 227,
            "name": "Large Medkit (227)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 228,
            "name": "Large Medkit (228)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 229,
            "name": "Yellow Armor (229)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 230,
            "name": "Shells (230)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 232,
            "name": "Spikes (232)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 233,
            "name": "Spikes (233)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 235,
            "name": "Rockets (235)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 236,
            "name": "Large Medkit (236)",
            "classname": "item_health",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 237,
            "name": "Spikes (237)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 238,
            "name": "Small Medkit (238)",
            "classname": "item_health",
            "spawnflags": 3073.0,
            "density": 0,
        },
        {
            "id": 239,
            "name": "Small Medkit (239)",
            "classname": "item_health",
            "spawnflags": 3073.0,
            "density": 0,
        },
        {
            "id": 242,
            "name": "Rocketlauncher (242)",
            "classname": "weapon_rocketlauncher",
            "spawnflags": 2048.0,
            "density": 0,
        },
    ]
    events = ["Gold Bridge Moved"]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Rockets (105)",
                "Shells (106)",
                "Spikes (175)",
                "Large Medkit (58)",
                "Large Medkit (59)",
                "Large Medkit (208)",
            ],
        )

        past_gold_key_door_area = self.region(
            "Past Gold Key Door Area",
            [
                "Shells (230)",
            ],
        )
        self.connect(ret, past_gold_key_door_area, self.gold_key)

        gold_door_past_button_area = self.region(
            "Gold Key Door Area - Past Button",
            [
                "Spikes (225)",
                "Large Medkit (226)",
                "Large Medkit (227)",
                "Large Medkit (228)",
                "Yellow Armor (229)",
                "Exit",
            ],
        )
        self.connect(past_gold_key_door_area, gold_door_past_button_area, r.can_button)

        past_button_upper_area = self.region(
            "Past Button Upper Area",
            [
                "Spikes (210)",
                "Yellow Armor (221)",
                "Supernailgun (43)",
                "Megahealth (220)",
            ],
        )

        # can get to this without button ability through the gap above
        self.connect(ret, past_button_upper_area, r.bigjump | r.can_button)

        past_button_area = self.region(
            "Past Button Area",
            [
                "Large Medkit (56)",
                "Large Medkit (57)",
                "Rocketlauncher (242)",
                "Shells (209)",
                "Secret (174)",
                "Quad Damage (219)",
                "Rockets (235)",
                "Large Medkit (236)",
                "Megahealth (78)",
                "Secret (224)",
            ],
        )
        self.connect(ret, past_button_area, r.can_button)

        self.restrict("Secret (224)", r.can_door)
        self.restrict("Megahealth (78)", r.can_door)
        self.restrict("Secret (174)", r.can_shootswitch | r.bigjump)
        self.restrict("Quad Damage (219)", r.can_shootswitch | r.bigjump)

        past_staircase_area = self.region(
            "Past Staircase",
            [
                "Spikes (237)",
                "Small Medkit (238)",
                "Small Medkit (239)",
                "Silver Key (25)",
                "Shells (101)",
            ],
        )

        self.connect(
            past_button_area,
            past_staircase_area,
            r.can_door
            | r.bigjump
            | (r.can_jump & r.difficulty("hard"))
            | (r.can_gj_hard | r.can_rj_hard),
        )

        # you can go past the dark path by lighting it up with shotgun shots, quad damage etc. (or jump towards the top right)
        dark_path_area = self.region(
            "Dark Path Area",
            [
                "Large Medkit (117)",
                "Large Medkit (211)",
                "Large Medkit (212)",
                "Spikes (233)",
                "Rockets (213)",
            ],
        )
        self.connect(ret, dark_path_area, r.difficulty("medium") | r.can_button)

        self.restrict("Large Medkit (117)", r.can_door)

        gold_key_pickup_area = self.region(
            "Gold Key Pickup Area",
            [
                "Gold Key (10)",
            ],
        )

        self.connect(
            ret,
            gold_key_pickup_area,
            (r.difficulty("extreme") & r.can_jump)
            | r.can_rj_hard
            | r.can_gj_extr
            | (r.bigjump & r.difficulty("medium"))
            | self.event("Gold Bridge Moved"),
        )

        behind_silver_door_area = self.region(
            "Behind Silver Door Area",
            [
                "Gold Bridge Moved",
                "Large Medkit (214)",
                "Large Medkit 215)",
            ],
        )
        self.restrict("Gold Bridge Moved", r.can_button)
        self.connect(
            dark_path_area,
            behind_silver_door_area,
            self.silver_key
            & (
                ((r.can_rj | r.can_gj | r.can_jump) & r.difficulty("hard"))
                | r.can_button
            ),
        )
        gold_bridge_door_area = self.region(
            "Gold Bridge Door Area",
            [
                "Spikes (232)",
            ],
        )
        self.connect(
            dark_path_area, gold_bridge_door_area, self.event("Gold Bridge Moved")
        )

        stair_secret_area = self.region(
            "Stair Secret Area",
            [
                "Secret (141)",
                "Rockets (168)",
                "Secret (169)",
                "Megahealth (61)",
            ],
        )
        self.restrict(
            "Megahealth (61)",
            # slopejump + rj/gj off of the stairslope
            r.difficulty("extreme") & r.bigjump,
        )
        self.restrict("Secret (141)", r.can_shootswitch)
        self.restrict("Rockets (168)", r.can_shootswitch)
        self.restrict("Secret (169)", r.can_shootswitch)
        self.connect(dark_path_area, stair_secret_area, r.can_button)

        return ret
