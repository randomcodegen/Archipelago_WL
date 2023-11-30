import hashlib
import os
import math
import Utils
import bsdiff4
from worlds.Files import APDeltaPatch
from BaseClasses import MultiWorld

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
    rom.write_byte(0x34a1b,0xc3) #d:4a1b    jp 7B00
    rom.write_byte(0x34a1c,0x00) #d:4a1c
    rom.write_byte(0x34a1d,0x7b) #d:4a1d
    #---
    rom.write_byte(0x37b00,0xea) #d:7b00    ld (A490),a
    rom.write_byte(0x37b01,0x90) #d:7b01
    rom.write_byte(0x37b02,0xa4) #d:7b02
    rom.write_byte(0x37b03,0xfa) #d:7b03    ld a,(A407)
    rom.write_byte(0x37b04,0x07) #d:7b04
    rom.write_byte(0x37b05,0xa4) #d:7b05
    rom.write_byte(0x37b06,0xa7) #d:7b06    and a
    rom.write_byte(0x37b07,0x28) #d:7b07    jr z,06
    rom.write_byte(0x37b08,0x06) #d:7b08
    rom.write_byte(0x37b09,0xfa) #d:7b09    ld a,(A490)
    rom.write_byte(0x37b0a,0x90) #d:7b0a
    rom.write_byte(0x37b0b,0xa4) #d:7b0b
    rom.write_byte(0x37b0c,0xc3) #d:7b0c    jp 4A1E
    rom.write_byte(0x37b0d,0x1e) #d:7b0d
    rom.write_byte(0x37b0e,0x4a) #d:7b0e
    rom.write_byte(0x37b0f,0xc3) #d:7b0f    jp 4A3D
    rom.write_byte(0x37b10,0x3d) #d:7b10
    rom.write_byte(0x37b11,0x4a) #d:7b11

    # Duck
    rom.write_byte(0x34c5a,0xcd) #d:4c5a    call 7B13
    rom.write_byte(0x34c5b,0x13) #d:4c5b
    rom.write_byte(0x34c5c,0x7b) #d:4c5c
    rom.write_byte(0x34a7c,0xcd) #d:4a7c    call 7B13
    rom.write_byte(0x34a7d,0x13) #d:4a7d
    rom.write_byte(0x34a7e,0x7b) #d:4a7e
    rom.write_byte(0x3504a,0xcd) #d:504a    call 7B13
    rom.write_byte(0x3504b,0x13) #d:504b
    rom.write_byte(0x3504c,0x7b) #d:504c
    rom.write_byte(0x35fa2,0xc3) #d:5fa2    jp 7B8E
    rom.write_byte(0x35fa3,0x8e) #d:5fa3
    rom.write_byte(0x35fa4,0x7b) #d:5fa4
    #---quicksand duck hook
    rom.write_byte(0x37b8e,0xfa) #d:7b8e    ld a,(A408)
    rom.write_byte(0x37b8f,0x08) #d:7b8f
    rom.write_byte(0x37b90,0xa4) #d:7b90
    rom.write_byte(0x37b91,0xa7) #d:7b91    and a
    rom.write_byte(0x37b92,0x20) #d:7b92    jr nz,03
    rom.write_byte(0x37b93,0x03) #d:7b93
    rom.write_byte(0x37b94,0xc3) #d:7b94    jp 5FB4
    rom.write_byte(0x37b95,0xb4) #d:7b95
    rom.write_byte(0x37b96,0x5f) #d:7b96
    rom.write_byte(0x37b97,0x3e) #d:7b97    ld a,01
    rom.write_byte(0x37b98,0x01) #d:7b98
    rom.write_byte(0x37b99,0xea) #d:7b99    ld (A93E),a
    rom.write_byte(0x37b9a,0x3e) #d:7b9a
    rom.write_byte(0x37b9b,0xa9) #d:7b9b
    rom.write_byte(0x37b9c,0xc3) #d:7b9c    jp 5FA5
    rom.write_byte(0x37b9d,0xa5) #d:7b9d
    rom.write_byte(0x37b9e,0x5f) #d:7b9e
    #---normal duck hook
    rom.write_byte(0x37b13,0xfa) #d:7b13    ld a,(A408)
    rom.write_byte(0x37b14,0x08) #d:7b14
    rom.write_byte(0x37b15,0xa4) #d:7b15
    rom.write_byte(0x37b16,0xa7) #d:7b16    and a
    rom.write_byte(0x37b17,0x28) #d:7b17    jr z,04
    rom.write_byte(0x37b18,0x04) #d:7b18
    rom.write_byte(0x37b19,0xfa) #d:7b19    ld a,(A956)
    rom.write_byte(0x37b1a,0x56) #d:7b1a
    rom.write_byte(0x37b1b,0xa9) #d:7b1b
    rom.write_byte(0x37b1c,0xc9) #d:7b1c    ret
    rom.write_byte(0x37b1d,0x3e) #d:7b1d    ld a,01
    rom.write_byte(0x37b1e,0x01) #d:7b1e
    rom.write_byte(0x37b1f,0xc9) #d:7b1f    ret

    # High jump
    rom.write_byte(0x34e75,0xcd) #d:4e75    call 7B22
    rom.write_byte(0x34e76,0x22) #d:4e76
    rom.write_byte(0x34e77,0x7b) #d:4e77
    #---
    rom.write_byte(0x37b22,0xfa) #d:7b22    ld a,(A405)
    rom.write_byte(0x37b23,0x05) #d:7b23
    rom.write_byte(0x37b24,0xa4) #d:7b24
    rom.write_byte(0x37b25,0xea) #d:7b25    ld (A92C),a
    rom.write_byte(0x37b26,0x2c) #d:7b26
    rom.write_byte(0x37b27,0xa9) #d:7b27
    rom.write_byte(0x37b28,0xc9) #d:7b28    ret

    # Dash
    rom.write_byte(0x35bd3,0xcd) #d:5bd3    call 7B29
    rom.write_byte(0x35bd4,0x29) #d:5bd4
    rom.write_byte(0x35bd5,0x7b) #d:5bd5
    #---
    rom.write_byte(0x37b29,0xfa) #d:7b29    ld a,(A404)
    rom.write_byte(0x37b2a,0x04) #d:7b2a
    rom.write_byte(0x37b2b,0xa4) #d:7b2b
    rom.write_byte(0x37b2c,0xa7) #d:7b2c    and a
    rom.write_byte(0x37b2d,0x28) #d:7b2d    jr z,04
    rom.write_byte(0x37b2e,0x04) #d:7b2e
    rom.write_byte(0x37b2f,0xfa) #d:7b2f    ld a,(A34D)
    rom.write_byte(0x37b30,0x4d) #d:7b30
    rom.write_byte(0x37b31,0xa3) #d:7b31
    rom.write_byte(0x37b32,0xc9) #d:7b32    ret
    rom.write_byte(0x37b33,0x3e) #d:7b33    ld a,01
    rom.write_byte(0x37b34,0x01) #d:7b34
    rom.write_byte(0x37b35,0xc9) #d:7b35    ret

    # Create coin
    rom.write_byte(0x34b74,0xcd) #d:4b74    call 7B36
    rom.write_byte(0x34b75,0x36) #d:4b75
    rom.write_byte(0x34b76,0x7b) #d:4b76
    #---
    rom.write_byte(0x37b36,0xfa) #d:7b36    ld a,(A406)
    rom.write_byte(0x37b37,0x06) #d:7b37
    rom.write_byte(0x37b38,0xa4) #d:7b38
    rom.write_byte(0x37b39,0xa7) #d:7b39    and a
    rom.write_byte(0x37b3a,0x28) #d:7b3a    jr z,04
    rom.write_byte(0x37b3b,0x04) #d:7b3b
    rom.write_byte(0x37b3c,0xfa) #d:7b3c    ld a,(A9A4)
    rom.write_byte(0x37b3d,0xa4) #d:7b3d
    rom.write_byte(0x37b3e,0xa9) #d:7b3e
    rom.write_byte(0x37b3f,0xc9) #d:7b3f    ret
    rom.write_byte(0x37b40,0x3e) #d:7b40    ld a,01
    rom.write_byte(0x37b41,0x01) #d:7b41
    rom.write_byte(0x37b42,0xc9) #d:7b42    ret

    # Force small wario
    rom.write_byte(0xec4,0xcd) #0:ec4   call 7F65
    rom.write_byte(0xec5,0x65) #0:ec5
    rom.write_byte(0xec6,0x7f) #0:ec6
    #---
    rom.write_byte(0x33f65,0xfa) #c:7f65    ld a,(A410)
    rom.write_byte(0x33f66,0x10) #c:7f66
    rom.write_byte(0x33f67,0xa4) #c:7f67
    rom.write_byte(0x33f68,0xa7) #c:7f68    and a
    rom.write_byte(0x33f69,0x20) #c:7f69    jr nz, 3
    rom.write_byte(0x33f6a,0x03) #c:7f6a
    rom.write_byte(0x33f6b,0xea) #c:7f6b    ld (A80A),a
    rom.write_byte(0x33f6c,0x0a) #c:7f6c
    rom.write_byte(0x33f6d,0xa8) #c:7f6d
    rom.write_byte(0x33f6e,0xfa) #c:7f6e    ld a, (A80A)
    rom.write_byte(0x33f6f,0x0a) #c:7f6f
    rom.write_byte(0x33f70,0xa8) #c:7f70
    rom.write_byte(0x33f71,0xc9) #c:7f71    ret
    return

