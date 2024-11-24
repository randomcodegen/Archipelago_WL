from BaseClasses import Region

from ..base_classes import Q1Level


class E1M7(Q1Level):
    name = "The House of Chthon"
    levelnum = 6
    volumenum = 0
    keys = []
    location_defs = [
        {
            "id": 20,
            "name": "Sigil (20)",
            "classname": "item_sigil",
            "spawnflags": 2049.0,
            "density": 0,
        },
        {
            "id": 26,
            "name": "Megahealth (26)",
            "classname": "item_health",
            "spawnflags": 1026.0,
            "density": 0,
        },
        {
            "id": 27,
            "name": "Exit",
            "classname": "trigger_changelevel",
            "spawnflags": 0.0,
        },
    ]
    has_boss = True

    def main_region(self) -> Region:
        r = self.rules

        ret = self.region(
            self.name,
            [
                "Sigil (20)",
                "Megahealth (26)",
                "Exit",
            ],
        )
        self.restrict("Exit", r.can_button)
        return ret
