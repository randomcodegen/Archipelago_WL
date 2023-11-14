import hashlib
import os
import math
import Utils
import bsdiff4
import random
from worlds.Files import APDeltaPatch

WORLDHASH = 'd9d957771484ef846d4e8d241f6f2815'
ROM_PLAYER_LIMIT = 65535

def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if WORLDHASH != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for WORLD release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        file_name = options["wl_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name

class WLDeltaPatch(APDeltaPatch):
    hash = WORLDHASH
    game = "Wario Land"
    patch_file_ending = ".apwl"
    result_file_ending = ".gb"

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()


class Rom:

    def __init__(self, file, patch=True, vanillaRom=None, name=None, hash=None):
        self.name = name
        self.hash = hash
        self.orig_buffer = None

        with open(file, 'rb') as stream:
            self.buffer = Utils.read_snes_rom(stream)
        
    def read_bit(self, address: int, bit_number: int) -> bool:
        bitflag = (1 << bit_number)
        return ((self.buffer[address] & bitflag) != 0)

    def read_byte(self, address: int) -> int:
        return self.buffer[address]

    def read_bytes(self, startaddress: int, length: int) -> bytes:
        return self.buffer[startaddress:startaddress + length]

    def write_byte(self, address: int, value: int):
        self.buffer[address] = value

    def write_bytes(self, startaddress: int, values):
        self.buffer[startaddress:startaddress + len(values)] = values

    def write_to_file(self, file):
        with open(file, 'wb') as outfile:
            outfile.write(self.buffer)

    def read_from_file(self, file):
        with open(file, 'rb') as stream:
            self.buffer = bytearray(stream.read())

# Some of the patched instructions are missing their 
# first byte because that one overlaps with the vanilla rom

# Block basic movement abilities
def patch_basic_abilities(rom):
    # Climb
    rom.write_byte(0x34a1b,0xc3) #d:4a1b    jp 7462
    rom.write_byte(0x34a1c,0x62) #d:4a1c    
    rom.write_byte(0x34a1d,0x74) #d:4a1d    
    #---
    rom.write_byte(0x37462,0xea) #d:7462    ld (A490),a
    rom.write_byte(0x37463,0x90) #d:7463    
    rom.write_byte(0x37464,0xa4) #d:7464    
    rom.write_byte(0x37465,0xfa) #d:7465    ld a,(A407)
    rom.write_byte(0x37466,0x07) #d:7466    
    rom.write_byte(0x37467,0xa4) #d:7467    
    rom.write_byte(0x37468,0xa7) #d:7468    and a
    rom.write_byte(0x37469,0x28) #d:7469    jr z,04
    rom.write_byte(0x3746a,0x04) #d:746a    
    rom.write_byte(0x3746b,0xfa) #d:746b    ld a,(A490)
    rom.write_byte(0x3746c,0x90) #d:746c    
    rom.write_byte(0x3746d,0xa4) #d:746d    
    rom.write_byte(0x3746e,0xc3) #d:746e    jp 4A1E
    rom.write_byte(0x3746f,0x1e) #d:746f    
    rom.write_byte(0x37470,0x4a) #d:7470    
    rom.write_byte(0x37471,0xc3) #d:7471    jp 4A3D
    rom.write_byte(0x37472,0x3d) #d:7472    
    rom.write_byte(0x37473,0x4a) #d:7473    

    # Duck
    rom.write_byte(0x34c5a,0xcd) #d:4c5a    call 7441
    rom.write_byte(0x34c5b,0x41) #d:4c5b    
    rom.write_byte(0x34c5c,0x74) #d:4c5c    
    rom.write_byte(0x34a7c,0xcd) #d:4a7c    call 7441
    rom.write_byte(0x34a7d,0x41) #d:4a7d    
    rom.write_byte(0x34a7e,0x74) #d:4a7e    
    #---
    rom.write_byte(0x37441,0xfa) #d:7441    ld a,(A408)
    rom.write_byte(0x37442,0x08) #d:7442    
    rom.write_byte(0x37443,0xa4) #d:7443    
    rom.write_byte(0x37444,0xa7) #d:7444    and a
    rom.write_byte(0x37445,0x28) #d:7445    jr z,04
    rom.write_byte(0x37446,0x04) #d:7446    
    rom.write_byte(0x37447,0xfa) #d:7447    ld a,(A956)
    rom.write_byte(0x37448,0x56) #d:7448    
    rom.write_byte(0x37449,0xa9) #d:7449    
    rom.write_byte(0x3744a,0xc9) #d:744a    ret
    rom.write_byte(0x3744b,0x3e) #d:744b    ld a,01
    rom.write_byte(0x3744c,0x01) #d:744c    
    rom.write_byte(0x3744d,0xc9) #d:744d    ret

    # High jump
    rom.write_byte(0x34e75,0xcd) #d:4e75    call 743A
    rom.write_byte(0x34e76,0x3a) #d:4e76    
    rom.write_byte(0x34e77,0x74) #d:4e77    
    #---
    rom.write_byte(0x3743a,0xfa) #d:743a    ld a,(A405)
    rom.write_byte(0x3743b,0x05) #d:743b    
    rom.write_byte(0x3743c,0xa4) #d:743c    
    rom.write_byte(0x3743d,0xea) #d:743d    ld (A92C),a
    rom.write_byte(0x3743e,0x2c) #d:743e    
    rom.write_byte(0x3743f,0xa9) #d:743f    
    rom.write_byte(0x37440,0xc9) #d:7440    ret

    # Dash
    rom.write_byte(0x35bd3,0xcd) #d:5bd3    call 7416
    rom.write_byte(0x35bd4,0x16) #d:5bd4    
    rom.write_byte(0x35bd5,0x74) #d:5bd5    
    #---
    rom.write_byte(0x37416,0xfa) #d:7416    ld a,(A404)
    rom.write_byte(0x37417,0x04) #d:7417    
    rom.write_byte(0x37418,0xa4) #d:7418    
    rom.write_byte(0x37419,0xa7) #d:7419    and a
    rom.write_byte(0x3741a,0x28) #d:741a    jr z,04
    rom.write_byte(0x3741b,0x04) #d:741b    
    rom.write_byte(0x3741c,0xfa) #d:741c    ld a,(A34D)
    rom.write_byte(0x3741d,0x4d) #d:741d    
    rom.write_byte(0x3741e,0xa3) #d:741e    
    rom.write_byte(0x3741f,0xc9) #d:741f    ret
    rom.write_byte(0x37420,0x3e) #d:7420    ld a,01
    rom.write_byte(0x37421,0x01) #d:7421    
    rom.write_byte(0x37422,0xc9) #d:7422    ret

    # Create coin
    rom.write_byte(0x34b74,0xcd) #d:4b74    call 742D
    rom.write_byte(0x34b75,0x2d) #d:4b75    
    rom.write_byte(0x34b76,0x74) #d:4b76    
    #---
    rom.write_byte(0x3742d,0xfa) #d:742d    ld a,(A406)
    rom.write_byte(0x3742e,0x06) #d:742e    
    rom.write_byte(0x3742f,0xa4) #d:742f    
    rom.write_byte(0x37430,0xa7) #d:7430    and a
    rom.write_byte(0x37431,0x28) #d:7431    jr z,04
    rom.write_byte(0x37432,0x04) #d:7432    
    rom.write_byte(0x37433,0xfa) #d:7433    ld a,(A9A4)
    rom.write_byte(0x37434,0xa4) #d:7434    
    rom.write_byte(0x37435,0xa9) #d:7435    
    rom.write_byte(0x37436,0xc9) #d:7436    ret
    rom.write_byte(0x37437,0x3e) #d:7437    ld a,01
    rom.write_byte(0x37438,0x01) #d:7438    
    rom.write_byte(0x37439,0xc9) #d:7439    ret

    # Force small wario
    rom.write_byte(0xec4,0xcd) #0:0ec4      call 7F72
    rom.write_byte(0xec5,0x72) #0:0ec5
    rom.write_byte(0xec6,0x7f) #0:0ec6
    #---
    rom.write_byte(0x33f72,0xfa) #c:7f72    ld a,(A410)
    rom.write_byte(0x33f73,0x10) #c:7f73    
    rom.write_byte(0x33f74,0xa4) #c:7f74    
    rom.write_byte(0x33f75,0xa7) #c:7f75    and a
    rom.write_byte(0x33f76,0x20) #c:7f76    jr nz, 3
    rom.write_byte(0x33f77,0x03) #c:7f77    
    rom.write_byte(0x33f78,0xea) #c:7f78    ld (A80A),a
    rom.write_byte(0x33f79,0x0a) #c:7f79    
    rom.write_byte(0x33f7a,0xa8) #c:7f7a    
    rom.write_byte(0x33f7b,0xfa) #c:7f7b    ld a, (A80A)
    rom.write_byte(0x33f7c,0x0a) #c:7f7c    
    rom.write_byte(0x33f7d,0xa8) #c:7f7d    
    rom.write_byte(0x33f7e,0xc9) #c:7f7e    ret
    return

# Block powerup usage
def patch_powerups(rom):
    rom.write_byte(0x364b2,0xcd) #d:64b2    call 738E
    rom.write_byte(0x364b3,0x8e) #d:64b3    
    rom.write_byte(0x364b4,0x73) #d:64b4    
    #---
    rom.write_byte(0x3738e,0xea) #d:738e    ld (A958),a
    rom.write_byte(0x3738f,0x58) #d:738f    
    rom.write_byte(0x37390,0xa9) #d:7390    
    rom.write_byte(0x37391,0xfe) #d:7391    cp a,04
    rom.write_byte(0x37392,0x04) #d:7392    
    rom.write_byte(0x37393,0xd2) #d:7393    jp nc, 73F5
    rom.write_byte(0x37394,0xf5) #d:7394    
    rom.write_byte(0x37395,0x73) #d:7395    
    rom.write_byte(0x37396,0xfe) #d:7396    cp a,03
    rom.write_byte(0x37397,0x03) #d:7397    
    rom.write_byte(0x37398,0xd2) #d:7398    jp nc, 73D5
    rom.write_byte(0x37399,0xd5) #d:7399    
    rom.write_byte(0x3739a,0x73) #d:739a    
    rom.write_byte(0x3739b,0xfe) #d:739b    cp a,02
    rom.write_byte(0x3739c,0x02) #d:739c    
    rom.write_byte(0x3739d,0xd2) #d:739d    jp nc, 73CB
    rom.write_byte(0x3739e,0xcb) #d:739e    
    rom.write_byte(0x3739f,0x73) #d:739f    
    rom.write_byte(0x373a0,0xfe) #d:73a0    cp a,01
    rom.write_byte(0x373a1,0x01) #d:73a1    
    rom.write_byte(0x373a2,0xd2) #d:73a2    jp nc, 73C1
    rom.write_byte(0x373a3,0xc1) #d:73a3    
    rom.write_byte(0x373a4,0x73) #d:73a4    
    #--Check garlic
    rom.write_byte(0x373c1,0xfa) #d:73c1    ld a,(A400)
    rom.write_byte(0x373c2,0x00) #d:73c2    
    rom.write_byte(0x373c3,0xa4) #d:73c3    
    rom.write_byte(0x373c4,0xa7) #d:73c4    and a
    rom.write_byte(0x373c5,0xca) #d:73c5    jp z,6261
    rom.write_byte(0x373c6,0x61) #d:73c6    
    rom.write_byte(0x373c7,0x62) #d:73c7    
    rom.write_byte(0x373c8,0x3e) #d:73c8    ld a,01
    rom.write_byte(0x373c9,0x01) #d:73c9    
    rom.write_byte(0x373ca,0xc9) #d:73ca    ret
    #--Check bull
    rom.write_byte(0x373cb,0xfa) #d:73cb    ld a,(A401)
    rom.write_byte(0x373cc,0x01) #d:73cc    
    rom.write_byte(0x373cd,0xa4) #d:73cd    
    rom.write_byte(0x373ce,0xa7) #d:73ce    and a
    rom.write_byte(0x373cf,0xca) #d:73cf    jp z,6261
    rom.write_byte(0x373d0,0x61) #d:73d0    
    rom.write_byte(0x373d1,0x62) #d:73d1    
    rom.write_byte(0x373d2,0x3e) #d:73d2    ld a,02
    rom.write_byte(0x373d3,0x02) #d:73d3    
    rom.write_byte(0x373d4,0xc9) #d:73d4    ret
    #--Check jet
    rom.write_byte(0x373d5,0xfa) #d:73d5    ld a,(A402)
    rom.write_byte(0x373d6,0x02) #d:73d6    
    rom.write_byte(0x373d7,0xa4) #d:73d7    
    rom.write_byte(0x373d8,0xa7) #d:73d8    and a
    rom.write_byte(0x373d9,0xca) #d:73d9    jp z,6261
    rom.write_byte(0x373da,0x61) #d:73da    
    rom.write_byte(0x373db,0x62) #d:73db    
    rom.write_byte(0x373dc,0x3e) #d:73dc    ld a,03
    rom.write_byte(0x373dd,0x03) #d:73dd    
    rom.write_byte(0x373de,0xc9) #d:73de    ret
    #--Check dragon
    rom.write_byte(0x373f5,0xfa) #d:73f5    ld a,(A403)
    rom.write_byte(0x373f6,0x03) #d:73f6    
    rom.write_byte(0x373f7,0xa4) #d:73f7    
    rom.write_byte(0x373f8,0xa7) #d:73f8    and a
    rom.write_byte(0x373f9,0xca) #d:73f9    jp z,6261
    rom.write_byte(0x373fa,0x61) #d:73fa    
    rom.write_byte(0x373fb,0x62) #d:73fb    
    rom.write_byte(0x373fc,0x3e) #d:73fc    ld a,04
    rom.write_byte(0x373fd,0x04) #d:73fd    
    rom.write_byte(0x373fe,0xc9) #d:73fe    ret
    return

# Patch Map Movement
def patch_world_enter(rom):
    # Blocking the world entering is only required if the setting is active.

    rom.write_byte(0x20187,0xc3) #8:4187    jp 664F
    rom.write_byte(0x20188,0x4f) #8:4188    
    rom.write_byte(0x20189,0x66) #8:4189    
    #--
    rom.write_byte(0x2264f,0xfa) #8:664f    ld a,(A79F)
    rom.write_byte(0x22650,0x9f) #8:6650    
    rom.write_byte(0x22651,0xa7) #8:6651    
    rom.write_byte(0x22652,0xfe) #8:6652    cp a,07
    rom.write_byte(0x22653,0x07) #8:6653    
    rom.write_byte(0x22654,0xd2) #8:6654    jp nc, 4B5E
    rom.write_byte(0x22655,0x5e) #8:6655    
    rom.write_byte(0x22656,0x4b) #8:6656    
    rom.write_byte(0x22657,0xfe) #8:6657    cp a,06
    rom.write_byte(0x22658,0x06) #8:6658    
    rom.write_byte(0x22659,0xd2) #8:6659    jp nc, 4B52
    rom.write_byte(0x2265a,0x52) #8:665a    
    rom.write_byte(0x2265b,0x4b) #8:665b    
    rom.write_byte(0x2265c,0xfe) #8:665c    cp a,05
    rom.write_byte(0x2265d,0x05) #8:665d    
    rom.write_byte(0x2265e,0xd2) #8:665e    jp nc, 4B46
    rom.write_byte(0x2265f,0x46) #8:665f    
    rom.write_byte(0x22660,0x4b) #8:6660    
    rom.write_byte(0x22661,0xfe) #8:6661    cp a,04
    rom.write_byte(0x22662,0x04) #8:6662    
    rom.write_byte(0x22663,0xd2) #8:6663    jp nc, 4AEC
    rom.write_byte(0x22664,0xec) #8:6664    
    rom.write_byte(0x22665,0x4a) #8:6665    
    rom.write_byte(0x22666,0xfe) #8:6666    cp a,03
    rom.write_byte(0x22667,0x03) #8:6667    
    rom.write_byte(0x22668,0xd2) #8:6668    jp nc, 4A2F
    rom.write_byte(0x22669,0x2f) #8:6669    
    rom.write_byte(0x2266a,0x4a) #8:666a    
    rom.write_byte(0x2266b,0xfe) #8:666b    cp a,02
    rom.write_byte(0x2266c,0x02) #8:666c    
    rom.write_byte(0x2266d,0xd2) #8:666d    jp nc, 4A23
    rom.write_byte(0x2266e,0x23) #8:666e    
    rom.write_byte(0x2266f,0x4a) #8:666f    
    rom.write_byte(0x22670,0xfe) #8:6670    cp a,01
    rom.write_byte(0x22671,0x01) #8:6671    
    rom.write_byte(0x22672,0xd2) #8:6672    jp nc, 49CC
    rom.write_byte(0x22673,0xcc) #8:6673    
    rom.write_byte(0x22674,0x49) #8:6674    
    rom.write_byte(0x22675,0xfe) #8:6675    cp a,00
    rom.write_byte(0x22676,0x00) #8:6676    
    rom.write_byte(0x22677,0xd2) #8:6677    jp nc, 49C0
    rom.write_byte(0x22678,0xc0) #8:6678    
    rom.write_byte(0x22679,0x49) #8:6679    
    #--
    rom.write_byte(0x209c0,0xfa) #8:49c0    ld a,(A409)
    rom.write_byte(0x209c1,0x09) #8:49c1    
    rom.write_byte(0x209c2,0xa4) #8:49c2    
    rom.write_byte(0x209c3,0xa7) #8:49c3    and a
    rom.write_byte(0x209c4,0xca) #8:49c4    jp z,41C4
    rom.write_byte(0x209c5,0xc4) #8:49c5    
    rom.write_byte(0x209c6,0x41) #8:49c6    
    rom.write_byte(0x209c7,0x3e) #8:49c7    ld a,23
    rom.write_byte(0x209c8,0x23) #8:49c8    
    rom.write_byte(0x209c9,0xc3) #8:49c9    jp 418A
    rom.write_byte(0x209ca,0x8a) #8:49ca    
    rom.write_byte(0x209cb,0x41) #8:49cb    
    #--
    rom.write_byte(0x209cc,0xfa) #8:49cc    ld a,(A40A)
    rom.write_byte(0x209cd,0x0a) #8:49cd    
    rom.write_byte(0x209ce,0xa4) #8:49ce    
    rom.write_byte(0x209cf,0xa7) #8:49cf    and a
    rom.write_byte(0x209d0,0xca) #8:49d0    jp z,41C4
    rom.write_byte(0x209d1,0xc4) #8:49d1    
    rom.write_byte(0x209d2,0x41) #8:49d2    
    rom.write_byte(0x209d3,0x3e) #8:49d3    ld a,23
    rom.write_byte(0x209d4,0x23) #8:49d4    
    rom.write_byte(0x209d5,0xc3) #8:49d5    jp 418A
    rom.write_byte(0x209d6,0x8a) #8:49d6    
    rom.write_byte(0x209d7,0x41) #8:49d7    
    #--
    rom.write_byte(0x20a23,0xfa) #8:4a23    ld a,(A40B)
    rom.write_byte(0x20a24,0x0b) #8:4a24    
    rom.write_byte(0x20a25,0xa4) #8:4a25    
    rom.write_byte(0x20a26,0xa7) #8:4a26    and a
    rom.write_byte(0x20a27,0xca) #8:4a27    jp z,41C4
    rom.write_byte(0x20a28,0xc4) #8:4a28    
    rom.write_byte(0x20a29,0x41) #8:4a29    
    rom.write_byte(0x20a2a,0x3e) #8:4a2a    ld a,23
    rom.write_byte(0x20a2b,0x23) #8:4a2b    
    rom.write_byte(0x20a2c,0xc3) #8:4a2c    jp 418A
    rom.write_byte(0x20a2d,0x8a) #8:4a2d    
    rom.write_byte(0x20a2e,0x41) #8:4a2e    
    #--
    rom.write_byte(0x20a2f,0xfa) #8:4a2f    ld a,(A40C)
    rom.write_byte(0x20a30,0x0c) #8:4a30    
    rom.write_byte(0x20a31,0xa4) #8:4a31    
    rom.write_byte(0x20a32,0xa7) #8:4a32    and a
    rom.write_byte(0x20a33,0xca) #8:4a33    jp z,41C4
    rom.write_byte(0x20a34,0xc4) #8:4a34    
    rom.write_byte(0x20a35,0x41) #8:4a35    
    rom.write_byte(0x20a36,0x3e) #8:4a36    ld a,23
    rom.write_byte(0x20a37,0x23) #8:4a37    
    rom.write_byte(0x20a38,0xc3) #8:4a38    jp 418A
    rom.write_byte(0x20a39,0x8a) #8:4a39    
    rom.write_byte(0x20a3a,0x41) #8:4a3a    
    #--
    rom.write_byte(0x20aec,0xfa) #8:4aec    ld a,(A40D)
    rom.write_byte(0x20aed,0x0d) #8:4aed    
    rom.write_byte(0x20aee,0xa4) #8:4aee    
    rom.write_byte(0x20aef,0xa7) #8:4aef    and a
    rom.write_byte(0x20af0,0xca) #8:4af0    jp z,41C4
    rom.write_byte(0x20af1,0xc4) #8:4af1    
    rom.write_byte(0x20af2,0x41) #8:4af2    
    rom.write_byte(0x20af3,0x3e) #8:4af3    ld a,23
    rom.write_byte(0x20af4,0x23) #8:4af4    
    rom.write_byte(0x20af5,0xc3) #8:4af5    jp 418A
    rom.write_byte(0x20af6,0x8a) #8:4af6    
    rom.write_byte(0x20af7,0x41) #8:4af7    
    #--
    rom.write_byte(0x20b46,0xfa) #8:4b46    ld a,(A40E)
    rom.write_byte(0x20b47,0x0e) #8:4b47    
    rom.write_byte(0x20b48,0xa4) #8:4b48    
    rom.write_byte(0x20b49,0xa7) #8:4b49    and a
    rom.write_byte(0x20b4a,0xca) #8:4b4a    jp z,41C4
    rom.write_byte(0x20b4b,0xc4) #8:4b4b    
    rom.write_byte(0x20b4c,0x41) #8:4b4c    
    rom.write_byte(0x20b4d,0x3e) #8:4b4d    ld a,23
    rom.write_byte(0x20b4e,0x23) #8:4b4e    
    rom.write_byte(0x20b4f,0xc3) #8:4b4f    jp 418A
    rom.write_byte(0x20b50,0x8a) #8:4b50    
    rom.write_byte(0x20b51,0x41) #8:4b51    
    #--
    rom.write_byte(0x20b52,0xfa) #8:4b52    ld a,(A40F)
    rom.write_byte(0x20b53,0x0f) #8:4b53    
    rom.write_byte(0x20b54,0xa4) #8:4b54    
    rom.write_byte(0x20b55,0xa7) #8:4b55    and a
    rom.write_byte(0x20b56,0xca) #8:4b56    jp z,41C4
    rom.write_byte(0x20b57,0xc4) #8:4b57    
    rom.write_byte(0x20b58,0x41) #8:4b58    
    rom.write_byte(0x20b59,0x3e) #8:4b59    ld a,23
    rom.write_byte(0x20b5a,0x23) #8:4b5a    
    rom.write_byte(0x20b5b,0xc3) #8:4b5b    jp 418A
    rom.write_byte(0x20b5c,0x8a) #8:4b5c    
    rom.write_byte(0x20b5d,0x41) #8:4b5d    
    #--
    rom.write_byte(0x20b5e,0xca) #8:4b5e    jp z,41C4
    rom.write_byte(0x20b5f,0xc4) #8:4b5f    
    rom.write_byte(0x20b60,0x41) #8:4b60    

def patch_world_movement(rom):
    # Block boss level entry
    rom.write_byte(0x21d76,0xc3) #8:5d76    jp 7f18
    rom.write_byte(0x21d77,0x18) #8:5d77    
    rom.write_byte(0x21d78,0x7f) #8:5d78    
    #--
    rom.write_byte(0x23f18,0xfa) #8:7f18    ld a,(A79E)
    rom.write_byte(0x23f19,0x9e) #8:7f19    
    rom.write_byte(0x23f1a,0xa7) #8:7f1a    
    rom.write_byte(0x23f1b,0xfe) #8:7f1b    cp a,19
    rom.write_byte(0x23f1c,0x19) #8:7f1c
    rom.write_byte(0x23f1d,0xfa) #8:7f1d    ld a,(A421)
    rom.write_byte(0x23f1e,0x21) #8:7f1e
    rom.write_byte(0x23f1f,0xa4) #8:7f1f
    rom.write_byte(0x23f20,0xca) #8:7f20    jp z, 7F67
    rom.write_byte(0x23f21,0x67) #8:7f21
    rom.write_byte(0x23f22,0x7f) #8:7f22
    rom.write_byte(0x23f23,0xfa) #8:7f23    ld a,(A79E)
    rom.write_byte(0x23f24,0x9e) #8:7f24
    rom.write_byte(0x23f25,0xa7) #8:7f25
    rom.write_byte(0x23f26,0xfe) #8:7f26    cp a,0A
    rom.write_byte(0x23f27,0x0a) #8:7f27
    rom.write_byte(0x23f28,0xfa) #8:7f28    ld a,(A422)
    rom.write_byte(0x23f29,0x22) #8:7f29
    rom.write_byte(0x23f2a,0xa4) #8:7f2a
    rom.write_byte(0x23f2b,0xca) #8:7f2b    jp z, 7F67
    rom.write_byte(0x23f2c,0x67) #8:7f2c
    rom.write_byte(0x23f2d,0x7f) #8:7f2d
    rom.write_byte(0x23f2e,0xfa) #8:7f2e    ld a,(A79E)
    rom.write_byte(0x23f2f,0x9e) #8:7f2f
    rom.write_byte(0x23f30,0xa7) #8:7f30
    rom.write_byte(0x23f31,0xfe) #8:7f31    cp a,18
    rom.write_byte(0x23f32,0x18) #8:7f32
    rom.write_byte(0x23f33,0xfa) #8:7f33    ld a,(A426)
    rom.write_byte(0x23f34,0x26) #8:7f34
    rom.write_byte(0x23f35,0xa4) #8:7f35
    rom.write_byte(0x23f36,0xca) #8:7f36    jp z, 7F67
    rom.write_byte(0x23f37,0x67) #8:7f37
    rom.write_byte(0x23f38,0x7f) #8:7f38
    rom.write_byte(0x23f39,0xfa) #8:7f39    ld a,(A79E)
    rom.write_byte(0x23f3a,0x9e) #8:7f3a
    rom.write_byte(0x23f3b,0xa7) #8:7f3b
    rom.write_byte(0x23f3c,0xfe) #8:7f3c    cp a,1C
    rom.write_byte(0x23f3d,0x1c) #8:7f3d
    rom.write_byte(0x23f3e,0xfa) #8:7f3e    ld a,(A423)
    rom.write_byte(0x23f3f,0x23) #8:7f3f
    rom.write_byte(0x23f40,0xa4) #8:7f40
    rom.write_byte(0x23f41,0xca) #8:7f41    jp z, 7F67
    rom.write_byte(0x23f42,0x67) #8:7f42
    rom.write_byte(0x23f43,0x7f) #8:7f43
    rom.write_byte(0x23f44,0xfa) #8:7f44    ld a,(A79E)
    rom.write_byte(0x23f45,0x9e) #8:7f45
    rom.write_byte(0x23f46,0xa7) #8:7f46
    rom.write_byte(0x23f47,0xfe) #8:7f47    cp a,14
    rom.write_byte(0x23f48,0x14) #8:7f48
    rom.write_byte(0x23f49,0xfa) #8:7f49    ld a,(A425)
    rom.write_byte(0x23f4a,0x25) #8:7f4a
    rom.write_byte(0x23f4b,0xa4) #8:7f4b
    rom.write_byte(0x23f4c,0xca) #8:7f4c    jp z, 7F67
    rom.write_byte(0x23f4d,0x67) #8:7f4d
    rom.write_byte(0x23f4e,0x7f) #8:7f4e
    rom.write_byte(0x23f4f,0xfa) #8:7f4f    ld a,(A79E)
    rom.write_byte(0x23f50,0x9e) #8:7f50
    rom.write_byte(0x23f51,0xa7) #8:7f51
    rom.write_byte(0x23f52,0xfe) #8:7f52    cp a,1A
    rom.write_byte(0x23f53,0x1a) #8:7f53
    rom.write_byte(0x23f54,0xfa) #8:7f54    ld a,(A424)
    rom.write_byte(0x23f55,0x24) #8:7f55
    rom.write_byte(0x23f56,0xa4) #8:7f56
    rom.write_byte(0x23f57,0xca) #8:7f57    jp z, 7F67
    rom.write_byte(0x23f58,0x67) #8:7f58
    rom.write_byte(0x23f59,0x7f) #8:7f59
    rom.write_byte(0x23f5a,0xfa) #8:7f5a    ld a,(A79E)
    rom.write_byte(0x23f5b,0x9e) #8:7f5b
    rom.write_byte(0x23f5c,0xa7) #8:7f5c
    rom.write_byte(0x23f5d,0xfe) #8:7f5d    cp a,28
    rom.write_byte(0x23f5e,0x28) #8:7f5e
    rom.write_byte(0x23f5f,0xfa) #8:7f5f    ld a,(A427)
    rom.write_byte(0x23f60,0x27) #8:7f60
    rom.write_byte(0x23f61,0xa4) #8:7f61
    rom.write_byte(0x23f62,0xca) #8:7f62    jp z, 7F67
    rom.write_byte(0x23f63,0x67) #8:7f63
    rom.write_byte(0x23f64,0x7f) #8:7f64
    rom.write_byte(0x23f65,0x3e) #8:7f65    ld a,1
    rom.write_byte(0x23f66,0x01) #8:7f66
    rom.write_byte(0x23f67,0xa7) #8:7f67    and a
    rom.write_byte(0x23f68,0xca) #8:7f68    jp z, 7F73
    rom.write_byte(0x23f69,0x73) #8:7f69
    rom.write_byte(0x23f6a,0x7f) #8:7f6a
    rom.write_byte(0x23f6b,0x3e) #8:7f6b    ld a,2b
    rom.write_byte(0x23f6c,0x2b) #8:7f6c
    rom.write_byte(0x23f6d,0xea) #8:7f6d    ld (A61C),a
    rom.write_byte(0x23f6e,0x1c) #8:7f6e
    rom.write_byte(0x23f6f,0xa6) #8:7f6f
    rom.write_byte(0x23f70,0xc3) #8:7f70    jp 5D79
    rom.write_byte(0x23f71,0x79) #8:7f71
    rom.write_byte(0x23f72,0x5d) #8:7f72
    rom.write_byte(0x23f73,0xc3) #8:7f73    jp 5D7D
    rom.write_byte(0x23f74,0x7d) #8:7f74
    rom.write_byte(0x23f75,0x5d) #8:7f75

    # Overworld movement

    # Rice beach
    rom.write_byte(0x22320,0x1a) #8:6320    ld a,(A41A)
    rom.write_byte(0x22321,0xa4) #8:6321    
    # Mt teapot
    rom.write_byte(0x22333,0x1b) #8:6333    ld a,(A41B)
    rom.write_byte(0x22334,0xa4) #8:6334    
    # Stove canyon
    rom.write_byte(0x22346,0x1c) #8:6346    ld a,(A41C)
    rom.write_byte(0x22347,0xa4) #8:6347    
    # Ss teacup
    rom.write_byte(0x22359,0x1d) #8:6359    ld a,(A41D)
    rom.write_byte(0x2235a,0xa4) #8:635a    
    # Parsley woods
    rom.write_byte(0x2236c,0x1e) #8:636c    ld a,(A41E)
    rom.write_byte(0x2236d,0xa4) #8:636d    
    # Sherbet land
    rom.write_byte(0x2237f,0x1f) #8:637f    ld a,(A41F)
    rom.write_byte(0x22380,0xa4) #8:6380    
    # Syrup castle
    rom.write_byte(0x22392,0x20) #8:6392    ld a,(A420)
    rom.write_byte(0x22393,0xa4) #8:6393    

    # Subworld movement

    # Rice beach
    rom.write_byte(0x22416,0x13) #8:6416    ld a,(A413)
    rom.write_byte(0x22417,0xa4) #8:6417    
    # Mt teapot
    rom.write_byte(0x22407,0x14) #8:6407    ld a,(A414)
    rom.write_byte(0x22408,0xa4) #8:6408    
    # Stove canyon
    rom.write_byte(0x223f8,0x15) #8:63f8    ld a,(A415)
    rom.write_byte(0x223f9,0xa4) #8:63f9    
    # Ss teacup
    rom.write_byte(0x223e9,0x16) #8:63e9    ld a,(A416)
    rom.write_byte(0x223ea,0xa4) #8:63ea    
    # Parsley woods
    rom.write_byte(0x223da,0x17) #8:63da    ld a,(A417)
    rom.write_byte(0x223db,0xa4) #8:63db    
    # Sherbet land
    rom.write_byte(0x223cb,0x18) #8:63cb    ld a,(A418)
    rom.write_byte(0x223cc,0xa4) #8:63cc    
    # Syrup castle
    rom.write_byte(0x223bc,0x19) #8:63bc    ld a,(A419)
    rom.write_byte(0x223bd,0xa4) #8:63bd
    return

# Fix bugs that appear due to changes in game structure
def apply_fixes(rom):
    # Fix syrup castle cutscene
    rom.write_byte(0x23af3,0xc1) #8:7af3    ld a,(46C1)
    rom.write_byte(0x23af4,0x46) #8:7af4    
    rom.write_byte(0x23b21,0xc1) #8:7b21    ld a,(46C1)
    rom.write_byte(0x23b22,0x46) #8:7b22

    # Fix parsley woods overworld movement
    rom.write_byte(0x20177,0xfa) #8:4177    ld a,(43C9)
    rom.write_byte(0x20178,0xc9) #8:4178   
    rom.write_byte(0x20179,0x43) #8:4179
    return

# Turn autoscrollers into normal scrolling screens
def remove_autoscrolling(rom):
    rom.write_byte(0x31d19,0x1) #c:5d19
    rom.write_byte(0x31d49,0x1) #c:5d49
    rom.write_byte(0x32b89,0x1) #c:6b89
    rom.write_byte(0x32bb9,0x1) #c:6bb9

# Force max speed value for post-level bonus select
def speedups(rom):
    rom.write_byte(0x465e,0x3e) #1:465e     ld a,ff
    rom.write_byte(0x465f,0xff) #1:465f     
    rom.write_byte(0x4660,0x00) #1:4660     nop

# Block player from using saveslot 3, repurposed for multiworld save data
def remove_saveslot_three(rom):
    rom.write_byte(0x74a5,0xcd) #1:74a5     call 7B82
    rom.write_byte(0x74a6,0x82) #1:74a6
    rom.write_byte(0x74a7,0x7b) #1:74a7
    rom.write_byte(0x7b82,0xfe) #1:7b82     cp a,02
    rom.write_byte(0x7b83,0x02) #1:7b83     
    rom.write_byte(0x7b84,0xc2) #1:7b84     jp nz, 7B89
    rom.write_byte(0x7b85,0x89) #1:7b85     
    rom.write_byte(0x7b86,0x7b) #1:7b86     
    rom.write_byte(0x7b87,0x3e) #1:7b87     ld a,01
    rom.write_byte(0x7b88,0x01) #1:7b88     
    rom.write_byte(0x7b89,0xea) #1:7b89     ld (A0C3),a
    rom.write_byte(0x7b8a,0xc3) #1:7b8a     
    rom.write_byte(0x7b8b,0xa0) #1:7b8b     
    rom.write_byte(0x7b8c,0xc9) #1:7b8c     ret

# Fix internal checksums
def fix_checksum(rom):
    # Header checksum first
    checksum=0
    for c in rom.buffer[0x134:0x14D]:
        checksum -= c + 1
    rom.write_byte(0x14D,checksum & 0xFF)

    # Clear ROM checksum bytes before calculation
    rom.buffer[0x14E] = 0
    rom.buffer[0x14F] = 0
    checksum = 0
    for byte in rom.buffer:
            checksum+=byte
    checksum_b1=(checksum >> 8) & 0xFF
    checksum_b2=(checksum) & 0xFF
    rom.write_byte(0x14E,checksum_b1)
    rom.write_byte(0x14F,checksum_b2)

def custom_level_table(rom):
    # Patch level exit value
    rom.write_byte(0x04a9f,0x9e) #1:4a9f    ld a,(A79E)
    rom.write_byte(0x04aa0,0xa7) #1:4aa0    

    # Hook into level loading method
    rom.write_byte(0x21dac,0xcd) #8:5dac    call 7EDF
    rom.write_byte(0x21dad,0xdf) #8:5dad    
    rom.write_byte(0x21dae,0x7e) #8:5dae    

    rom.write_byte(0x23edf,0xfa) #8:7edf    ld a,(A79E)
    rom.write_byte(0x23ee0,0x9e) #8:7ee0    
    rom.write_byte(0x23ee1,0xa7) #8:7ee1    
    rom.write_byte(0x23ee2,0x4f) #8:7ee2    ld c,a
    rom.write_byte(0x23ee3,0x06) #8:7ee3    ld b,00
    rom.write_byte(0x23ee4,0x00) #8:7ee4    
    rom.write_byte(0x23ee5,0x21) #8:7ee5    ld hl,7EEB
    rom.write_byte(0x23ee6,0xeb) #8:7ee6    
    rom.write_byte(0x23ee7,0x7e) #8:7ee7    
    rom.write_byte(0x23ee8,0x09) #8:7ee8    add hl,bc
    rom.write_byte(0x23ee9,0x7e) #8:7ee9    ld a,[hl]
    rom.write_byte(0x23eea,0xc9) #8:7eea    ret

    # Start of custom level table
    rom.write_byte(0x23eeb,0x00) #8:7eeb
    rom.write_byte(0x23eec,0x01) #8:7eec
    rom.write_byte(0x23eed,0x02) #8:7eed
    rom.write_byte(0x23eee,0x03) #8:7eee
    rom.write_byte(0x23eef,0x04) #8:7eef
    rom.write_byte(0x23ef0,0x05) #8:7ef0
    rom.write_byte(0x23ef1,0x06) #8:7ef1
    rom.write_byte(0x23ef2,0x07) #8:7ef2
    rom.write_byte(0x23ef3,0x08) #8:7ef3
    rom.write_byte(0x23ef4,0x09) #8:7ef4
    rom.write_byte(0x23ef5,0x0a) #8:7ef5
    rom.write_byte(0x23ef6,0x0b) #8:7ef6
    rom.write_byte(0x23ef7,0x0c) #8:7ef7
    rom.write_byte(0x23ef8,0x0d) #8:7ef8
    rom.write_byte(0x23ef9,0x0e) #8:7ef9
    rom.write_byte(0x23efa,0x0f) #8:7efa
    rom.write_byte(0x23efb,0x10) #8:7efb
    rom.write_byte(0x23efc,0x11) #8:7efc
    rom.write_byte(0x23efd,0x12) #8:7efd
    rom.write_byte(0x23efe,0x13) #8:7efe
    rom.write_byte(0x23eff,0x14) #8:7eff
    rom.write_byte(0x23f00,0x15) #8:7f00
    rom.write_byte(0x23f01,0x16) #8:7f01
    rom.write_byte(0x23f02,0x17) #8:7f02
    rom.write_byte(0x23f03,0x18) #8:7f03
    rom.write_byte(0x23f04,0x19) #8:7f04
    rom.write_byte(0x23f05,0x1a) #8:7f05
    rom.write_byte(0x23f06,0x1b) #8:7f06
    rom.write_byte(0x23f07,0x1c) #8:7f07
    rom.write_byte(0x23f08,0x1d) #8:7f08
    rom.write_byte(0x23f09,0x1e) #8:7f09
    rom.write_byte(0x23f0a,0x1f) #8:7f0a
    rom.write_byte(0x23f0b,0x20) #8:7f0b
    rom.write_byte(0x23f0c,0x21) #8:7f0c
    rom.write_byte(0x23f0d,0x22) #8:7f0d
    rom.write_byte(0x23f0e,0x23) #8:7f0e
    rom.write_byte(0x23f0f,0x24) #8:7f0f
    rom.write_byte(0x23f10,0x25) #8:7f10
    rom.write_byte(0x23f11,0x26) #8:7f11
    rom.write_byte(0x23f12,0x27) #8:7f12
    rom.write_byte(0x23f13,0x28) #8:7f13
    rom.write_byte(0x23f14,0x29) #8:7f14
    rom.write_byte(0x23f15,0x2A) #8:7f15
    rom.write_byte(0x23f16,0x2B) #8:7f16     
    # End of custom level table

# Shuffles the level music in vanilla limitations
def shuffle_music(rom):
    level_music=[0x03,0x04,0x09,0x0A,0x0B,0x0E,0x10,0x16,0x17,0x1B,0x1E,0x22,0x27]
    shuffled_level_music=random.shuffle(level_music)
    level_music_addr=[0x33ECD,0x33ED9,0x33EE5,0x33EF1,0x33EFD,0x33F09,0x33F15,0x33F21,0x33F2D,0x33F39,0x33F45,0x33F51,0x33F5D]
    # Second address always + 0x03 away
    for music_offset in level_music_addr:
        music_pick=shuffled_level_music.pop()
        rom.write_byte(music_offset,music_pick)
        rom.write_byte(music_offset+0x03,music_pick)

def new_feature(rom):
    rom.write_byte(0x153a,0xc3) #0:153a jp 3C00
    rom.write_byte(0x153b,0x00) #0:153b
    rom.write_byte(0x153c,0x3c) #0:153c
    rom.write_byte(0x3c00,0xfa) #0:3c00 ld a,(A918)
    rom.write_byte(0x3c01,0x18) #0:3c01
    rom.write_byte(0x3c02,0xa9) #0:3c02
    rom.write_byte(0x3c03,0xea) #0:3c03 ld (A4F0),a
    rom.write_byte(0x3c04,0xf0) #0:3c04
    rom.write_byte(0x3c05,0xa4) #0:3c05
    rom.write_byte(0x3c06,0x67) #0:3c06 ld h,a
    rom.write_byte(0x3c07,0xfa) #0:3c07 ld a,(A919)
    rom.write_byte(0x3c08,0x19) #0:3c08
    rom.write_byte(0x3c09,0xa9) #0:3c09
    rom.write_byte(0x3c0a,0xea) #0:3c0a ld (A4F1),a
    rom.write_byte(0x3c0b,0xf1) #0:3c0b
    rom.write_byte(0x3c0c,0xa4) #0:3c0c
    rom.write_byte(0x3c0d,0x6f) #0:3c0d ld l,a
    rom.write_byte(0x3c0e,0xc3) #0:3c0e jp 1542
    rom.write_byte(0x3c0f,0x42) #0:3c0f
    rom.write_byte(0x3c10,0x15) #0:3c10

def patch_rom(world, rom, player):

    # Starting Life Count, hex equals displayed value directly
    rom.write_byte(0x7B7D, bytes.fromhex(str(world.starting_life_count[player].value))[0])

    patch_basic_abilities(rom)
    patch_powerups(rom)
    patch_world_movement(rom)
    speedups(rom)
    apply_fixes(rom)
    patch_world_enter(rom)
    
    # TODO: Add option for new feature
    new_feature(rom)
    
    if world.remove_autoscrollers[player]:
        remove_autoscrolling(rom)
    if world.music_shuffle[player]:
        shuffle_music(rom)

    # TODO: This patch is not required until level shuffle mode exists
    #custom_level_table(rom)
    # TODO: this is broken on gambatte but works fine on bgb, no idea why :(
    #remove_saveslot_three(rom)

    from Utils import __version__
    rom.name = bytearray(f'WL{__version__.replace(".", "")[0:3]}_{player}_{world.seed:11}\0', 'utf8')[:21]
    rom.name.extend([0] * (21 - len(rom.name)))

    player_name_length=0
    # Write slot info to ROM
    for i, byte in enumerate(world.player_name[player].encode("utf-8")):
        rom.write_byte(0x674B1+i, byte)
        player_name_length+=1
    rom.write_byte(0x674B0, player_name_length)

    # Re-write header title
    new_title="WARIOLANDAP"
    for i, byte in enumerate(new_title.encode("utf-8")):
        rom.write_byte(0x134+i,byte)
        
    for i in range(5):
        rom.write_byte(0x13F+i,0x00)
    # Fix checksums so emulators don't complain
    fix_checksum(rom)