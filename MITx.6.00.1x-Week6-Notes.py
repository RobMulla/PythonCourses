# EdX MITx.6.00.1x - Week 6 Code and notes

# Lecture 11: Classes #

# Below is the coordinate.py example provided by instructor
import math


def sq(x):
    return x * x


class Coordinate(object):  # object is superclass - coordinate is subclass
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distance(self, other):
        return math.sqrt(sq(self.x - other.x)
                         + sq(self.y - other.y))


c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print "c.x is: " + str(c.x)
print "origin.x is: " + str(origin.x)


# L11 problem 1

class Address(object):
    def __init__(self, number, streetName):
        self.number = number  # Line 1: Creating a number attribute
        self.streetName = streetName  # Line 2: Creating a streetName attribute


# An Enviornement View of Classes

c.__init__(5, 6)
print c.x, c.y
print origin.x, origin.y

# Adding Methods to a Class

print c
print type(c)
print Coordinate, type(Coordinate)

print isinstance(c, Coordinate)

print c.distance(origin)
print Coordinate(3,4).distance(origin)


print 7 + 17 + 7
print 18+18+8