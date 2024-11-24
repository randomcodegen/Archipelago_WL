from ..base_classes import Q1Episode
from .e1m1 import E1M1
from .e1m2 import E1M2
from .e1m3 import E1M3
from .e1m4 import E1M4
from .e1m5 import E1M5
from .e1m6 import E1M6
from .e1m7 import E1M7
from .e1m8 import E1M8


class E1(Q1Episode):
    name = "Doomed Dimension"
    volumenum = 0
    levels = [E1M1(), E1M2(), E1M3(), E1M4(), E1M5(), E1M6(), E1M7(), E1M8()]
    maxlevel = 8


"""
class E2(Q1Episode):
    name = "Realm of Black Magic"
    volumenum = 1
    levels = [E2M1(), E2M2(), E2M3(), E2M4(), E2M5(), E2M6(), E2M7()]
    maxlevel = 7

class E3(Q1Episode):
    name = "Netherworld"
    volumenum = 2
    levels = [E3M1(), E3M2(), E3M3(), E3M4(), E3M5(), E3M6(), E3M7()]
    maxlevel = 7

class E4(Q1Episode):
    name = "The Elder World"
    volumenum = 3
    levels = [E4M1(), E4M2(), E4M3(), E4M4(), E4M5(), E4M6(), E4M7(), E4M8()]
    maxlevel = 8
"""

# all_episodes = [E1(),E2()]
all_episodes = [E1()]
all_levels = [level for ep in all_episodes for level in ep.levels]
