#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from robointerface import RoboInterface
from .roboif import roboif


class ftifpy:
    def __init__(self, iDevice=0, serialDevice=None, SerialType=RoboInterface.FT_ROBO_IF_COM, iUSBSerial=0):
        self.outer = RoboInterface(iDevice=iDevice, serialDevice=serialDevice, SerialType=SerialType, bEnableDist=True, iUSBSerial=iUSBSerial)
        self.numexts = self.outer.GetNumDevices()
        self.motorlocks = {}

        def genFalseList(n):
            l = []
            for _ in range(n):
                l.append(False)
            return(l)
        for n in range(self.numexts + 1):
            self.motorlocks[n] = genFalseList(8)

    def roboif(self, n=0):
        if n > self.outer.GetNumDevices():
            raise(ValueError('Extension ' + str(n) + ' too high!'))
        return(roboif(self, n))
