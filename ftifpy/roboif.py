#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

from .peripherals import motor, IFinput, output, resistor, ultrasonic, colorsensor


class roboif:
    def __init__(self, ftif, n):
        self.ftif = ftif
        self.outer = self.ftif.outer
        self.id = n
        self.trailfollower = self.input

    def setLock(self, o, s):
        if s:
            for n in o:
                if self.ftif.motorlocks[self.id][n]:
                    raise(BlockingIOError)
        for n in o:
            self.ftif.motorlocks[self.id][n] = s

    def motor(self, o):
        return(motor(self, o))

    def input(self, i):
        return(IFinput(self, i))

    def output(self, o):
        return(output(self, o))

    def resistor(self, i):
        return(resistor(self, i))

    def ultrasonic(self, i):
        return(ultrasonic(self, i))

    def colorsensor(self, i):
        return(colorsensor(self, i))