# Block powerup usage
def patch_powerups(rom):
    rom.write_byte(0x364b2,0xc3) #d:64b2    jp 7B43
    rom.write_byte(0x364b3,0x43) #d:64b3
    rom.write_byte(0x364b4,0x7b) #d:64b4
    #---
    rom.write_byte(0x37b43,0xea) #d:7b43    ld (A958),a
    rom.write_byte(0x37b44,0x58) #d:7b44
    rom.write_byte(0x37b45,0xa9) #d:7b45
    rom.write_byte(0x37b46,0xfe) #d:7b46    cp a,04
    rom.write_byte(0x37b47,0x04) #d:7b47
    rom.write_byte(0x37b48,0xd2) #d:7b48    jp nc, 7B81
    rom.write_byte(0x37b49,0x81) #d:7b49
    rom.write_byte(0x37b4a,0x7b) #d:7b4a
    rom.write_byte(0x37b4b,0xfe) #d:7b4b    cp a,03
    rom.write_byte(0x37b4c,0x03) #d:7b4c
    rom.write_byte(0x37b4d,0xd2) #d:7b4d    jp nc, 7B75
    rom.write_byte(0x37b4e,0x75) #d:7b4e
    rom.write_byte(0x37b4f,0x7b) #d:7b4f
    rom.write_byte(0x37b50,0xfe) #d:7b50    cp a,02
    rom.write_byte(0x37b51,0x02) #d:7b51
    rom.write_byte(0x37b52,0xd2) #d:7b52    jp nc, 7B69
    rom.write_byte(0x37b53,0x69) #d:7b53
    rom.write_byte(0x37b54,0x7b) #d:7b54
    rom.write_byte(0x37b55,0xfe) #d:7b55    cp a,01
    rom.write_byte(0x37b56,0x01) #d:7b56
    rom.write_byte(0x37b57,0xd2) #d:7b57    jp nc, 7B5D
    rom.write_byte(0x37b58,0x5d) #d:7b58
    rom.write_byte(0x37b59,0x7b) #d:7b59
    rom.write_byte(0x37b5a,0xc3) #d:7b5a    jp 64B5
    rom.write_byte(0x37b5b,0xb5) #d:7b5b
    rom.write_byte(0x37b5c,0x64) #d:7b5c
    #--Check garlic
    rom.write_byte(0x37b5d,0xfa) #d:7b5d    ld a,(A400)
    rom.write_byte(0x37b5e,0x00) #d:7b5e
    rom.write_byte(0x37b5f,0xa4) #d:7b5f
    rom.write_byte(0x37b60,0xa7) #d:7b60    and a
    rom.write_byte(0x37b61,0xca) #d:7b61    jp z,6261
    rom.write_byte(0x37b62,0x61) #d:7b62
    rom.write_byte(0x37b63,0x62) #d:7b63
    rom.write_byte(0x37b64,0x3e) #d:7b64    ld a,01
    rom.write_byte(0x37b65,0x01) #d:7b65
    rom.write_byte(0x37b66,0xc3) #d:7b66    jp 64B5
    rom.write_byte(0x37b67,0xb5) #d:7b67
    rom.write_byte(0x37b68,0x64) #d:7b68
    #--Check bull
    rom.write_byte(0x37b69,0xfa) #d:7b69    ld a,(A401)
    rom.write_byte(0x37b6a,0x01) #d:7b6a
    rom.write_byte(0x37b6b,0xa4) #d:7b6b
    rom.write_byte(0x37b6c,0xa7) #d:7b6c    and a
    rom.write_byte(0x37b6d,0xca) #d:7b6d    jp z,6261
    rom.write_byte(0x37b6e,0x61) #d:7b6e
    rom.write_byte(0x37b6f,0x62) #d:7b6f
    rom.write_byte(0x37b70,0x3e) #d:7b70    ld a,02
    rom.write_byte(0x37b71,0x02) #d:7b71
    rom.write_byte(0x37b72,0xc3) #d:7b72    jp 64B5
    rom.write_byte(0x37b73,0xb5) #d:7b73
    rom.write_byte(0x37b74,0x64) #d:7b74
    #--Check jet
    rom.write_byte(0x37b75,0xfa) #d:7b75    ld a,(A402)
    rom.write_byte(0x37b76,0x02) #d:7b76
    rom.write_byte(0x37b77,0xa4) #d:7b77
    rom.write_byte(0x37b78,0xa7) #d:7b78    and a
    rom.write_byte(0x37b79,0xca) #d:7b79    jp z,6261
    rom.write_byte(0x37b7a,0x61) #d:7b7a
    rom.write_byte(0x37b7b,0x62) #d:7b7b
    rom.write_byte(0x37b7c,0x3e) #d:7b7c    ld a,03
    rom.write_byte(0x37b7d,0x03) #d:7b7d
    rom.write_byte(0x37b7e,0xc3) #d:7b7e    jp 64B5
    rom.write_byte(0x37b7f,0xb5) #d:7b7f
    rom.write_byte(0x37b80,0x64) #d:7b80
    #--Check dragon
    rom.write_byte(0x37b81,0xfa) #d:7b81    ld a,(A403)
    rom.write_byte(0x37b82,0x03) #d:7b82
    rom.write_byte(0x37b83,0xa4) #d:7b83
    rom.write_byte(0x37b84,0xa7) #d:7b84    and a
    rom.write_byte(0x37b85,0xca) #d:7b85    jp z,6261
    rom.write_byte(0x37b86,0x61) #d:7b86
    rom.write_byte(0x37b87,0x62) #d:7b87
    rom.write_byte(0x37b88,0xfa) #d:7b88    ld (A958),a
    rom.write_byte(0x37b89,0x58) #d:7b89
    rom.write_byte(0x37b8a,0xa9) #d:7b8a
    rom.write_byte(0x37b8b,0xc3) #d:7b8b    jp 64B5
    rom.write_byte(0x37b8c,0xb5) #d:7b8c
    rom.write_byte(0x37b8d,0x64) #d:7b8d
    return

