import typing

from BaseClasses import Location
from .Names import LocationName


class WLLocation(Location):
    game: str = "Wario Land"

    def __init__(self, player: int, name: str = '', address: int = None, parent=None, prog_byte: int = None, prog_mask: int = None):
        super().__init__(player, name, address, parent)
        self.progress_byte = prog_byte
        self.progress_mask  = prog_mask




level_location_table = {
    LocationName.ricebeach_1_exit_1:    0xA80B01,
    LocationName.ricebeach_2_exit_1:    0xA80B02,
    LocationName.ricebeach_3_exit_1:    0xA80B04,
    LocationName.ricebeach_3_exit_2:    0xA80B08,
    LocationName.ricebeach_4_exit_1:    0xA80B10,
    LocationName.ricebeach_6_exit_1:    0xA80B40,
    LocationName.ricebeach_boss:        0xA80B20,

    LocationName.mtteapot_7_exit_1:     0xA80C01,
    LocationName.mtteapot_8_exit_1:     0xA80C02,
    LocationName.mtteapot_8_exit_2:     0xA80C04,
    LocationName.mtteapot_9_exit_1:     0xA80C08,
    LocationName.mtteapot_10_exit_1:    0xA80C10,
    LocationName.mtteapot_11_exit_1:    0xA80C20,
    LocationName.mtteapot_12_exit_1:    0xA80C40,
    LocationName.mtteapot_boss:         0xA80C80,

    LocationName.sherbetland_14_exit_1: 0xA81301,
    LocationName.sherbetland_15_exit_1: 0xA81302,
    LocationName.sherbetland_15_exit_2: 0xA81304,
    LocationName.sherbetland_16_exit_1: 0xA81308,
    LocationName.sherbetland_16_exit_2: 0xA81310,
    LocationName.sherbetland_17_exit_1: 0xA81320,
    LocationName.sherbetland_18_exit_1: 0xA81340,
    LocationName.sherbetland_boss:      0xA81380,

    LocationName.stovecanyon_20_exit_1: 0xA81001,
    LocationName.stovecanyon_21_exit_1: 0xA81002,
    LocationName.stovecanyon_22_exit_1: 0xA81004,
    LocationName.stovecanyon_23_exit_1: 0xA81008,
    LocationName.stovecanyon_23_exit_2: 0xA81010,
    LocationName.stovecanyon_24_exit_1: 0xA81020,
    LocationName.stovecanyon_boss:      0xA81040,

    LocationName.ssteacup_26_exit_1:    0xA81101,
    LocationName.ssteacup_27_exit_1:    0xA81102,
    LocationName.ssteacup_28_exit_1:    0xA81104,
    LocationName.ssteacup_29_exit_1:    0xA81108,
    LocationName.ssteacup_boss:         0xA81110,

    LocationName.parsleywoods_31_exit_1:    0xA81201,
    LocationName.parsleywoods_32_exit_1:    0xA81202,
    LocationName.parsleywoods_33_exit_1:    0xA81204,
    LocationName.parsleywoods_34_exit_1:    0xA81208,
    LocationName.parsleywoods_35_exit_1:    0xA81210,
    LocationName.parsleywoods_boss:         0xA81220,

    LocationName.syrupcastle_37_exit_1:     0xA81401,
    LocationName.syrupcastle_38_exit_1:     0xA81402,
    LocationName.syrupcastle_39_exit_1:     0xA81404,
    LocationName.syrupcastle_boss:          0xA81408,
}

treasure_location_table = {
    LocationName.ricebeach_3_treasure:      0xA80E20,
    LocationName.mtteapot_9_treasure:       0xA80F08,
    LocationName.mtteapot_11_treasure:      0xA80E02,
    LocationName.stovecanyon_20_treasure:   0xA80F20,
    LocationName.stovecanyon_24_treasure:   0xA80E80,
    LocationName.sherbetland_16_treasure:   0xA80F10,
    LocationName.sherbetland_17_treasure:   0xA80F80,
    LocationName.sherbetland_18_treasure:   0xA80E08,
    LocationName.ssteacup_26_treasure:      0xA80E04,
    LocationName.ssteacup_29_treasure:      0xA80F40,
    LocationName.ssteacup_30_treasure:      0xA80F04,
    LocationName.parsleywoods_31_treasure:  0xA80F02,
    LocationName.parsleywoods_34_treasure:  0xA80F01,
    LocationName.syrupcastle_37_treasure:   0xA80E40,
    LocationName.syrupcastle_39_treasure:   0xA80E10,
}

genie_location_table = {
    LocationName.genie: 0xA81700,
}

garlic_location_table = {
    LocationName.garlic_goal: 0xA41300,
}

all_locations = {
    **level_location_table,
    **treasure_location_table,
    #**genie_location_table,
    **garlic_location_table,
}

checkable_locations = {
    **level_location_table,
    **treasure_location_table,
}

location_table = {}


def setup_locations(world, player: int):
    location_table = {**level_location_table}

    if world.treasure_checks[player].value:
        location_table.update({**treasure_location_table})
    if world.goal[player] == "garlic_hunt":
        location_table.update({**garlic_location_table})
    #else:
    #    location_table.update({**genie_location_table})    
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}
