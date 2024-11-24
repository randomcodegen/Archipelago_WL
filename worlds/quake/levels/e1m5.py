from BaseClasses import Region

from ..base_classes import Q1Level


class E1M5(Q1Level):
    name = "Gloom Keep"
    levelnum = 4
    volumenum = 0
    keys = ["Silver", "Gold"]
    location_defs = [
        {
            "id": 58,
            "name": "Gold Key (58)",
            "classname": "item_key2",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 106,
            "name": "Yellow Armor (106)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 112,
            "name": "Large Medkit (112)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 113,
            "name": "Large Medkit (113)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 114,
            "name": "Shells (114)",
            "classname": "item_shells",
            "spawnflags": 1024.0,
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
            "id": 138,
            "name": "Small Medkit (138)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 139,
            "name": "Small Medkit (139)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 140,
            "name": "Small Medkit (140)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 146,
            "name": "Large Medkit (146)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 147,
            "name": "Large Medkit (147)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 148,
            "name": "Large Medkit (148)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 149,
            "name": "Large Medkit (149)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 150,
            "name": "Small Medkit (150)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 151,
            "name": "Shells (151)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 152,
            "name": "Shells (152)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 153,
            "name": "Large Medkit (153)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 154,
            "name": "Large Medkit (154)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 155,
            "name": "Shells (155)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 156,
            "name": "Small Medkit (156)",
            "classname": "item_health",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 157,
            "name": "Spikes (157)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 158,
            "name": "Rockets (158)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 159,
            "name": "Large Medkit (159)",
            "classname": "item_health",
            "spawnflags": 2304.0,
            "density": 0,
        },
        {
            "id": 160,
            "name": "Large Medkit (160)",
            "classname": "item_health",
            "spawnflags": 2304.0,
            "density": 0,
        },
        {
            "id": 161,
            "name": "Shells (161)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 162,
            "name": "Shells (162)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 163,
            "name": "Large Medkit (163)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 164,
            "name": "Large Medkit (164)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 165,
            "name": "Small Medkit (165)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 166,
            "name": "Small Medkit (166)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 167,
            "name": "Large Medkit (167)",
            "classname": "item_health",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 168,
            "name": "Shells (168)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Shells (169)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 170,
            "name": "Rockets (170)",
            "classname": "item_rockets",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 171,
            "name": "Small Medkit (171)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 193,
            "name": "Small Medkit (193)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 195,
            "name": "Supernailgun (195)",
            "classname": "weapon_supernailgun",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 196,
            "name": "Silver Key (196)",
            "classname": "item_key1",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 197,
            "name": "Spikes (197)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 198,
            "name": "Large Medkit (198)",
            "classname": "item_health",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 199,
            "name": "Large Medkit (199)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 200,
            "name": "Spikes (200)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 201,
            "name": "Rocketlauncher (201)",
            "classname": "weapon_rocketlauncher",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 207,
            "name": "Secret (207)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 208,
            "name": "Secret (208)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 215,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 216,
            "name": "Large Medkit (216)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 217,
            "name": "Large Medkit (217)",
            "classname": "item_health",
            "spawnflags": 0.0,
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
            "id": 226,
            "name": "Shells (226)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 230,
            "name": "Spikes (230)",
            "classname": "item_spikes",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 232,
            "name": "Secret (232)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 233,
            "name": "Megahealth (233)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 234,
            "name": "Shells (234)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 235,
            "name": "Rockets (235)",
            "classname": "item_rockets",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 236,
            "name": "Spikes (236)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 237,
            "name": "Spikes (237)",
            "classname": "item_spikes",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 238,
            "name": "Spikes (238)",
            "classname": "item_spikes",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 239,
            "name": "Green Armor (239)",
            "classname": "item_armor1",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 240,
            "name": "Quad Damage (240)",
            "classname": "item_artifact_super_damage",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 242,
            "name": "Yellow Armor (242)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 247,
            "name": "Secret (247)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 248,
            "name": "Small Medkit (248)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 249,
            "name": "Shells (249)",
            "classname": "item_shells",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 250,
            "name": "Rockets (250)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 251,
            "name": "Large Medkit (251)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 252,
            "name": "Small Medkit (252)",
            "classname": "item_health",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 256,
            "name": "Secret (256)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Shells (169)",
                "Large Medkit (216)",
                "Large Medkit (217)",
            ],
        )

        underwater_cave_area = self.region(
            "Underwater Cave Secret Area",
            [
                "Secret (232)",
                "Spikes (236)",
                "Megahealth (233)",
            ],
        )
        self.connect(ret, underwater_cave_area, r.can_dive)

        inside_1f_area = self.region(
            "Inside 1F Area",
            [
                "Large Medkit (251)",
                "Shells (162)",
                "Rocketlauncher (201)",
                "Rockets (250)",
                "Small Medkit (252)",
                "Small Medkit (156)",
                "Shells (155)",
                "Shells (151)",
                "Large Medkit (163)",
                "Large Medkit (164)",
                "Large Medkit (146)",
                "Large Medkit (147)",
                "Small Medkit (150)",
                "Spikes (197)",
                "Shells (152)",
            ],
        )
        self.connect(ret, inside_1f_area)

        inside_basement_area = self.region(
            "Inside Basement Area",
            [
                "Small Medkit (165)",
                "Small Medkit (166)",
                "Shells (249)",
                "Spikes (157)",
                "Large Medkit (153)",
                "Large Medkit (154)",
                "Rockets (170)",
                "Shells (234)",
                "Large Medkit (148)",
                "Large Medkit (149)",
            ],
        )
        self.connect(ret, inside_basement_area)
        tower_secret_area = self.region(
            "Tower Secret  Area",
            [
                "Secret (256)",
                "Yellow Armor (106)",
                "Shells (226)",
            ],
        )
        self.connect(
            inside_basement_area, tower_secret_area, r.can_jump | r.can_gj | r.can_rj
        )

        inside_2f_area = self.region(
            "Inside 2F Area",
            [
                "Spikes (219)",
                "Supernailgun (195)",
                "Small Medkit (138)",
                "Small Medkit (139)",
                "Small Medkit (140)",
                "Large Medkit (198)",
                "Large Medkit (199)",
                "Spikes (200)",
                "Yellow Armor (242)",
                "Secret (208)",
            ],
        )
        self.connect(ret, inside_2f_area)
        self.restrict(
            "Yellow Armor (242)",
            (r.can_jump | r.can_gj | r.can_rj) & r.can_button,
        )
        self.restrict(
            "Secret (208)",
            (r.can_jump | r.can_gj | r.can_rj) & r.can_button,
        )

        inside_3f_area = self.region(
            "Inside 3F Area",
            [
                "Rockets (235)",
                "Secret (207)",
                "Quad Damage (240)",
            ],
        )
        self.connect(ret, inside_3f_area)

        past_button_area = self.region(
            "Past Button Area",
            [
                "Gold Key (58)",
                "Shells (114)",
                "Large Medkit (112)",
                "Large Medkit (113)",
                "Small Medkit (115)",
                "Large Medkit (159)",
                "Large Medkit (160)",
                "Small Medkit (171)",
                "Spikes (230)",
                "Spikes (237)",
                "Spikes (238)",
                "Shells (161)",
                "Silver Key (196)",
                "Small Medkit (248)",
            ],
        )
        self.connect(ret, past_button_area, r.can_button)

        past_elevator_area = self.region(
            "Past Elevator Area",
            [
                "Large Medkit (167)",
                "Shells (168)",
            ],
        )
        self.connect(
            ret,
            past_elevator_area,
            # maybe medium difficulty jump? slightly obscure
            self.silver_key | (r.bigjump & r.difficulty("hard")),
        )

        past_gold_key_door_area = self.region(
            "Past Gold Key Door Area",
            [
                "Green Armor (239)",
                "Secret (247)",
                "Small Medkit (193)",
                "Exit",
            ],
        )
        self.connect(past_elevator_area, past_gold_key_door_area, self.gold_key)

        return ret