# Patch Map Movement
def patch_world_enter(rom):
    # Block world entering
    rom.write_byte(0x20187,0xc3) #8:4187    jp 7EE1
    rom.write_byte(0x20188,0xe1) #8:4188
    rom.write_byte(0x20189,0x7e) #8:4189
    #--
    rom.write_byte(0x23ee1,0xfa) #8:7ee1    ld a,(A79F)
    rom.write_byte(0x23ee2,0x9f) #8:7ee2
    rom.write_byte(0x23ee3,0xa7) #8:7ee3
    rom.write_byte(0x23ee4,0xfe) #8:7ee4    cp a,07
    rom.write_byte(0x23ee5,0x07) #8:7ee5
    rom.write_byte(0x23ee6,0xd2) #8:7ee6    jp nc, 7F60
    rom.write_byte(0x23ee7,0x60) #8:7ee7
    rom.write_byte(0x23ee8,0x7f) #8:7ee8
    rom.write_byte(0x23ee9,0xfe) #8:7ee9    cp a,06
    rom.write_byte(0x23eea,0x06) #8:7eea
    rom.write_byte(0x23eeb,0xd2) #8:7eeb    jp nc, 7F54
    rom.write_byte(0x23eec,0x54) #8:7eec
    rom.write_byte(0x23eed,0x7f) #8:7eed
    rom.write_byte(0x23eee,0xfe) #8:7eee    cp a,05
    rom.write_byte(0x23eef,0x05) #8:7eef
    rom.write_byte(0x23ef0,0xd2) #8:7ef0    jp nc, 7F48
    rom.write_byte(0x23ef1,0x48) #8:7ef1
    rom.write_byte(0x23ef2,0x7f) #8:7ef2
    rom.write_byte(0x23ef3,0xfe) #8:7ef3    cp a,04
    rom.write_byte(0x23ef4,0x04) #8:7ef4
    rom.write_byte(0x23ef5,0xd2) #8:7ef5    jp nc, 7F3C
    rom.write_byte(0x23ef6,0x3c) #8:7ef6
    rom.write_byte(0x23ef7,0x7f) #8:7ef7
    rom.write_byte(0x23ef8,0xfe) #8:7ef8    cp a,03
    rom.write_byte(0x23ef9,0x03) #8:7ef9
    rom.write_byte(0x23efa,0xd2) #8:7efa    jp nc, 7F30
    rom.write_byte(0x23efb,0x30) #8:7efb
    rom.write_byte(0x23efc,0x7f) #8:7efc
    rom.write_byte(0x23efd,0xfe) #8:7efd    cp a,02
    rom.write_byte(0x23efe,0x02) #8:7efe
    rom.write_byte(0x23eff,0xd2) #8:7eff    jp nc, 7F24
    rom.write_byte(0x23f00,0x24) #8:7f00
    rom.write_byte(0x23f01,0x7f) #8:7f01
    rom.write_byte(0x23f02,0xfe) #8:7f02    cp a,01
    rom.write_byte(0x23f03,0x01) #8:7f03
    rom.write_byte(0x23f04,0xd2) #8:7f04    jp nc, 7F18
    rom.write_byte(0x23f05,0x18) #8:7f05
    rom.write_byte(0x23f06,0x7f) #8:7f06
    rom.write_byte(0x23f07,0xfe) #8:7f07    cp a,00
    rom.write_byte(0x23f08,0x00) #8:7f08
    rom.write_byte(0x23f09,0xd2) #8:7f09    jp nc, 7F0C
    rom.write_byte(0x23f0a,0x0c) #8:7f0a
    rom.write_byte(0x23f0b,0x7f) #8:7f0b
    #--
    rom.write_byte(0x23f0c,0xfa) #8:7f0c    ld a,(A409)
    rom.write_byte(0x23f0d,0x09) #8:7f0d
    rom.write_byte(0x23f0e,0xa4) #8:7f0e
    rom.write_byte(0x23f0f,0xa7) #8:7f0f    and a
    rom.write_byte(0x23f10,0xca) #8:7f10    jp z,41C4
    rom.write_byte(0x23f11,0xc4) #8:7f11
    rom.write_byte(0x23f12,0x41) #8:7f12
    rom.write_byte(0x23f13,0x3e) #8:7f13    ld a,23
    rom.write_byte(0x23f14,0x23) #8:7f14
    rom.write_byte(0x23f15,0xc3) #8:7f15    jp 418A
    rom.write_byte(0x23f16,0x8a) #8:7f16
    rom.write_byte(0x23f17,0x41) #8:7f17
    #--
    rom.write_byte(0x23f18,0xfa) #8:7f18    ld a,(A40A)
    rom.write_byte(0x23f19,0x0a) #8:7f19
    rom.write_byte(0x23f1a,0xa4) #8:7f1a
    rom.write_byte(0x23f1b,0xa7) #8:7f1b    and a
    rom.write_byte(0x23f1c,0xca) #8:7f1c    jp z,41C4
    rom.write_byte(0x23f1d,0xc4) #8:7f1d
    rom.write_byte(0x23f1e,0x41) #8:7f1e
    rom.write_byte(0x23f1f,0x3e) #8:7f1f    ld a,23
    rom.write_byte(0x23f20,0x23) #8:7f20
    rom.write_byte(0x23f21,0xc3) #8:7f21    jp 418A
    rom.write_byte(0x23f22,0x8a) #8:7f22
    rom.write_byte(0x23f23,0x41) #8:7f23
    #--
    rom.write_byte(0x23f24,0xfa) #8:7f24    ld a,(A40B)
    rom.write_byte(0x23f25,0x0b) #8:7f25
    rom.write_byte(0x23f26,0xa4) #8:7f26
    rom.write_byte(0x23f27,0xa7) #8:7f27    and a
    rom.write_byte(0x23f28,0xca) #8:7f28    jp z,41C4
    rom.write_byte(0x23f29,0xc4) #8:7f29
    rom.write_byte(0x23f2a,0x41) #8:7f2a
    rom.write_byte(0x23f2b,0x3e) #8:7f2b    ld a,23
    rom.write_byte(0x23f2c,0x23) #8:7f2c
    rom.write_byte(0x23f2d,0xc3) #8:7f2d    jp 418A
    rom.write_byte(0x23f2e,0x8a) #8:7f2e
    rom.write_byte(0x23f2f,0x41) #8:7f2f
    #--
    rom.write_byte(0x23f30,0xfa) #8:7f30    ld a,(A40C)
    rom.write_byte(0x23f31,0x0c) #8:7f31
    rom.write_byte(0x23f32,0xa4) #8:7f32
    rom.write_byte(0x23f33,0xa7) #8:7f33    and a
    rom.write_byte(0x23f34,0xca) #8:7f34    jp z,41C4
    rom.write_byte(0x23f35,0xc4) #8:7f35
    rom.write_byte(0x23f36,0x41) #8:7f36
    rom.write_byte(0x23f37,0x3e) #8:7f37    ld a,23
    rom.write_byte(0x23f38,0x23) #8:7f38
    rom.write_byte(0x23f39,0xc3) #8:7f39    jp 418A
    rom.write_byte(0x23f3a,0x8a) #8:7f3a
    rom.write_byte(0x23f3b,0x41) #8:7f3b
    #--
    rom.write_byte(0x23f3c,0xfa) #8:7f3c    ld a,(A40D)
    rom.write_byte(0x23f3d,0x0d) #8:7f3d
    rom.write_byte(0x23f3e,0xa4) #8:7f3e
    rom.write_byte(0x23f3f,0xa7) #8:7f3f    and a
    rom.write_byte(0x23f40,0xca) #8:7f40    jp z,41C4
    rom.write_byte(0x23f41,0xc4) #8:7f41
    rom.write_byte(0x23f42,0x41) #8:7f42
    rom.write_byte(0x23f43,0x3e) #8:7f43    ld a,23
    rom.write_byte(0x23f44,0x23) #8:7f44
    rom.write_byte(0x23f45,0xc3) #8:7f45    jp 418A
    rom.write_byte(0x23f46,0x8a) #8:7f46
    rom.write_byte(0x23f47,0x41) #8:7f47
    #--
    rom.write_byte(0x23f48,0xfa) #8:7f48    ld a,(A40E)
    rom.write_byte(0x23f49,0x0e) #8:7f49
    rom.write_byte(0x23f4a,0xa4) #8:7f4a
    rom.write_byte(0x23f4b,0xa7) #8:7f4b    and a
    rom.write_byte(0x23f4c,0xca) #8:7f4c    jp z,41C4
    rom.write_byte(0x23f4d,0xc4) #8:7f4d
    rom.write_byte(0x23f4e,0x41) #8:7f4e
    rom.write_byte(0x23f4f,0x3e) #8:7f4f    ld a,23
    rom.write_byte(0x23f50,0x23) #8:7f50
    rom.write_byte(0x23f51,0xc3) #8:7f51    jp 418A
    rom.write_byte(0x23f52,0x8a) #8:7f52
    rom.write_byte(0x23f53,0x41) #8:7f53
    #--
    rom.write_byte(0x23f54,0xfa) #8:7f54    ld a,(A40F)
    rom.write_byte(0x23f55,0x0f) #8:7f55
    rom.write_byte(0x23f56,0xa4) #8:7f56
    rom.write_byte(0x23f57,0xa7) #8:7f57    and a
    rom.write_byte(0x23f58,0xca) #8:7f58    jp z,41C4
    rom.write_byte(0x23f59,0xc4) #8:7f59
    rom.write_byte(0x23f5a,0x41) #8:7f5a
    rom.write_byte(0x23f5b,0x3e) #8:7f5b    ld a,23
    rom.write_byte(0x23f5c,0x23) #8:7f5c
    rom.write_byte(0x23f5d,0xc3) #8:7f5d    jp 418A
    rom.write_byte(0x23f5e,0x8a) #8:7f5e
    rom.write_byte(0x23f5f,0x41) #8:7f5f
    #--
    rom.write_byte(0x23f60,0xc3) #8:7f60    jp 41C4
    rom.write_byte(0x23f61,0xc4) #8:7f61
    rom.write_byte(0x23f62,0x41) #8:7f62

