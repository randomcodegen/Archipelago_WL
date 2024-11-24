from BaseClasses import Region

from ..base_classes import Q1Level


class E1M2(Q1Level):
    name = "Castle Of The Damned"
    levelnum = 1
    volumenum = 0
    keys = ["Silver"]
    location_defs = [
        {
            "id": 10,
            "name": "Large Medkit (10)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 11,
            "name": "Shells (11)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Small Medkit (15)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Small Medkit (16)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Shells (17)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Shells (20)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 21,
            "name": "Large Medkit (21)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Shells (26)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Small Medkit (27)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Small Medkit (28)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Large Medkit (30)",
            "classname": "item_health",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 34,
            "name": "Shells (34)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Small Medkit (35)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 36,
            "name": "Small Medkit (36)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Large Medkit (38)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Large Medkit (40)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Silver Key (42)",
            "classname": "item_key1",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Yellow Armor (46)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 100,
            "name": "Small Medkit (100)",
            "classname": "item_health",
            "spawnflags": 1025.0,
            "density": 0,
        },
        {
            "id": 101,
            "name": "Small Medkit (101)",
            "classname": "item_health",
            "spawnflags": 1025.0,
            "density": 0,
        },
        {
            "id": 102,
            "name": "Small Medkit (102)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 114,
            "name": "Large Medkit (114)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 115,
            "name": "Large Medkit (115)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 116,
            "name": "Shells (116)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 117,
            "name": "Shells (117)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 118,
            "name": "Large Medkit (118)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 119,
            "name": "Large Medkit (119)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 120,
            "name": "Small Medkit (120)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 121,
            "name": "Small Medkit (121)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 122,
            "name": "Large Medkit (122)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 123,
            "name": "Large Medkit (123)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 136,
            "name": "Shells (136)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 137,
            "name": "Supershotgun (137)",
            "classname": "weapon_supershotgun",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 138,
            "name": "Shells (138)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 142,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 147,
            "name": "Small Medkit (147)",
            "classname": "item_health",
            "spawnflags": 1025.0,
            "density": 0,
        },
        {
            "id": 157,
            "name": "Green Armor (157)",
            "classname": "item_armor1",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 165,
            "name": "Secret (165)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 166,
            "name": "Secret (166)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 168,
            "name": "Spikes (168)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Spikes (169)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 170,
            "name": "Spikes (170)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 181,
            "name": "Spikes (181)",
            "classname": "item_spikes",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 197,
            "name": "Secret (197)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 198,
            "name": "Quad Damage (198)",
            "classname": "item_artifact_super_damage",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 199,
            "name": "Spikes (199)",
            "classname": "item_spikes",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 200,
            "name": "Large Medkit (200)",
            "classname": "item_health",
            "spawnflags": 2048.0,
            "density": 0,
        },
    ]
    events = ["Bridge Moved", "Bridge Door Open"]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Shells (26)",
                "Small Medkit (120)",
                "Small Medkit (121)",
                "Spikes (168)",
                "Large Medkit (10)",
                "Small Medkit (15)",
                "Small Medkit (16)",
                "Large Medkit (38)",
                "Shells (11)",
                "Shells (17)",
                "Green Armor (157)",
                "Supershotgun (137)",
                "Shells (20)",
                "Large Medkit (21)",
                "Yellow Armor (46)",
                "Secret (166)",
                "Large Medkit (40)",
                "Spikes (169)",
                "Large Medkit (200)",
                "Spikes (199)",
                "Small Medkit (147)",
                "Small Medkit (27)",
                "Small Medkit (28)",
                "Spikes (170)",
                "Bridge Moved",
                "Bridge Door Open",
                "Silver Key (42)",
            ],
        )
        self.restrict("Spikes (168)", r.can_dive)
        self.restrict("Yellow Armor (46)", r.jump & r.can_shootswitch)

        self.restrict("Large Medkit (38)", r.jump | r.can_door)
        self.restrict("Green Armor (157)", r.jump | r.can_door)

        self.restrict("Secret (166)", r.can_door)
        self.restrict("Large Medkit (40)", r.can_door)
        self.restrict("Spikes (169)", r.can_door)

        self.restrict("Small Medkit (147)", r.can_door)
        self.restrict("Spikes (170)", r.can_door)

        self.restrict("Bridge Moved", r.can_door & r.can_button)
        self.restrict(
            "Bridge Door Open",
            self.event("Bridge Moved")
            | r.can_door
            | (r.difficulty("extreme") & r.can_gj),
        )

        self.restrict(
            "Silver Key (42)",
            self.event("Bridge Moved") | (r.difficulty("hard") & r.jump),
        )

        underwater_secret_area = self.region(
            "Underwater Secret Area",
            [
                "Secret (165)",
                "Shells (136)",
                "Large Medkit (122)",
                "Large Medkit (123)",
            ],
        )
        self.connect(
            ret,
            underwater_secret_area,
            r.can_dive,
        )

        silver_key_door_area = self.region(
            "Silver Key Door Area",
            [
                "Small Medkit (100)",
                "Small Medkit (101)",
                "Small Medkit (102)",
                "Shells (138)",
                "Large Medkit (30)",
                "Shells (116)",
            ],
        )
        self.connect(
            ret, silver_key_door_area, self.event("Bridge Door Open") | r.can_door
        )

        alcove_secret_area = self.region(
            "Alcove Secret Area",
            [
                "Secret (197)",
                "Quad Damage (198)",
            ],
        )
        self.connect(silver_key_door_area, alcove_secret_area, r.can_button)

        past_silver_door = self.region(
            "Past Silver Door Area",
            [
                "Shells (117)",
                "Large Medkit (118)",
                "Large Medkit (119)",
            ],
        )
        self.connect(silver_key_door_area, past_silver_door, self.silver_key)

        past_silver_door_upper = self.region(
            "Past Silver Door Upper Area",
            [
                "Large Medkit (114)",
                "Large Medkit (115)",
                "Spikes (181)",
            ],
        )
        self.connect(past_silver_door, past_silver_door_upper, r.bigjump | r.can_button)

        final_area = self.region(
            "Final Area",
            [
                "Small Medkit (35)",
                "Small Medkit (36)",
                "Shells (34)",
                "Exit",
            ],
        )
        self.connect(past_silver_door, final_area, r.can_button)

        return ret
