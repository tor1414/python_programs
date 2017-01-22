"""
Victoria Lynn Hagan 
Victoria014
2/11/2014
Lab 4 - CSC 131
"""
import math
class Point(object):
    COUNT = 0

    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
        Point.COUNT += 1

    def __str__(self):
        return "A point at the corrdinates (" + str(self._x) + " , " + str(self._y) + ")."

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def distance(self, anotherPoint):
        d = math.sqrt((anotherPoint._x - self._x) ** 2 + (anotherPoint._y - self._y) ** 2)
        return d

    def __cmp__(self, anotherPoint):
        d1 = math.sqrt((self._x) ** 2 + (self._y) ** 2)
        d2 = math.sqrt((anotherPoint._x) ** 2 + (anotherPoint._y) ** 2)
        if d1 < d2:
            return -1
        elif d1 > d2:
            return 1
        else:
            return 0

    def __eq__(self, anotherPoint):
        if self is anotherPoint:
            return True
        elif type(self) != type(anotherPoint):
            return False
        else:
            d1 = math.sqrt((self._x) ** 2 + (self._y) ** 2)
            d2 = math.sqrt((anotherPoint._x) ** 2 + (anotherPoint._y) ** 2)
            return  d1 == d2

    def __ne__(self, anotherPoint):
        return not self == anotherPoint

def main():
    p1 = Point(3,4)
    print p1
    p2 = Point(3,0)
    print "The x-cordinate of the point p2 is ", p2.getX()
    print "The y-cordinate of the point p2 is ", p2.getY()
    print "The distance between points p1 and p2 is ", p1.distance(p2)
    print "p1 == p2?", p1 == p2
    print "p1 != p2?", p1 != p2
    print "p1 < p2?", p1 < p2
    print "p1 <= p2?", p1 <= p2
    print "p1 > p2?", p1 > p2
    print "p1 >= p2?", p1 >= p2
    print "p1 == 'Hello'?", p1 == "Hello"
    print "p1 != 'Hello'?", p1 != "Hello"
    print "There have been ", p2.COUNT, " points entered into the class."

    

main()
    
    

    