def patch_world_movement(rom):
    # Block boss level entry
    rom.write_byte(0x21d76,0xc3) #8:5d76    jp 7f63
    rom.write_byte(0x21d77,0x63) #8:5d77
    rom.write_byte(0x21d78,0x7f) #8:5d78
    #--
    rom.write_byte(0x23f63,0xfa) #8:7f63    ld a,(A79E)
    rom.write_byte(0x23f64,0x9e) #8:7f64
    rom.write_byte(0x23f65,0xa7) #8:7f65
    rom.write_byte(0x23f66,0xfe) #8:7f66    cp a,19
    rom.write_byte(0x23f67,0x19) #8:7f67
    rom.write_byte(0x23f68,0xfa) #8:7f68    ld a,(A421)
    rom.write_byte(0x23f69,0x21) #8:7f69
    rom.write_byte(0x23f6a,0xa4) #8:7f6a
    rom.write_byte(0x23f6b,0xca) #8:7f6b    jp z, 7FB2
    rom.write_byte(0x23f6c,0xb2) #8:7f6c
    rom.write_byte(0x23f6d,0x7f) #8:7f6d
    rom.write_byte(0x23f6e,0xfa) #8:7f6e    ld a,(A79E)
    rom.write_byte(0x23f6f,0x9e) #8:7f6f
    rom.write_byte(0x23f70,0xa7) #8:7f70
    rom.write_byte(0x23f71,0xfe) #8:7f71    cp a,0A
    rom.write_byte(0x23f72,0x0a) #8:7f72
    rom.write_byte(0x23f73,0xfa) #8:7f73    ld a,(A422)
    rom.write_byte(0x23f74,0x22) #8:7f74
    rom.write_byte(0x23f75,0xa4) #8:7f75
    rom.write_byte(0x23f76,0xca) #8:7f76    jp z, 7FB2
    rom.write_byte(0x23f77,0xb2) #8:7f77
    rom.write_byte(0x23f78,0x7f) #8:7f78
    rom.write_byte(0x23f79,0xfa) #8:7f79    ld a,(A79E)
    rom.write_byte(0x23f7a,0x9e) #8:7f7a
    rom.write_byte(0x23f7b,0xa7) #8:7f7b
    rom.write_byte(0x23f7c,0xfe) #8:7f7c    cp a,18
    rom.write_byte(0x23f7d,0x18) #8:7f7d
    rom.write_byte(0x23f7e,0xfa) #8:7f7e    ld a,(A426)
    rom.write_byte(0x23f7f,0x26) #8:7f7f
    rom.write_byte(0x23f80,0xa4) #8:7f80
    rom.write_byte(0x23f81,0xca) #8:7f81    jp z, 7FB2
    rom.write_byte(0x23f82,0xb2) #8:7f82
    rom.write_byte(0x23f83,0x7f) #8:7f83
    rom.write_byte(0x23f84,0xfa) #8:7f84    ld a,(A79E)
    rom.write_byte(0x23f85,0x9e) #8:7f85
    rom.write_byte(0x23f86,0xa7) #8:7f86
    rom.write_byte(0x23f87,0xfe) #8:7f87    cp a,1C
    rom.write_byte(0x23f88,0x1c) #8:7f88
    rom.write_byte(0x23f89,0xfa) #8:7f89    ld a,(A423)
    rom.write_byte(0x23f8a,0x23) #8:7f8a
    rom.write_byte(0x23f8b,0xa4) #8:7f8b
    rom.write_byte(0x23f8c,0xca) #8:7f8c    jp z, 7FB2
    rom.write_byte(0x23f8d,0xb2) #8:7f8d
    rom.write_byte(0x23f8e,0x7f) #8:7f8e
    rom.write_byte(0x23f8f,0xfa) #8:7f8f    ld a,(A79E)
    rom.write_byte(0x23f90,0x9e) #8:7f90
    rom.write_byte(0x23f91,0xa7) #8:7f91
    rom.write_byte(0x23f92,0xfe) #8:7f92    cp a,14
    rom.write_byte(0x23f93,0x14) #8:7f93
    rom.write_byte(0x23f94,0xfa) #8:7f94    ld a,(A425)
    rom.write_byte(0x23f95,0x25) #8:7f95
    rom.write_byte(0x23f96,0xa4) #8:7f96
    rom.write_byte(0x23f97,0xca) #8:7f97    jp z, 7FB2
    rom.write_byte(0x23f98,0xb2) #8:7f98
    rom.write_byte(0x23f99,0x7f) #8:7f99
    rom.write_byte(0x23f9a,0xfa) #8:7f9a    ld a,(A79E)
    rom.write_byte(0x23f9b,0x9e) #8:7f9b
    rom.write_byte(0x23f9c,0xa7) #8:7f9c
    rom.write_byte(0x23f9d,0xfe) #8:7f9d    cp a,1A
    rom.write_byte(0x23f9e,0x1a) #8:7f9e
    rom.write_byte(0x23f9f,0xfa) #8:7f9f    ld a,(A424)
    rom.write_byte(0x23fa0,0x24) #8:7fa0
    rom.write_byte(0x23fa1,0xa4) #8:7fa1
    rom.write_byte(0x23fa2,0xca) #8:7fa2    jp z, 7FB2
    rom.write_byte(0x23fa3,0xb2) #8:7fa3
    rom.write_byte(0x23fa4,0x7f) #8:7fa4
    rom.write_byte(0x23fa5,0xfa) #8:7fa5    ld a,(A79E)
    rom.write_byte(0x23fa6,0x9e) #8:7fa6
    rom.write_byte(0x23fa7,0xa7) #8:7fa7
    rom.write_byte(0x23fa8,0xfe) #8:7fa8    cp a,28
    rom.write_byte(0x23fa9,0x28) #8:7fa9
    rom.write_byte(0x23faa,0xfa) #8:7faa    ld a,(A427)
    rom.write_byte(0x23fab,0x27) #8:7fab
    rom.write_byte(0x23fac,0xa4) #8:7fac
    rom.write_byte(0x23fad,0xca) #8:7fad    jp z, 7FB2
    rom.write_byte(0x23fae,0xb2) #8:7fae
    rom.write_byte(0x23faf,0x7f) #8:7faf
    rom.write_byte(0x23fb0,0x3e) #8:7fb0    ld a,1
    rom.write_byte(0x23fb1,0x01) #8:7fb1
    rom.write_byte(0x23fb2,0xa7) #8:7fb2    and a
    rom.write_byte(0x23fb3,0xca) #8:7fb3    jp z, 7FBE
    rom.write_byte(0x23fb4,0xbe) #8:7fb4
    rom.write_byte(0x23fb5,0x7f) #8:7fb5
    rom.write_byte(0x23fb6,0x3e) #8:7fb6    ld a,2b
    rom.write_byte(0x23fb7,0x2b) #8:7fb7
    rom.write_byte(0x23fb8,0xea) #8:7fb8    ld (A61C),a
    rom.write_byte(0x23fb9,0x1c) #8:7fb9
    rom.write_byte(0x23fba,0xa6) #8:7fba
    rom.write_byte(0x23fbb,0xc3) #8:7fbb    jp 5D79
    rom.write_byte(0x23fbc,0x79) #8:7fbc
    rom.write_byte(0x23fbd,0x5d) #8:7fbd
    rom.write_byte(0x23fbe,0xc3) #8:7fbe    jp 5D7D
    rom.write_byte(0x23fbf,0x7d) #8:7fbf
    rom.write_byte(0x23fc0,0x5d) #8:7fc0

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
    rom.write_byte(0x21dac,0xcd) #8:5dac    call 7FC1
    rom.write_byte(0x21dad,0xc1) #8:5dad
    rom.write_byte(0x21dae,0x7f) #8:5dae

    rom.write_byte(0x23fc1,0xfa) #8:7fc1    ld	a,(A79E)
    rom.write_byte(0x23fc2,0x9e) #8:7fc2
    rom.write_byte(0x23fc3,0xa7) #8:7fc3
    rom.write_byte(0x23fc4,0x4f) #8:7fc4    ld	c, a
    rom.write_byte(0x23fc5,0x06) #8:7fc5    ld	b, 00
    rom.write_byte(0x23fc6,0x00) #8:7fc6
    rom.write_byte(0x23fc7,0x21) #8:7fc7    ld	hl, 7FCD
    rom.write_byte(0x23fc8,0xcd) #8:7fc8
    rom.write_byte(0x23fc9,0x7f) #8:7fc9
    rom.write_byte(0x23fca,0x09) #8:7fca    add	hl, bc
    rom.write_byte(0x23fcb,0x7e) #8:7fcb    ld	a, [hl]
    rom.write_byte(0x23fcc,0xc9) #8:7fcc    ret

    # Start of custom level table
    rom.write_byte(0x23fcd,0x00) #8:7fcd
    rom.write_byte(0x23fce,0x01) #8:7fce
    rom.write_byte(0x23fcf,0x02) #8:7fcf
    rom.write_byte(0x23fd0,0x03) #8:7fd0
    rom.write_byte(0x23fd1,0x04) #8:7fd1
    rom.write_byte(0x23fd2,0x05) #8:7fd2
    rom.write_byte(0x23fd3,0x06) #8:7fd3
    rom.write_byte(0x23fd4,0x07) #8:7fd4
    rom.write_byte(0x23fd5,0x08) #8:7fd5
    rom.write_byte(0x23fd6,0x09) #8:7fd6
    rom.write_byte(0x23fd7,0x0a) #8:7fd7
    rom.write_byte(0x23fd8,0x0b) #8:7fd8
    rom.write_byte(0x23fd9,0x0c) #8:7fd9
    rom.write_byte(0x23fda,0x0d) #8:7fda
    rom.write_byte(0x23fdb,0x0e) #8:7fdb
    rom.write_byte(0x23fdc,0x0f) #8:7fdc
    rom.write_byte(0x23fdd,0x10) #8:7fdd
    rom.write_byte(0x23fde,0x11) #8:7fde
    rom.write_byte(0x23fdf,0x12) #8:7fdf
    rom.write_byte(0x23fe0,0x13) #8:7fe0
    rom.write_byte(0x23fe1,0x14) #8:7fe1
    rom.write_byte(0x23fe2,0x15) #8:7fe2
    rom.write_byte(0x23fe3,0x16) #8:7fe3
    rom.write_byte(0x23fe4,0x17) #8:7fe4
    rom.write_byte(0x23fe5,0x18) #8:7fe5
    rom.write_byte(0x23fe6,0x19) #8:7fe6
    rom.write_byte(0x23fe7,0x1a) #8:7fe7
    rom.write_byte(0x23fe8,0x1b) #8:7fe8
    rom.write_byte(0x23fe9,0x1c) #8:7fe9
    rom.write_byte(0x23fea,0x1d) #8:7fea
    rom.write_byte(0x23feb,0x1e) #8:7feb
    rom.write_byte(0x23fec,0x1f) #8:7fec
    rom.write_byte(0x23fed,0x20) #8:7fed
    rom.write_byte(0x23fee,0x21) #8:7fee
    rom.write_byte(0x23fef,0x22) #8:7fef
    rom.write_byte(0x23ff0,0x23) #8:7ff0
    rom.write_byte(0x23ff1,0x24) #8:7ff1
    rom.write_byte(0x23ff2,0x25) #8:7ff2
    rom.write_byte(0x23ff3,0x26) #8:7ff3
    rom.write_byte(0x23ff4,0x27) #8:7ff4
    rom.write_byte(0x23ff5,0x28) #8:7ff5
    # End of custom level table

