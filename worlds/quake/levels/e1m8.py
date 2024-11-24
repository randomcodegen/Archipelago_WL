from BaseClasses import Region

from ..base_classes import Q1Level


class E1M8(Q1Level):
    name = "Ziggurat Vertigo"
    levelnum = 7
    volumenum = 0
    keys = ["Silver"]
    location_defs = [
        {
            "id": 13,
            "name": "Rockets (13)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 14,
            "name": "Spikes (14)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 15,
            "name": "Rockets (15)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 16,
            "name": "Yellow Armor (16)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 17,
            "name": "Large Medkit (17)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 18,
            "name": "Large Medkit (18)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 19,
            "name": "Megahealth (19)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 20,
            "name": "Large Medkit (20)",
            "classname": "item_health",
            "spawnflags": 0.0,
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
            "id": 22,
            "name": "Large Medkit (22)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 23,
            "name": "Large Medkit (23)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 24,
            "name": "Spikes (24)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 25,
            "name": "Large Medkit (25)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Large Medkit (26)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Large Medkit (27)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 28,
            "name": "Spikes (28)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 29,
            "name": "Megahealth (29)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 30,
            "name": "Large Medkit (30)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Large Medkit (31)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 38,
            "name": "Shells (38)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 39,
            "name": "Shells (39)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 40,
            "name": "Shells (40)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 41,
            "name": "Shells (41)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 42,
            "name": "Shells (42)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 43,
            "name": "Spikes (43)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 44,
            "name": "Rockets (44)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 45,
            "name": "Rockets (45)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 46,
            "name": "Shells (46)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 70,
            "name": "Invulnerability (70)",
            "classname": "item_artifact_invulnerability",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 71,
            "name": "Invulnerability (71)",
            "classname": "item_artifact_invulnerability",
            "spawnflags": 256.0,
            "density": 0,
        },
        {
            "id": 83,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 91,
            "name": "Yellow Armor (91)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 92,
            "name": "Spikes (92)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 93,
            "name": "Spikes (93)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 94,
            "name": "Small Medkit (94)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 95,
            "name": "Small Medkit (95)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 96,
            "name": "Spikes (96)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 97,
            "name": "Spikes (97)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 98,
            "name": "Large Medkit (98)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 99,
            "name": "Large Medkit (99)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 100,
            "name": "Spikes (100)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 101,
            "name": "Large Medkit (101)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 102,
            "name": "Large Medkit (102)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 103,
            "name": "Shells (103)",
            "classname": "item_shells",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 104,
            "name": "Large Medkit (104)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 105,
            "name": "Large Medkit (105)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 106,
            "name": "Small Medkit (106)",
            "classname": "item_health",
            "spawnflags": 3073.0,
            "density": 0,
        },
        {
            "id": 107,
            "name": "Small Medkit (107)",
            "classname": "item_health",
            "spawnflags": 3073.0,
            "density": 0,
        },
        {
            "id": 108,
            "name": "Large Medkit (108)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 109,
            "name": "Large Medkit (109)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 110,
            "name": "Spikes (110)",
            "classname": "item_spikes",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 111,
            "name": "Spikes (111)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 113,
            "name": "Rocketlauncher (113)",
            "classname": "weapon_rocketlauncher",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 114,
            "name": "Spikes (114)",
            "classname": "item_spikes",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 117,
            "name": "Silver Key (117)",
            "classname": "item_key1",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 127,
            "name": "Spikes (127)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 128,
            "name": "Large Medkit (128)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 142,
            "name": "Spikes (142)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 150,
            "name": "Spikes (150)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 152,
            "name": "Secret (152)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 153,
            "name": "Spikes (153)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 154,
            "name": "Secret (154)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 155,
            "name": "Quad Damage (155)",
            "classname": "item_artifact_super_damage",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 156,
            "name": "Large Medkit (156)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 157,
            "name": "Large Medkit (157)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Small Medkit (169)",
            "classname": "item_health",
            "spawnflags": 2305.0,
            "density": 0,
        },
    ]
    must_invuln = True

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Invulnerability (70)",
                "Yellow Armor (91)",
                "Shells (40)",
                "Shells (41)",
                "Large Medkit (22)",
                "Large Medkit (23)",
                "Large Medkit (128)",
                "Spikes (14)",
                "Spikes (111)",
            ],
        )

        first_room_upper_plateau = self.region(
            "First Room Upper Plateau",
            [
                "Rockets (13)",
                "Small Medkit (94)",
                "Small Medkit (95)",
                "Shells (103)",
            ],
        )
        # can go up using the elevator
        self.connect(
            ret,
            first_room_upper_plateau,
            r.true,
        )

        first_room_upper_area = self.region(
            "First Room Upper Area",
            [
                "Rocketlauncher (113)",
                "Large Medkit (101)",
                "Large Medkit (102)",
                "Spikes (92)",
                "Spikes (93)",
            ],
        )
        self.connect(ret, first_room_upper_area)

        first_room_roof = self.region(
            "First Room Roof Area",
            [
                "Megahealth (19)",
                "Spikes (28)",
                "Rockets (45)",
                "Spikes (100)",
                "Small Medkit (169)",
            ],
        )
        self.connect(ret, first_room_roof, r.can_jump | r.can_gj | r.can_rj)

        lava_secret_area = self.region(
            "Lava Secret Area",
            [
                "Secret (154)",
                "Quad Damage (155)",
                "Large Medkit (156)",
                "Large Medkit (157)",
            ],
        )
        self.connect(ret, lava_secret_area, r.can_dive & r.invuln)

        second_room_area = self.region(
            "Second Room Area",
            [
                "Shells (38)",
                "Shells (39)",
                "Small Medkit (106)",
                "Small Medkit (107)",
                "Rockets (15)",
            ],
        )
        self.connect(first_room_roof, second_room_area, r.can_button)
        second_room_upper_area = self.region(
            "Second Room Upper Area",
            [
                "Large Medkit (20)",
                "Large Medkit (21)",
                "Spikes (142)",
                "Shells (42)",
                "Spikes (43)",
                "Rockets (44)",
                "Shells (46)",
                "Large Medkit (104)",
                "Large Medkit (105)",
                "Large Medkit (98)",
                "Large Medkit (99)",
                "Large Medkit (17)",
                "Large Medkit (18)",
                "Large Medkit (108)",
                "Large Medkit (109)",
                "Megahealth (29)",
                "Spikes (110)",
                "Spikes (150)",
                "Spikes (114)",
                "Spikes (96)",
                "Spikes (97)",
                "Invulnerability (71)",
                "Yellow Armor (16)",
            ],
        )
        self.connect(ret, second_room_upper_area, r.jump)

        second_room_upper_inside_area = self.region(
            "Second Room Upper Inside Area",
            [
                "Silver Key (117)",
                "Large Medkit (26)",
                "Large Medkit (27)",
                "Large Medkit (30)",
                "Large Medkit (31)",
                "Spikes (127)",
            ],
        )
        self.connect(second_room_upper_area, second_room_upper_inside_area)

        silver_key_area = self.region(
            "Silver Key Area",
            [
                "Secret (152)",
                "Spikes (24)",
                "Spikes (153)",
                "Large Medkit (25)",
                "Exit",
            ],
        )
        self.connect(second_room_upper_area, silver_key_area, self.silver_key)
        self.restrict("Secret (152)", r.can_shootswitch)
        self.restrict("Spikes (24)", r.can_shootswitch)
        self.restrict("Spikes (153)", r.can_shootswitch)

        return ret
