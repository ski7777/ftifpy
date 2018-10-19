#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


class IFinput:
    def __init__(self, roboif, i):
        assert(i in range(1, 9))
        self.roboif = roboif
        self.id = self.roboif.id
        self.outer = self.roboif.outer
        self.i = self.id * 8 + i

    def state(self):
        return(self.outer.Digital(self.i))


class motor:
    def __init__(self, roboif, m):
        assert(m in range(1, 5))
        self.roboif = roboif
        self.id = self.roboif.id
        self.outer = self.roboif.outer
        self.m = self.id * 4 + m
        self.locks = [(m - 1) * 2, (m - 1) * 2 + 1]
        self.roboif.setLock(self.locks, True)

    def __del__(self):
        self.stop()
        self.roboif.setLock(self.locks, False)

    def setSpeed(self, speed):
        if speed > 0:
            d = 'l'
        elif speed < 0:
            d = 'r'
        else:
            d = 's'
        speed = abs(speed) - 1
        self.outer.SetMotor(self.m, d, speed)

    def stop(self):
        self.setSpeed(0)

    def setDistantance(self, distance, syncto=None):
        raise(NotImplementedError)

    def finished(self):
        raise(NotImplementedError)

    def getCurrentDistance(self):
        raise(NotImplementedError)


class output:
    def __init__(self, roboif, o):
        assert(o in range(1, 9))
        self.roboif = roboif
        self.id = self.roboif.id
        self.outer = self.roboif.outer
        self.o = self.id * 8 + o
        self.locks = [o - 1]
        self.roboif.setLock(self.locks, True)

    def __del__(self):
        self.setLevel(0)
        self.roboif.setLock(self.locks, False)

    def setLevel(self, level):
        self.outer.SetOutput(self.o, level)


class resistor:
    def __init__(self, roboif, ar):
        self.roboif = roboif
        self.id = self.roboif.id
        assert(self.id == 0 and ar in range(1, 3) or ar == 1)
        self.outer = self.roboif.outer
        if self.id == 0:
            if ar == 1:
                self.ar = self.outer.GetAX
            else:
                self.ar = self.outer.GetAY
        elif self.id == 1:
            self.ar = self.outer.GetAX_Slave1
        elif self.id == 2:
            self.ar = self.outer.GetAX_Slave2
        else:
            self.ar = self.outer.GetAX_Slave3

    def value(self):
        return(self.ar())

    def ntcTemperature(self):
        raise(NotImplementedError)


class ultrasonic:
    def __init__(self, roboif, d):
        assert(d in range(1, 3))
        self.roboif = roboif
        self.id = self.roboif.id
        assert(self.id == 0)
        self.outer = self.roboif.outer
        if d == 1:
            self.d = self.outer.GetD1
        else:
            self.d = self.outer.GetD2

    def distance(self):
        return(self.d())


class colorsensor:
    def __init__(self, roboif, av):
        assert(av in range(1, 3))
        self.roboif = roboif
        self.id = self.roboif.id
        assert(self.id == 0)
        self.outer = self.roboif.outer
        if av == 1:
            self.av = self.outer.GetA1
        else:
            self.av = self.outer.GetA2

    def value(self):
        return(self.av())

    def color(self):
        raise(NotImplementedError)
