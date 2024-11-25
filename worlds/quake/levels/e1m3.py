from BaseClasses import Region

from ..base_classes import Q1Level


class E1M3(Q1Level):
    name = "The Necropolis"
    levelnum = 2
    volumenum = 0
    keys = ["Gold"]
    location_defs = [
        {
            "id": 76,
            "name": "Gold Key (76)",
            "classname": "item_key2",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 136,
            "name": "Nailgun (136)",
            "classname": "weapon_nailgun",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 142,
            "name": "Shells (142)",
            "classname": "item_shells",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 143,
            "name": "Large Medkit (143)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 144,
            "name": "Small Medkit (144)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 145,
            "name": "Supershotgun (143)",
            "classname": "weapon_supershotgun",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 146,
            "name": "Shells (146)",
            "classname": "item_shells",
            "spawnflags": 1024.0,
            "density": 0,
        },
        {
            "id": 147,
            "name": "Rockets (147)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 148,
            "name": "Spikes (148)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 149,
            "name": "Green Armor (149)",
            "classname": "item_armor1",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 150,
            "name": "Large Medkit (150)",
            "classname": "item_health",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 151,
            "name": "Spikes (151)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 152,
            "name": "Small Medkit (152)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 153,
            "name": "Small Medkit (153)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 154,
            "name": "Rockets (154)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 155,
            "name": "Large Medkit (155)",
            "classname": "item_health",
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
            "name": "Spikes (157)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 158,
            "name": "Shells (158)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 159,
            "name": "Rockets (159)",
            "classname": "item_rockets",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 160,
            "name": "Large Medkit (160)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 161,
            "name": "Small Medkit (161)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 162,
            "name": "Small Medkit (162)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 164,
            "name": "Shells (164)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 165,
            "name": "Spikes (165)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 166,
            "name": "Spikes (166)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 167,
            "name": "Shells (167)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 168,
            "name": "Spikes (168)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 169,
            "name": "Small Medkit (169)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 170,
            "name": "Small Medkit (170)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 171,
            "name": "Large Medkit (171)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 172,
            "name": "Rockets (172)",
            "classname": "item_rockets",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 173,
            "name": "Shells (173)",
            "classname": "item_shells",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 174,
            "name": "Shells (174)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 175,
            "name": "Spikes (175)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 176,
            "name": "Rockets (176)",
            "classname": "item_rockets",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 179,
            "name": "Small Medkit (179)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 184,
            "name": "Large Medkit (184)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 185,
            "name": "Small Medkit (185)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 186,
            "name": "Shells (186)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 187,
            "name": "Large Medkit (187)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 193,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 194,
            "name": "Large Medkit (194)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 196,
            "name": "Small Medkit (196)",
            "classname": "item_health",
            "spawnflags": 1281.0,
            "density": 0,
        },
        {
            "id": 197,
            "name": "Small Medkit (197)",
            "classname": "item_health",
            "spawnflags": 1281.0,
            "density": 0,
        },
        {
            "id": 198,
            "name": "Shells (198)",
            "classname": "item_shells",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 220,
            "name": "Secret (220)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 221,
            "name": "Rockets (221)",
            "classname": "item_rockets",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 222,
            "name": "Yellow Armor (222)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 223,
            "name": "Grenadelauncher (223)",
            "classname": "weapon_grenadelauncher",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 229,
            "name": "Large Medkit (229)",
            "classname": "item_health",
            "spawnflags": 3072.0,
            "density": 0,
        },
        {
            "id": 247,
            "name": "Large Medkit (247)",
            "classname": "item_health",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 252,
            "name": "Secret (252)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 253,
            "name": "Invisibility (253)",
            "classname": "item_artifact_invisibility",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 255,
            "name": "Secret (255)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 256,
            "name": "Large Medkit (256)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 257,
            "name": "Rockets (257)",
            "classname": "item_rockets",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 261,
            "name": "Large Medkit (261)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
    ]

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Shells (146)",
                "Large Medkit (143)",
                "Small Medkit (144)",
                "Grenadelauncher (223)",
                "Rockets (147)",
                "Large Medkit (150)",
                "Large Medkit (261)",
                "Supershotgun (143)",
                "Shells (164)",
                "Spikes (151)",
                "Small Medkit (179)",
                "Secret (255)",
                "Green Armor (149)",
                "Small Medkit (152)",
                "Small Medkit (153)",
                "Shells (167)",
                "Rockets (154)",
                "Large Medkit (155)",
                "Large Medkit (156)",
                "Gold Key (76)",
                "Large Medkit (256)",
                "Rockets (257)",
            ],
        )
        self.restrict("Secret (255)", r.can_shootswitch)
        self.restrict("Large Medkit (256)", r.can_shootswitch)
        self.restrict("Rockets (257)", r.can_shootswitch)
        self.restrict("Large Medkit (261)", r.can_door)

        underwater_secret = self.region(
            "Underwater Secret",
            [
                "Invisibility (253)",
                "Secret (252)",
            ],
        )
        self.connect(ret, underwater_secret, r.can_dive)

        dd_area = self.region(
            "Past Double Door",
            [
                "Spikes (148)",
                "Spikes (175)",
                "Spikes (165)",
                "Spikes (166)",
                "Small Medkit (196)",
                "Small Medkit (197)",
                "Large Medkit (187)",
                "Rockets (176)",
                "Shells (173)",
            ],
        )

        dd_ele_area = self.region(
            "Double Door Elevator",
            # This one always requires access through the double door from the top
            [
                "Nailgun (136)",
            ],
        )
        self.connect(ret, dd_ele_area, r.can_door)

        # rj/gj upwards from the golden key "island"
        self.connect(
            ret,
            dd_area,
            (r.can_door & r.can_shootswitch)
            | (r.can_rj_hard & r.can_jump)
            | (r.can_gj_extr & r.can_jump),
        )

        past_gold_door_area = self.region(
            "Past Gold Door",
            [
                "Spikes (168)",
                "Large Medkit (194)",
                "Large Medkit (229)",
                "Shells (198)",
                "Small Medkit (169)",
                "Small Medkit (170)",
                "Large Medkit (171)",
                "Rockets (172)",
                "Shells (174)",
                "Small Medkit (161)",
                "Small Medkit (162)",
                "Rockets (159)",
                "Large Medkit (184)",
                "Small Medkit (185)",
                "Shells (142)",
                "Yellow Armor (222)",
                "Secret (220)",
                "Rockets (221)",
            ],
        )
        self.connect(dd_area, past_gold_door_area, self.gold_key)
        # very difficult in-place grenade jumps to get on top
        self.restrict(
            "Rockets (159)",
            r.can_jump | r.can_rj_hard | r.can_gj_extr,
        )

        self.restrict(
            "Secret (220)",
            (r.can_shootswitch & r.jump)
            | (r.can_jump & (r.can_rj_hard | r.can_gj_extr)),
        )
        self.restrict(
            "Rockets (221)",
            (r.can_shootswitch & r.jump)
            | (r.can_jump & (r.can_rj_hard | r.can_gj_extr)),
        )

        past_sewer_button_area = self.region(
            "Past Sewer Button",
            [
                "Spikes (157)",
                "Shells (158)",
                "Large Medkit (160)",
            ],
        )
        self.connect(
            past_gold_door_area,
            past_sewer_button_area,
            # very difficult in-place grenade jumps to get on top
            r.can_button & (r.can_jump | r.can_rj_hard | r.can_gj_extr),
        )

        past_elevator_area = self.region(
            "Past Elevator",
            [
                "Large Medkit (247)",
                "Shells (186)",
                "Exit",
            ],
        )

        self.connect(
            past_gold_door_area,
            past_elevator_area,
            r.can_button,
        )

        return ret
