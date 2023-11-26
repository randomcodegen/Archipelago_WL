import typing

from BaseClasses import Location
from .Names import LocationName


class WLLocation(Location):
    game: str = "Wario Land"

    def __init__(self, player: int, name: str = '', address: int = None, parent=None):
        super().__init__(player, name, address, parent)

boss_item_location_table = {
    LocationName.ricebeach_boss_item:   0xA80B2B,
    LocationName.mtteapot_boss_item:    0xA80C8B,
    LocationName.sherbetland_boss_item: 0xA8138B,
    LocationName.ssteacup_boss_item:    0xA8111B,
    LocationName.stovecanyon_boss_item: 0xA8104B,
    LocationName.parsleywoods_boss_item:0xA8122B,
    LocationName.syrupcastle_boss_item: 0xA8140B,
}


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

block_location_table = {
    LocationName.ricebeach_1_block1:  0xA82000, 
    LocationName.ricebeach_1_block2:  0xA82001, 
    LocationName.ricebeach_1_block3:  0xA82002, 
    LocationName.ricebeach_1_block4:  0xA82003, 
    LocationName.ricebeach_1_block5:  0xA82004, 
    LocationName.ricebeach_1_block6:  0xA82005, 
    LocationName.ricebeach_1_block7:  0xA82006, 
    LocationName.ricebeach_1_block8:  0xA82007, 
    LocationName.ricebeach_1_block9:  0xA82008, 
    LocationName.ricebeach_1_block10: 0xA82009,
    LocationName.ricebeach_1_block11: 0xA82010,
    LocationName.ricebeach_1_block12: 0xA82011,
    LocationName.ricebeach_1_block13: 0xA82012,
    LocationName.ricebeach_1_block14: 0xA82013,
    LocationName.ricebeach_1_block15: 0xA82014,
    LocationName.ricebeach_1_block16: 0xA82015,
    LocationName.ricebeach_1_block17: 0xA82016,
    LocationName.ricebeach_1_block18: 0xA82017,

    LocationName.ricebeach_2_block1:  0xA82018, 
    LocationName.ricebeach_2_block2:  0xA82019, 
    LocationName.ricebeach_2_block3:  0xA82020, 
    LocationName.ricebeach_2_block4:  0xA82021, 
    LocationName.ricebeach_2_block5:  0xA82022, 
    LocationName.ricebeach_2_block6:  0xA82023, 
    LocationName.ricebeach_2_block7:  0xA82024, 
    LocationName.ricebeach_2_block8:  0xA82025, 
    LocationName.ricebeach_2_block9:  0xA82026, 
    LocationName.ricebeach_2_block10: 0xA82027,
    LocationName.ricebeach_2_block11: 0xA82028,
    LocationName.ricebeach_2_block12: 0xA82029,
    LocationName.ricebeach_2_block13: 0xA82030,
    LocationName.ricebeach_2_block14: 0xA82031,
    LocationName.ricebeach_2_block15: 0xA82032,
    LocationName.ricebeach_2_block16: 0xA82033,
    LocationName.ricebeach_2_block17: 0xA82034,
    LocationName.ricebeach_2_block18: 0xA82035,
    LocationName.ricebeach_2_block19: 0xA82036,
    LocationName.ricebeach_2_block20: 0xA82037,

    LocationName.ricebeach_3_block1:  0xA82038, 
    LocationName.ricebeach_3_block2:  0xA82039, 
    LocationName.ricebeach_3_block3:  0xA82040, 
    LocationName.ricebeach_3_block4:  0xA82041, 
    LocationName.ricebeach_3_block5:  0xA82042, 
    LocationName.ricebeach_3_block6:  0xA82043, 
    LocationName.ricebeach_3_block7:  0xA82044, 
    LocationName.ricebeach_3_block8:  0xA82045, 
    LocationName.ricebeach_3_block9:  0xA82046, 
    LocationName.ricebeach_3_block10: 0xA82047,
    LocationName.ricebeach_3_block11: 0xA82048,
    LocationName.ricebeach_3_block12: 0xA82049,
    LocationName.ricebeach_3_block13: 0xA82050,
    LocationName.ricebeach_3_block14: 0xA82051,
    LocationName.ricebeach_3_block15: 0xA82052,

    LocationName.ricebeach_4_block1: 0xA82053, 
    LocationName.ricebeach_4_block2: 0xA82054, 
    LocationName.ricebeach_4_block3: 0xA82055, 
    LocationName.ricebeach_4_block4: 0xA82056, 
    LocationName.ricebeach_4_block5: 0xA82057, 
    LocationName.ricebeach_4_block6: 0xA82058, 

    LocationName.ricebeach_5_block1: 0xA82059, 
    LocationName.ricebeach_5_block2: 0xA82060, 
    LocationName.ricebeach_5_block3: 0xA82061, 
    LocationName.ricebeach_5_block4: 0xA82062, 
    LocationName.ricebeach_5_block5: 0xA82063, 
    LocationName.ricebeach_5_block6: 0xA82064, 

    LocationName.ricebeach_6_block1: 0xA82065, 
    LocationName.ricebeach_6_block2: 0xA82066, 
    LocationName.ricebeach_6_block3: 0xA82067, 
    LocationName.ricebeach_6_block4: 0xA82068, 
    LocationName.ricebeach_6_block5: 0xA82069, 
    LocationName.ricebeach_6_block6: 0xA82070, 
    LocationName.ricebeach_6_block7: 0xA82071, 
    LocationName.ricebeach_6_block8: 0xA82072, 

    LocationName.mtteapot_7_block1:  0xA82073, 
    LocationName.mtteapot_7_block2:  0xA82074, 
    LocationName.mtteapot_7_block3:  0xA82075, 
    LocationName.mtteapot_7_block4:  0xA82076, 
    LocationName.mtteapot_7_block5:  0xA82077, 
    LocationName.mtteapot_7_block6:  0xA82078, 
    LocationName.mtteapot_7_block7:  0xA82079, 
    LocationName.mtteapot_7_block8:  0xA82080, 
    LocationName.mtteapot_7_block9:  0xA82081, 
    LocationName.mtteapot_7_block10: 0xA82082, 
    LocationName.mtteapot_7_block11: 0xA82083, 
    LocationName.mtteapot_7_block12: 0xA82084, 
    LocationName.mtteapot_7_block13: 0xA82085, 
    LocationName.mtteapot_7_block14: 0xA82086, 
    LocationName.mtteapot_7_block15: 0xA82087, 
    LocationName.mtteapot_7_block16: 0xA82088, 
    LocationName.mtteapot_7_block17: 0xA82089, 
    LocationName.mtteapot_7_block18: 0xA82090, 
    LocationName.mtteapot_7_block19: 0xA82091, 
    LocationName.mtteapot_7_block20: 0xA82092, 
    LocationName.mtteapot_7_block21: 0xA82093, 
    LocationName.mtteapot_7_block22: 0xA82094, 
    LocationName.mtteapot_7_block23: 0xA82095, 
    LocationName.mtteapot_7_block24: 0xA82096, 
    LocationName.mtteapot_7_block25: 0xA82097, 
    LocationName.mtteapot_7_block26: 0xA82098, 
    LocationName.mtteapot_7_block27: 0xA82099, 

    LocationName.mtteapot_8_block1:  0xA82100, 
    LocationName.mtteapot_8_block2:  0xA82101, 
    LocationName.mtteapot_8_block3:  0xA82102, 
    LocationName.mtteapot_8_block4:  0xA82103, 
    LocationName.mtteapot_8_block5:  0xA82104, 
    LocationName.mtteapot_8_block6:  0xA82105, 
    LocationName.mtteapot_8_block7:  0xA82106, 
    LocationName.mtteapot_8_block8:  0xA82107, 
    LocationName.mtteapot_8_block9:  0xA82108, 
    LocationName.mtteapot_8_block10: 0xA82109, 
    LocationName.mtteapot_8_block11: 0xA82110, 
    LocationName.mtteapot_8_block12: 0xA82111, 
    LocationName.mtteapot_8_block13: 0xA82112, 
    LocationName.mtteapot_8_block14: 0xA82113, 
    LocationName.mtteapot_8_block15: 0xA82114, 
    LocationName.mtteapot_8_block16: 0xA82115, 
    LocationName.mtteapot_8_block17: 0xA82116, 
    LocationName.mtteapot_8_block18: 0xA82117, 
    LocationName.mtteapot_8_block19: 0xA82118, 
    LocationName.mtteapot_8_block20: 0xA82119, 
    LocationName.mtteapot_8_block21: 0xA82120, 
    LocationName.mtteapot_8_block22: 0xA82121, 

    LocationName.mtteapot_9_block1:  0xA82122, 
    LocationName.mtteapot_9_block2:  0xA82123, 
    LocationName.mtteapot_9_block3:  0xA82124, 
    LocationName.mtteapot_9_block4:  0xA82125, 
    LocationName.mtteapot_9_block5:  0xA82126, 
    LocationName.mtteapot_9_block6:  0xA82127, 
    LocationName.mtteapot_9_block7:  0xA82128, 
    LocationName.mtteapot_9_block8:  0xA82129, 
    LocationName.mtteapot_9_block9:  0xA82130, 
    LocationName.mtteapot_9_block10: 0xA82131, 
    LocationName.mtteapot_9_block11: 0xA82132, 
    LocationName.mtteapot_9_block12: 0xA82133, 
    LocationName.mtteapot_9_block13: 0xA82134, 
    LocationName.mtteapot_9_block14: 0xA82135, 
    LocationName.mtteapot_9_block15: 0xA82136, 

    LocationName.mtteapot_10_block1:  0xA82137, 
    LocationName.mtteapot_10_block2:  0xA82138, 
    LocationName.mtteapot_10_block3:  0xA82139, 
    LocationName.mtteapot_10_block4:  0xA82140, 
    LocationName.mtteapot_10_block5:  0xA82141, 
    LocationName.mtteapot_10_block6:  0xA82142, 
    LocationName.mtteapot_10_block7:  0xA82143, 
    LocationName.mtteapot_10_block8:  0xA82144, 
    LocationName.mtteapot_10_block9:  0xA82145, 
    LocationName.mtteapot_10_block10: 0xA82146,
    LocationName.mtteapot_10_block11: 0xA82147,
    LocationName.mtteapot_10_block12: 0xA82148,
    LocationName.mtteapot_10_block13: 0xA82149,
    LocationName.mtteapot_10_block14: 0xA82150,
    LocationName.mtteapot_10_block15: 0xA82151,
    LocationName.mtteapot_10_block16: 0xA82152,
    LocationName.mtteapot_10_block17: 0xA82153,
    LocationName.mtteapot_10_block18: 0xA82154,
    LocationName.mtteapot_10_block19: 0xA82155,
    LocationName.mtteapot_10_block20: 0xA82156,
    LocationName.mtteapot_10_block21: 0xA82157,
    LocationName.mtteapot_10_block22: 0xA82158,

    LocationName.mtteapot_11_block1:  0xA82159, 
    LocationName.mtteapot_11_block2:  0xA82160, 
    LocationName.mtteapot_11_block3:  0xA82161, 
    LocationName.mtteapot_11_block4:  0xA82162, 
    LocationName.mtteapot_11_block5:  0xA82163, 
    LocationName.mtteapot_11_block6:  0xA82164, 
    LocationName.mtteapot_11_block7:  0xA82165, 
    LocationName.mtteapot_11_block8:  0xA82166, 
    LocationName.mtteapot_11_block9:  0xA82167, 
    LocationName.mtteapot_11_block10: 0xA82168,
    LocationName.mtteapot_11_block11: 0xA82169,
    LocationName.mtteapot_11_block12: 0xA82170,
    LocationName.mtteapot_11_block13: 0xA82171,
    LocationName.mtteapot_11_block14: 0xA82172,
    LocationName.mtteapot_11_block15: 0xA82173,
    LocationName.mtteapot_11_block16: 0xA82174,
    LocationName.mtteapot_11_block17: 0xA82175,
    LocationName.mtteapot_11_block18: 0xA82176,

    LocationName.mtteapot_12_block1: 0xA82177, 
    LocationName.mtteapot_12_block2: 0xA82178, 
    LocationName.mtteapot_12_block3: 0xA82179, 
    LocationName.mtteapot_12_block4: 0xA82180, 
    LocationName.mtteapot_12_block5: 0xA82181, 
    LocationName.mtteapot_12_block6: 0xA82182, 
    LocationName.mtteapot_12_block7: 0xA82183, 
    LocationName.mtteapot_12_block8: 0xA82184, 

    LocationName.mtteapot_13_block1:  0xA82185, 
    LocationName.mtteapot_13_block2:  0xA82186, 
    LocationName.mtteapot_13_block3:  0xA82187, 
    LocationName.mtteapot_13_block4:  0xA82188, 
    LocationName.mtteapot_13_block5:  0xA82189, 
    LocationName.mtteapot_13_block6:  0xA82190, 
    LocationName.mtteapot_13_block7:  0xA82191, 
    LocationName.mtteapot_13_block8:  0xA82192, 
    LocationName.mtteapot_13_block9:  0xA82193, 
    LocationName.mtteapot_13_block10: 0xA82194,
    LocationName.mtteapot_13_block11: 0xA82195,
    LocationName.mtteapot_13_block12: 0xA82196,
    LocationName.mtteapot_13_block13: 0xA82197,
    LocationName.mtteapot_13_block14: 0xA82198,
    LocationName.mtteapot_13_block15: 0xA82199,
    LocationName.mtteapot_13_block16: 0xA82200,
    LocationName.mtteapot_13_block17: 0xA82201,
    LocationName.mtteapot_13_block18: 0xA82202,
    LocationName.mtteapot_13_block19: 0xA82203,
    LocationName.mtteapot_13_block20: 0xA82204,
    LocationName.mtteapot_13_block21: 0xA82205,

    LocationName.sherbetland_14_block1: 0xA82206, 
    LocationName.sherbetland_14_block2: 0xA82207, 
    LocationName.sherbetland_14_block3: 0xA82208, 
    LocationName.sherbetland_14_block4: 0xA82209, 
    LocationName.sherbetland_14_block5: 0xA82210, 
    LocationName.sherbetland_14_block6: 0xA82211, 
    LocationName.sherbetland_14_block7: 0xA82212, 

    LocationName.sherbetland_15_block1:  0xA82213,
    LocationName.sherbetland_15_block2:  0xA82214,
    LocationName.sherbetland_15_block3:  0xA82215,
    LocationName.sherbetland_15_block4:  0xA82216,
    LocationName.sherbetland_15_block5:  0xA82217,
    LocationName.sherbetland_15_block6:  0xA82218,
    LocationName.sherbetland_15_block7:  0xA82219,
    LocationName.sherbetland_15_block8:  0xA82220,
    LocationName.sherbetland_15_block9:  0xA82221,
    LocationName.sherbetland_15_block10: 0xA82222,
    LocationName.sherbetland_15_block11: 0xA82223,
    LocationName.sherbetland_15_block12: 0xA82224,
    LocationName.sherbetland_15_block13: 0xA82225,

    LocationName.sherbetland_16_block1: 0xA82226,
    LocationName.sherbetland_16_block2: 0xA82227,
    LocationName.sherbetland_16_block3: 0xA82228,
    LocationName.sherbetland_16_block4: 0xA82229,
    LocationName.sherbetland_16_block5: 0xA82230,
    LocationName.sherbetland_16_block6: 0xA82231,
    LocationName.sherbetland_16_block7: 0xA82232,
    LocationName.sherbetland_16_block8: 0xA82233,

    LocationName.sherbetland_17_block1:  0xA82234,
    LocationName.sherbetland_17_block2:  0xA82235,
    LocationName.sherbetland_17_block3:  0xA82236,
    LocationName.sherbetland_17_block4:  0xA82237,
    LocationName.sherbetland_17_block5:  0xA82238,
    LocationName.sherbetland_17_block6:  0xA82239,
    LocationName.sherbetland_17_block7:  0xA82240,
    LocationName.sherbetland_17_block8:  0xA82241,
    LocationName.sherbetland_17_block9:  0xA82242,
    LocationName.sherbetland_17_block10: 0xA82243,
    LocationName.sherbetland_17_block11: 0xA82244,
    LocationName.sherbetland_17_block12: 0xA82245,
    LocationName.sherbetland_17_block13: 0xA82246,
    LocationName.sherbetland_17_block14: 0xA82247,
    LocationName.sherbetland_17_block15: 0xA82248,
    LocationName.sherbetland_17_block16: 0xA82249,
    LocationName.sherbetland_17_block17: 0xA82250,
    LocationName.sherbetland_17_block18: 0xA82251,

    LocationName.sherbetland_18_block1: 0xA82252,
    LocationName.sherbetland_18_block2: 0xA82253,
    LocationName.sherbetland_18_block3: 0xA82254,
    LocationName.sherbetland_18_block4: 0xA82255,
    LocationName.sherbetland_18_block5: 0xA82256,
    LocationName.sherbetland_18_block6: 0xA82257,
    LocationName.sherbetland_18_block7: 0xA82258,
    LocationName.sherbetland_18_block8: 0xA82259,
    LocationName.sherbetland_18_block9: 0xA82260,

    LocationName.sherbetland_19_block1:  0xA82261,
    LocationName.sherbetland_19_block2:  0xA82262,
    LocationName.sherbetland_19_block3:  0xA82263,
    LocationName.sherbetland_19_block4:  0xA82264,
    LocationName.sherbetland_19_block5:  0xA82265,
    LocationName.sherbetland_19_block6:  0xA82266,
    LocationName.sherbetland_19_block7:  0xA82267,
    LocationName.sherbetland_19_block8:  0xA82268,
    LocationName.sherbetland_19_block9:  0xA82269,
    LocationName.sherbetland_19_block10: 0xA82270,
    LocationName.sherbetland_19_block11: 0xA82271,
    LocationName.sherbetland_19_block12: 0xA82272,
    LocationName.sherbetland_19_block13: 0xA82273,
    LocationName.sherbetland_19_block14: 0xA82274,

    LocationName.stovecanyon_20_block1:  0xA82275,
    LocationName.stovecanyon_20_block2:  0xA82276,
    LocationName.stovecanyon_20_block3:  0xA82277,
    LocationName.stovecanyon_20_block4:  0xA82278,
    LocationName.stovecanyon_20_block5:  0xA82279,
    LocationName.stovecanyon_20_block6:  0xA82280,
    LocationName.stovecanyon_20_block7:  0xA82281,
    LocationName.stovecanyon_20_block8:  0xA82282,
    LocationName.stovecanyon_20_block9:  0xA82283,
    LocationName.stovecanyon_20_block10: 0xA82284,
    LocationName.stovecanyon_20_block11: 0xA82285,

    LocationName.stovecanyon_21_block1: 0xA82286,
    LocationName.stovecanyon_21_block2: 0xA82287,
    LocationName.stovecanyon_21_block3: 0xA82288,
    LocationName.stovecanyon_21_block4: 0xA82289,
    LocationName.stovecanyon_21_block5: 0xA82290,
    LocationName.stovecanyon_21_block6: 0xA82291,
    LocationName.stovecanyon_21_block7: 0xA82292,

    LocationName.stovecanyon_22_block1: 0xA82293,
    LocationName.stovecanyon_22_block2: 0xA82294,
    LocationName.stovecanyon_22_block3: 0xA82295,
    LocationName.stovecanyon_22_block4: 0xA82296,
    LocationName.stovecanyon_22_block5: 0xA82297,
    LocationName.stovecanyon_22_block6: 0xA82298,
    LocationName.stovecanyon_22_block7: 0xA82299,

    LocationName.stovecanyon_23_block1: 0xA82300,
    LocationName.stovecanyon_23_block2: 0xA82301,
    LocationName.stovecanyon_23_block3: 0xA82302,
    LocationName.stovecanyon_23_block4: 0xA82303,
    LocationName.stovecanyon_23_block5: 0xA82304,
    LocationName.stovecanyon_23_block6: 0xA82305,
    LocationName.stovecanyon_23_block7: 0xA82306,
    LocationName.stovecanyon_23_block8: 0xA82307,

    LocationName.stovecanyon_24_block1: 0xA82308,
    LocationName.stovecanyon_24_block2: 0xA82309,
    LocationName.stovecanyon_24_block3: 0xA82310,
    LocationName.stovecanyon_24_block4: 0xA82311,
    LocationName.stovecanyon_24_block5: 0xA82312,
    LocationName.stovecanyon_24_block6: 0xA82313,
    LocationName.stovecanyon_24_block7: 0xA82314,
    LocationName.stovecanyon_24_block8: 0xA82315,

    LocationName.stovecanyon_25_block1: 0xA82316,
    LocationName.stovecanyon_25_block2: 0xA82317,
    LocationName.stovecanyon_25_block3: 0xA82318,
    LocationName.stovecanyon_25_block4: 0xA82319,
    LocationName.stovecanyon_25_block5: 0xA82320,
    LocationName.stovecanyon_25_block6: 0xA82321,
    LocationName.stovecanyon_25_block7: 0xA82322,

    LocationName.ssteacup_26_block1:  0xA82323, 
    LocationName.ssteacup_26_block2:  0xA82324, 
    LocationName.ssteacup_26_block3:  0xA82325, 
    LocationName.ssteacup_26_block4:  0xA82326, 
    LocationName.ssteacup_26_block5:  0xA82327, 
    LocationName.ssteacup_26_block6:  0xA82328, 
    LocationName.ssteacup_26_block7:  0xA82329, 
    LocationName.ssteacup_26_block8:  0xA82330, 
    LocationName.ssteacup_26_block9:  0xA82331, 
    LocationName.ssteacup_26_block10: 0xA82332,
    LocationName.ssteacup_26_block11: 0xA82333,

    LocationName.ssteacup_27_block1:  0xA82334, 
    LocationName.ssteacup_27_block2:  0xA82335, 
    LocationName.ssteacup_27_block3:  0xA82336, 
    LocationName.ssteacup_27_block4:  0xA82337, 
    LocationName.ssteacup_27_block5:  0xA82338, 
    LocationName.ssteacup_27_block6:  0xA82339, 
    LocationName.ssteacup_27_block7:  0xA82340, 
    LocationName.ssteacup_27_block8:  0xA82341, 
    LocationName.ssteacup_27_block9:  0xA82342, 
    LocationName.ssteacup_27_block10: 0xA82343,
    LocationName.ssteacup_27_block11: 0xA82344,
    LocationName.ssteacup_27_block12: 0xA82345,
    LocationName.ssteacup_27_block13: 0xA82346,
    LocationName.ssteacup_27_block14: 0xA82347,
    LocationName.ssteacup_27_block15: 0xA82348,
    LocationName.ssteacup_27_block16: 0xA82349,
    LocationName.ssteacup_27_block17: 0xA82350,
    LocationName.ssteacup_27_block18: 0xA82351,
    LocationName.ssteacup_27_block19: 0xA82352,
    LocationName.ssteacup_27_block20: 0xA82353,
    LocationName.ssteacup_27_block21: 0xA82354,
    LocationName.ssteacup_27_block22: 0xA82355,
    LocationName.ssteacup_27_block23: 0xA82356,
    LocationName.ssteacup_27_block24: 0xA82357,
    LocationName.ssteacup_27_block25: 0xA82358,

    LocationName.ssteacup_28_block1:  0xA82359, 
    LocationName.ssteacup_28_block2:  0xA82360, 
    LocationName.ssteacup_28_block3:  0xA82361, 
    LocationName.ssteacup_28_block4:  0xA82362, 
    LocationName.ssteacup_28_block5:  0xA82363, 
    LocationName.ssteacup_28_block6:  0xA82364, 
    LocationName.ssteacup_28_block7:  0xA82365, 
    LocationName.ssteacup_28_block8:  0xA82366, 
    LocationName.ssteacup_28_block9:  0xA82367, 
    LocationName.ssteacup_28_block10: 0xA82368,

    LocationName.ssteacup_29_block1:  0xA82369, 
    LocationName.ssteacup_29_block2:  0xA82370, 
    LocationName.ssteacup_29_block3:  0xA82371, 
    LocationName.ssteacup_29_block4:  0xA82372, 
    LocationName.ssteacup_29_block5:  0xA82373, 
    LocationName.ssteacup_29_block6:  0xA82374, 
    LocationName.ssteacup_29_block7:  0xA82375, 
    LocationName.ssteacup_29_block8:  0xA82376, 
    LocationName.ssteacup_29_block9:  0xA82377, 
    LocationName.ssteacup_29_block10: 0xA82378,
    LocationName.ssteacup_29_block11: 0xA82379,

    LocationName.ssteacup_30_block1:  0xA82380, 
    LocationName.ssteacup_30_block2:  0xA82381, 
    LocationName.ssteacup_30_block3:  0xA82382, 
    LocationName.ssteacup_30_block4:  0xA82383, 
    LocationName.ssteacup_30_block5:  0xA82384, 
    LocationName.ssteacup_30_block6:  0xA82385, 
    LocationName.ssteacup_30_block7:  0xA82386, 
    LocationName.ssteacup_30_block8:  0xA82387, 
    LocationName.ssteacup_30_block9:  0xA82388, 
    LocationName.ssteacup_30_block10: 0xA82389,
    LocationName.ssteacup_30_block11: 0xA82390,
    LocationName.ssteacup_30_block12: 0xA82391,
    LocationName.ssteacup_30_block13: 0xA82392,
    LocationName.ssteacup_30_block14: 0xA82393,
    LocationName.ssteacup_30_block15: 0xA82394,
    LocationName.ssteacup_30_block16: 0xA82395,
    LocationName.ssteacup_30_block17: 0xA82396,
    LocationName.ssteacup_30_block18: 0xA82397,
    LocationName.ssteacup_30_block19: 0xA82398,
    LocationName.ssteacup_30_block20: 0xA82399,
    LocationName.ssteacup_30_block21: 0xA82400,
    LocationName.ssteacup_30_block22: 0xA82401,
    LocationName.ssteacup_30_block23: 0xA82402,

    LocationName.parsleywoods_31_block1:  0xA82403,
    LocationName.parsleywoods_31_block2:  0xA82404,
    LocationName.parsleywoods_31_block3:  0xA82405,
    LocationName.parsleywoods_31_block4:  0xA82406,
    LocationName.parsleywoods_31_block5:  0xA82407,
    LocationName.parsleywoods_31_block6:  0xA82408,
    LocationName.parsleywoods_31_block7:  0xA82409,
    LocationName.parsleywoods_31_block8:  0xA82410,
    LocationName.parsleywoods_31_block9:  0xA82411,
    LocationName.parsleywoods_31_block10: 0xA82412,
    LocationName.parsleywoods_31_block11: 0xA82413,
    LocationName.parsleywoods_31_block12: 0xA82414,
    LocationName.parsleywoods_31_block13: 0xA82415,
    LocationName.parsleywoods_31_block14: 0xA82416,

    LocationName.parsleywoods_31_drained_block1:  0xA82417,
    LocationName.parsleywoods_31_drained_block2:  0xA82418,
    LocationName.parsleywoods_31_drained_block3:  0xA82419,
    LocationName.parsleywoods_31_drained_block4:  0xA82420,
    LocationName.parsleywoods_31_drained_block5:  0xA82421,
    LocationName.parsleywoods_31_drained_block6:  0xA82422,
    LocationName.parsleywoods_31_drained_block7:  0xA82423,
    LocationName.parsleywoods_31_drained_block8:  0xA82424,
    LocationName.parsleywoods_31_drained_block9:  0xA82425,
    LocationName.parsleywoods_31_drained_block10: 0xA82426,
    LocationName.parsleywoods_31_drained_block11: 0xA82427,
    LocationName.parsleywoods_31_drained_block12: 0xA82428,
    LocationName.parsleywoods_31_drained_block13: 0xA82429,

    LocationName.parsleywoods_32_block1: 0xA82430,
    LocationName.parsleywoods_32_block2: 0xA82431,
    LocationName.parsleywoods_32_block3: 0xA82432,
    LocationName.parsleywoods_32_block4: 0xA82433,

    LocationName.parsleywoods_33_block1:  0xA82434,
    LocationName.parsleywoods_33_block2:  0xA82435,
    LocationName.parsleywoods_33_block3:  0xA82436,
    LocationName.parsleywoods_33_block4:  0xA82437,
    LocationName.parsleywoods_33_block5:  0xA82438,
    LocationName.parsleywoods_33_block6:  0xA82439,
    LocationName.parsleywoods_33_block7:  0xA82440,
    LocationName.parsleywoods_33_block8:  0xA82441,
    LocationName.parsleywoods_33_block9:  0xA82442,
    LocationName.parsleywoods_33_block10: 0xA82443,

    LocationName.parsleywoods_34_block1:  0xA82444,
    LocationName.parsleywoods_34_block2:  0xA82445,
    LocationName.parsleywoods_34_block3:  0xA82446,
    LocationName.parsleywoods_34_block4:  0xA82447,
    LocationName.parsleywoods_34_block5:  0xA82448,
    LocationName.parsleywoods_34_block6:  0xA82449,
    LocationName.parsleywoods_34_block7:  0xA82450,
    LocationName.parsleywoods_34_block8:  0xA82451,
    LocationName.parsleywoods_34_block9:  0xA82452,
    LocationName.parsleywoods_34_block10: 0xA82453,
    LocationName.parsleywoods_34_block11: 0xA82454,
    LocationName.parsleywoods_34_block12: 0xA82455,

    LocationName.parsleywoods_35_block1: 0xA82456,
    LocationName.parsleywoods_35_block2: 0xA82457,
    LocationName.parsleywoods_35_block3: 0xA82458,
    LocationName.parsleywoods_35_block4: 0xA82459,
    LocationName.parsleywoods_35_block5: 0xA82460,

    LocationName.parsleywoods_36_block1: 0xA82461,
    LocationName.parsleywoods_36_block2: 0xA82462,
    LocationName.parsleywoods_36_block3: 0xA82463,
    LocationName.parsleywoods_36_block4: 0xA82464,
    LocationName.parsleywoods_36_block5: 0xA82465,
    LocationName.parsleywoods_36_block6: 0xA82466,
    LocationName.parsleywoods_36_block7: 0xA82467,
    LocationName.parsleywoods_36_block8: 0xA82468,
    LocationName.parsleywoods_36_block9: 0xA82469,

    LocationName.syrupcastle_37_block1:  0xA82470,
    LocationName.syrupcastle_37_block2:  0xA82471,
    LocationName.syrupcastle_37_block3:  0xA82472,
    LocationName.syrupcastle_37_block4:  0xA82473,
    LocationName.syrupcastle_37_block5:  0xA82474,
    LocationName.syrupcastle_37_block6:  0xA82475,
    LocationName.syrupcastle_37_block7:  0xA82476,
    LocationName.syrupcastle_37_block8:  0xA82477,
    LocationName.syrupcastle_37_block9:  0xA82478,
    LocationName.syrupcastle_37_block10: 0xA82479,
    LocationName.syrupcastle_37_block11: 0xA82480,
    LocationName.syrupcastle_37_block12: 0xA82481,
    LocationName.syrupcastle_37_block13: 0xA82482,
    LocationName.syrupcastle_37_block14: 0xA82483,
    LocationName.syrupcastle_37_block15: 0xA82484,
    LocationName.syrupcastle_37_block16: 0xA82485,
    LocationName.syrupcastle_37_block17: 0xA82486,
    LocationName.syrupcastle_37_block18: 0xA82487,
    LocationName.syrupcastle_37_block19: 0xA82488,
    LocationName.syrupcastle_37_block20: 0xA82489,
    LocationName.syrupcastle_37_block21: 0xA82490,
    
    LocationName.syrupcastle_38_block1: 0xA82491,
    LocationName.syrupcastle_38_block2: 0xA82492,
    LocationName.syrupcastle_38_block3: 0xA82493,
    LocationName.syrupcastle_38_block4: 0xA82494,
    LocationName.syrupcastle_38_block5: 0xA82495,
    LocationName.syrupcastle_38_block6: 0xA82496,
    LocationName.syrupcastle_38_block7: 0xA82497,
    LocationName.syrupcastle_38_block8: 0xA82498,
    LocationName.syrupcastle_38_block9: 0xA82499,
    
    LocationName.syrupcastle_39_block1:  0xA82500,
    LocationName.syrupcastle_39_block2:  0xA82501,
    LocationName.syrupcastle_39_block3:  0xA82502,
    LocationName.syrupcastle_39_block4:  0xA82503,
    LocationName.syrupcastle_39_block5:  0xA82504,
    LocationName.syrupcastle_39_block6:  0xA82505,
    LocationName.syrupcastle_39_block7:  0xA82506,
    LocationName.syrupcastle_39_block8:  0xA82507,
    LocationName.syrupcastle_39_block9:  0xA82508,
    LocationName.syrupcastle_39_block10: 0xA82509,
    LocationName.syrupcastle_39_block11: 0xA82510,
    
    LocationName.syrupcastle_40_block1:  0xA82511,
    LocationName.syrupcastle_40_block2:  0xA82512,
    LocationName.syrupcastle_40_block3:  0xA82513,
    LocationName.syrupcastle_40_block4:  0xA82514,
    LocationName.syrupcastle_40_block5:  0xA82515,
    LocationName.syrupcastle_40_block6:  0xA82516,
    LocationName.syrupcastle_40_block7:  0xA82517,
    LocationName.syrupcastle_40_block8:  0xA82518,
    LocationName.syrupcastle_40_block9:  0xA82519,
    LocationName.syrupcastle_40_block10: 0xA82520,
    LocationName.syrupcastle_40_block11: 0xA82521,
    LocationName.syrupcastle_40_block12: 0xA82522,
    LocationName.syrupcastle_40_block13: 0xA82523,
    LocationName.syrupcastle_40_block14: 0xA82524,
    LocationName.syrupcastle_40_block15: 0xA82525,
    LocationName.syrupcastle_40_block16: 0xA82526,
    LocationName.syrupcastle_40_block17: 0xA82527,
    LocationName.syrupcastle_40_block18: 0xA82528,
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
    **block_location_table,
    **garlic_location_table,
    **boss_item_location_table,
}

checkable_locations = {
    **level_location_table,
    **treasure_location_table,
}

unlock_locations = {
    **level_location_table,
    **treasure_location_table,
    **block_location_table,
}

location_table = {}


def setup_locations(world, player: int):
    location_table = {**level_location_table}
    location_table.update({**boss_item_location_table})
    if world.treasure_checks[player].value:
        location_table.update({**treasure_location_table})
    if world.blocksanity[player].value:
        location_table.update({**block_location_table})
    if world.goal[player] == "garlic_hunt":
        location_table.update({**garlic_location_table})
    #else:
    #    location_table.update({**genie_location_table})    
    return location_table


lookup_id_to_name: typing.Dict[int, str] = {id: name for name, _ in all_locations.items()}

boss_location_dict={
0xA80B20: 0xA80B2B,
0xA80C80: 0xA80C8B,
0xA81380: 0xA8138B,
0xA81040: 0xA8104B,
0xA81110: 0xA8111B,
0xA81220: 0xA8122B,
0xA81408: 0xA8140B,
}