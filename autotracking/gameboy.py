import sys
import consts
from webgameboy import WebGameboy


class Gameboy:
    def __init__(self):
        self.emulator = None
        # self.wramSnapshot = None
        # self.hramSnapshot = None
        self.ramSnapshot = None
        self.gfxSnapshot = None
        # self.wramLowSnapshot = None
    
    def canReadRom(self):
        return self.emulator != None and self.emulator.canReadRom
    
    def snapshot(self):
        # (wramLow, wram, hram) = self.readSnapshot()
        # (self.wramLowSnapshot, self.wramSnapshot, self.hramSnapshot) = self.readSnapshot()

        # # Keep reading until we get two consecutive snapshots that are the same
        # while (wramLow != self.wramLowSnapshot
        #        or wram != self.wramSnapshot
        #        or hram != self.hramSnapshot):
        #     (wramLow, wram, hram) = (self.wramLowSnapshot, self.wramSnapshot, self.hramSnapshot)
        #     (self.wramLowSnapshot, self.wramSnapshot, self.hramSnapshot) = self.readSnapshot()

        #     print (f'{wramLow == self.wramLowSnapshot}, {wram == self.wramSnapshot}, {hram == self.hramSnapshot}')
        self.ramSnapshot = self.emulator.readSnapshot()

        if self.canReadRom():
            self.gfxSnapshot = self.emulator.readRom(consts.gfxStart, consts.gfxHashSize)
    
    def findEmulator(self):
        if self.emulator is None:
            self.emulator = WebGameboy(12345)
        return True

    def readRamByte(self, address):
        return self.ramSnapshot[address - consts.wram]
    
    def readRomByte(self, address):
        assert(self.emulator.canReadRom)

        return self.emulator.readRomByte(address)
    
    def readRom(self, address, size):
        assert(self.emulator.canReadRom)

        return self.emulator.readRom(address, size)
