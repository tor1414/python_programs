"""
Victoria Lynn Hagan 
Victoria014
2/25/2014
Lab 5 - CSC 131
"""

from geometricObject import GeometricObject 
import math

class Circle(GeometricObject):
    def __init__(self, radius = 1.0, color = "White", filled = True):
        GeometricObject.__init__(self, color, filled)
        self._radius = radius

    def __str__(self):
        return "Circle: radius = " + str(self._radius) + GeometricObject.__str__(self)

    def getArea(self):
        return (self._radius ** 2)* math.pi

    def getPerimeter(self):
        return 2 * self._radius * math.pi

class Triangle(GeometricObject):
    def __init__(self, side1 = 1.0, side2 = 1.0, side3 = 1.0, color = "white", filled = True):
        GeometricObject.__init__(self, color, filled)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    def __str__(self):
        return "Triangle: side1 = " + str(self._side1) + " side2 = " + str(self._side2) + " side3 = " + str(self._side3) + GeometricObject.__str__(self)

    def getArea(self):
        s = (self._side1 + self._side2 + self._side3)/2.0
        return math.sqrt(s*(s - self._side1)*(s - self._side2)*(s - self._side3))

    def getPerimeter(self):
        return self._side1 + self._side2 + self._side3

def main():
    #Testing Circle class
    print "Entering input values for a circle"
    r = input('Enter value for radius: ')

    c1 = Circle(r)
    
    print c1
    print "%.2f" % c1.getArea()
    print "%.2f" % c1.getPerimeter()
    print c1.getColor()
    print c1.isFilled()

    #Testing Triangle class
    print "\nEntering input values for a traingle"
    s1 = input('Enter value for side1: ')
    s2 = input('Enter value for side2: ')
    s3 = input('Enter value for side3: ')
    color = raw_input('Enter color of the triangle: ')
    filled = input('Is the triangle filled (1/0)? ')
    filled = (filled == 1)
    
    t1 = Triangle(s1, s2, s3, color, filled)

    print t1
    print "%.2f" % t1.getArea()
    print "%.2f" % t1.getPerimeter()
    print t1.getColor()
    print t1.isFilled()

main()
