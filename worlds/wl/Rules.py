import math

from BaseClasses import MultiWorld
from .Names import LocationName, ItemName
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import add_rule, set_rule

def set_rules(world: MultiWorld, player: int):
    if world.goal[player] == "garlic_hunt":
        required_garlic_cloves = max(math.floor(
                world.number_of_garlic_cloves[player].value * (world.percentage_of_garlic_cloves[player].value / 100.0)), 1)
        add_rule(world.get_location(LocationName.garlic_goal, player),
                 lambda state: state.has(ItemName.garlic_clove, player, required_garlic_cloves))
    world.completion_condition[player] = lambda state: state.has(ItemName.victory, player)