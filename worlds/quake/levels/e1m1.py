from BaseClasses import Region

from ..base_classes import Q1Level


class E1M1(Q1Level):
    name = "The Slipgate Complex"
    levelnum = 0
    volumenum = 0
    keys = []
    location_defs = [
        {
            "id": 11,
            "name": "Green Armor (11)",
            "classname": "item_armor1",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 31,
            "name": "Nailgun (31)",
            "classname": "weapon_nailgun",
            "spawnflags": 2048.0,
            "density": 0,
        },
        {
            "id": 35,
            "name": "Spikes (35)",
            "classname": "item_spikes",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 47,
            "name": "Quad Damage (47)",
            "classname": "item_artifact_super_damage",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 55,
            "name": "Megahealth (55)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 57,
            "name": "Shells (57)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 58,
            "name": "Small Medkit (58)",
            "classname": "item_health",
            "spawnflags": 1.0,
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
            "id": 60,
            "name": "Large Medkit (60)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 75,
            "name": "Spikes (75)",
            "classname": "item_spikes",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 76,
            "name": "Large Medkit (76)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 77,
            "name": "Small Medkit (77)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 78,
            "name": "Small Medkit (78)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 85,
            "name": "Large Medkit (85)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 86,
            "name": "Large Medkit (86)",
            "classname": "item_health",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 87,
            "name": "Small Medkit (87)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 91,
            "name": "Biosuit (91)",
            "classname": "item_artifact_envirosuit",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 92,
            "name": "Megahealth (92)",
            "classname": "item_health",
            "spawnflags": 2.0,
            "density": 0,
        },
        {
            "id": 106,
            "name": "Supershotgun (106)",
            "classname": "weapon_supershotgun",
            "spawnflags": 0.0,
            "density": 2,
        },
        {
            "id": 108,
            "name": "Shells (108)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 131,
            "name": "Small Medkit (131)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 133,
            "name": "Shells (133)",
            "classname": "item_shells",
            "spawnflags": 0.0,
            "density": 0,
        },
        {
            "id": 134,
            "name": "Secret (134)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 135,
            "name": "Secret (135)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 136,
            "name": "Secret (136)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 137,
            "name": "Secret (137)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 138,
            "name": "Secret (138)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 139,
            "name": "Secret (139)",
            "classname": "trigger_secret",
            "spawnflags": 0.0,
        },
        {
            "id": 140,
            "name": "Small Medkit (140)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 144,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
        {
            "id": 145,
            "name": "Small Medkit (145)",
            "classname": "item_health",
            "spawnflags": 1.0,
            "density": 0,
        },
        {
            "id": 149,
            "name": "Yellow Armor (149)",
            "classname": "item_armor2",
            "spawnflags": 0.0,
            "density": 0,
        },
    ]
    must_bio = True
    must_invuln = True

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(self.name)

        secret_ledge = self.region(
            "Ledge Secret Area",
            [
                "Shells (133)",
                "Secret (134)",
            ],
        )
        self.connect(ret, secret_ledge, r.jump & r.can_shootswitch)

        start_ledge = self.region(
            "Start Ledge Area",
            [
                "Shells (108)",
                "Green Armor (11)",
            ],
        )
        self.connect(ret, start_ledge, r.jump)

        # Requires door + button to go down the elevator
        past_door = self.region(
            "Past Start Door",
            [
                "Large Medkit (85)",
                "Large Medkit (86)",
                "Small Medkit (131)",
                "Secret (135)",
                "Megahealth (55)",
                "Shells (57)",
                "Pillar Health (13)",
                "Nailgun (31)",
                "Spikes (35)",
                "Small Medkit (87)",
                "Secret (139)",
                "Supershotgun (106)",
                "Secret (138)",
                "Quad Damage (47)",
                "Small Medkit (140)",
                "Small Medkit (145)",
                "Biosuit (91)",
                "Large Medkit (76)",
                "Small Medkit (77)",
                "Small Medkit (78)",
                "Spikes (75)",
                "Exit",
            ],
        )
        self.connect(ret, past_door, r.can_button & r.can_door)

        self.restrict("Supershotgun (106)", r.can_shootswitch)
        self.restrict("Secret (139)", r.can_shootswitch)

        self.restrict("Secret (138)", r.can_shootswitch)
        self.restrict("Quad Damage (47)", r.can_shootswitch)

        upper_spiral = self.region(
            "Upper Spiral Area",
            [
                "Secret (137)",
                "Megahealth (92)",
            ],
        )
        # very difficult in-place grenade jump when standing on top of the light/switch
        self.connect(
            past_door,
            upper_spiral,
            r.can_jump | r.can_rj | r.can_gj_extr,
        )

        spiral_dive = self.region(
            "Spiral Dive Area",
            [
                "Secret (136)",
                "Small Medkit (58)",
                "Large Medkit (59)",
                "Large Medkit (60)",
                "Yellow Armor (149)",
            ],
        )
        # Can dive through with 100 health
        self.connect(
            past_door,
            spiral_dive,
            r.jump
            & r.can_dive
            & ((r.difficulty("hard") | r.biosuit(1) | r.invuln(1) | r.heal(75))),
        )

        return ret