# Shuffles the level music in vanilla limitations
def shuffle_music(rom, level_music):
    level_music_addr=[0x33ECD,0x33ED9,0x33EE5,0x33EF1,0x33EFD,0x33F09,0x33F15,0x33F21,0x33F2D,0x33F39,0x33F45,0x33F51,0x33F5D]
    # Second address always + 0x03 away
    for music_offset in level_music_addr:
        music_pick=level_music.pop()
        rom.write_byte(music_offset,music_pick)
        rom.write_byte(music_offset+0x03,music_pick)

def blocksanity(rom):
    rom.write_byte(0x153a,0xc3) #0:153a    jp 3C00
    rom.write_byte(0x153b,0x00) #0:153b
    rom.write_byte(0x153c,0x3c) #0:153c
    #---
    rom.write_byte(0x3c00,0xfa) #0:3c00    ld a,(A42F)
    rom.write_byte(0x3c01,0x2f) #0:3c01
    rom.write_byte(0x3c02,0xa4) #0:3c02
    rom.write_byte(0x3c03,0xfe) #0:3c03    cp a,0
    rom.write_byte(0x3c04,0x00) #0:3c04
    rom.write_byte(0x3c05,0xc2) #0:3c05    jp nz, 3C0E
    rom.write_byte(0x3c06,0x0e) #0:3c06
    rom.write_byte(0x3c07,0x3c) #0:3c07
    rom.write_byte(0x3c08,0x21) #0:3c08    ld hl,A430
    rom.write_byte(0x3c09,0x30) #0:3c09
    rom.write_byte(0x3c0a,0xa4) #0:3c0a
    rom.write_byte(0x3c0b,0xc3) #0:3c0b    jp 3C1B
    rom.write_byte(0x3c0c,0x1b) #0:3c0c
    rom.write_byte(0x3c0d,0x3c) #0:3c0d
    rom.write_byte(0x3c0e,0xfa) #0:3c0e    ld a,(A42E)
    rom.write_byte(0x3c0f,0x2e) #0:3c0f
    rom.write_byte(0x3c10,0xa4) #0:3c10
    rom.write_byte(0x3c11,0xfe) #0:3c11    cp a,6C
    rom.write_byte(0x3c12,0x6c) #0:3c12
    rom.write_byte(0x3c13,0xd2) #0:3c13    jp nc, 3C08
    rom.write_byte(0x3c14,0x08) #0:3c14
    rom.write_byte(0x3c15,0x3c) #0:3c15
    rom.write_byte(0x3c16,0x6f) #0:3c16    ld l, a
    rom.write_byte(0x3c17,0xfa) #0:3c17    ld a,(A42F)
    rom.write_byte(0x3c18,0x2f) #0:3c18
    rom.write_byte(0x3c19,0xa4) #0:3c19
    rom.write_byte(0x3c1a,0x67) #0:3c1a    ld h, a
    rom.write_byte(0x3c1b,0xfa) #0:3c1b    ld a,(A918)
    rom.write_byte(0x3c1c,0x18) #0:3c1c
    rom.write_byte(0x3c1d,0xa9) #0:3c1d
    rom.write_byte(0x3c1e,0x22) #0:3c1e    ldi (hl),a
    rom.write_byte(0x3c1f,0xfa) #0:3c1f    ld a,(A919)
    rom.write_byte(0x3c20,0x19) #0:3c20
    rom.write_byte(0x3c21,0xa9) #0:3c21
    rom.write_byte(0x3c22,0x22) #0:3c22    ldi (hl),a
    rom.write_byte(0x3c23,0x7c) #0:3c23    ld a, h
    rom.write_byte(0x3c24,0xea) #0:3c24    ld (A42F),a
    rom.write_byte(0x3c25,0x2f) #0:3c25
    rom.write_byte(0x3c26,0xa4) #0:3c26
    rom.write_byte(0x3c27,0x7d) #0:3c27    ld a, l
    rom.write_byte(0x3c28,0xea) #0:3c28    ld (A42E),a
    rom.write_byte(0x3c29,0x2e) #0:3c29
    rom.write_byte(0x3c2a,0xa4) #0:3c2a
    rom.write_byte(0x3c2b,0xfa) #0:3c2b    ld a,(A918)
    rom.write_byte(0x3c2c,0x18) #0:3c2c
    rom.write_byte(0x3c2d,0xa9) #0:3c2d
    rom.write_byte(0x3c2e,0x67) #0:3c2e    ld h, a
    rom.write_byte(0x3c2f,0xfa) #0:3c2f    ld a,(A919)
    rom.write_byte(0x3c30,0x19) #0:3c30
    rom.write_byte(0x3c31,0xa9) #0:3c31
    rom.write_byte(0x3c32,0x6f) #0:3c32    ld l, a
    rom.write_byte(0x3c33,0xc3) #0:3c33    jp 1542
    rom.write_byte(0x3c34,0x42) #0:3c34
    rom.write_byte(0x3c35,0x15) #0:3c35

def patch_rom(world, rom, player):

    # Starting Life Count, hex equals displayed value directly
    rom.write_byte(0x7B7D, int(str(world.starting_life_count[player].value),16))

    patch_basic_abilities(rom)
    patch_powerups(rom)
    patch_world_movement(rom)
    speedups(rom)
    apply_fixes(rom)
    patch_world_enter(rom)
    
    if world.blocksanity[player]:
        blocksanity(rom)
    if world.remove_autoscrollers[player]:
        remove_autoscrolling(rom)
    if world.music_shuffle[player]:
        level_music=[0x03,0x04,0x09,0x0A,0x0B,0x0E,0x10,0x16,0x17,0x1B,0x1E,0x22,0x27]
        world.per_slot_randoms[player].shuffle(level_music)
        shuffle_music(rom, level_music)

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