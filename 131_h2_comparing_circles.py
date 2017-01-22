"""
Victoria Lynn Hagan 
Victoria014
2/10/2014
Homework 2 - CSC 131
"""
import math 
class Circle2D(object):
    """A circle is represented by the value of it's radius and the corrdinates of it's center"""
    def __init__(self, x = 0, y = 0, radius = 0):
        """Intializes the X-corrdinate of the center"""
        self._x = x
        """Intializes the Y-corridinate of the center"""
        self._y = y
        """Intializes the radius"""
        self._radius = radius

    def __str__(self):
        """Return a string representation of a circle"""
        return 'Circle with center (' + str(self._x) + ' , ' + str(self._y) + ') and radius ' + str(self._radius) 

    def getX(self):
        """Returns the X-corrdinate of the center"""
        return self._x

    def getY(self):
        """Returns the Y-corrdinate of the center"""
        return self._y

    def getRadius(self):
        """Returns the Radius"""
        return self._radius

    def setRadius(self, radius = 0):
        """Intiallizes a new value for the Radius"""
        self._radius = radius
        
    def getArea(self):
        """Returns Area"""
        return self._radius * self._radius * math.pi

    def getPerimeter(self):
        """Returns Perimeter"""
        return 2 * math.pi * self._radius

    def containsPoint(self, x, y):
        """Tests to see if a point is within the circle"""
        d =  math.sqrt((x - self._x)** 2 + (y - self._y)** 2)
        if d < self._radius:
            return True
        else:
            return False

    def contains(self, circle2D):
        """Tests to see if anothoer circle is within the circle"""
        d = math.sqrt((circle2D._x - self._x) ** 2 + (circle2D._y - self._y) ** 2)
        if d <= self._radius:
            if circle2D._radius + d <= self._radius:
                return True
            else:
                return False
        else:
            return False

    def overlaps(self, circle2D):
        """Tests to see if anther circle overlaps with the circle"""
        d = math.sqrt((circle2D._x - self._x) ** 2 + (circle2D._y - self._y) ** 2)
        if d <= abs(circle2D._radius + self._radius):
                return True
        else:
            return False

    def __cmp__(self, anotherCircle):
        """Compares two circles based on the magnitude of each circles's radius"""
        if self._radius < anotherCircle._radius:
            return -1
        elif self._radius > anotherCircle._radius:
            return 1
        else:
            return 0
        

    def __eq__(self, anotherCircle):
        """Checks for equality between two circles based on each circle's radius"""
        if self is anotherCircle:
            return True
        elif type(self) != type(anotherCircle):
            return False
        else:
            return self._radius == anotherCircle._radius # and \
                   # self._x == anotherCircle._x and \
                   # self._y == anotherCircle._y
                    # I would personally also compare the x and y to validate 
                    # that they are the same circle since in math the center is
                    # part of what defines a circle alongside the radius

    def __ne__(self, anotherCircle):
        """Checks for inequality between two circles based on each circles radius"""
        return not self == anotherCircle

    def __contains__(self, anotherCircle):
        """Tests to see if another circle is within the circle using the 'in' operator""" 
        d = math.sqrt((anotherCircle._x - self._x) ** 2 + (anotherCircle._y - self._y) ** 2)
        if d <= self._radius:
            if anotherCircle._radius + d <= self._radius:
                return True
        else:
            return False
    #I included the following method because your instructions sounded like
        # you wanted the possiblity of testing a (x,y) tuple using the special
        # method __contains__(self, item). If I am incorrect I apologize. 
    def __contains__(self, item):
        """Tests to see if an item based on type is within the circle using the 'in' operator"""
        if type(item) ==  type(self):
            d = math.sqrt((item._x - self._x) ** 2 + (item._y - self._y) ** 2)
            if d <= self._radius:
                if item._radius + d <= self._radius:
                    return True
                else:
                    return False
        elif type(item) == type(tuple(item)):
            x = item[0]
            y = item[1]
            d =  math.sqrt((x - self._x)** 2 + (y - self._y)** 2)
            if d < self._radius:
                    return True
            else:
                return False
        else: 
            return False


def main():
    x = input("Enter x coordinate for the center of circle 1: ")
    y = input("Enter y coordinate for the center of circle 1: ")
    r = input("Enter the radius of circle 1: ")
    c1 = Circle2D(x, y, r)
    print c1
    
    x = input("\nEnter x coordinate for the center of circle 2: ")
    y = input("Enter y coordinate for the center of circle 2: ")
    r = input("Enter the radius of circle 2: ")
    c2 = Circle2D(x, y, r)
    print c2

    #Test the getArea() and getPerimeter() methods
    print "\nArea of a %s is %0.2f" % (c1, c1.getArea())
    print "Perimeter of a %s is %0.2f" % (c1, c1.getPerimeter())

    print "\nArea of a %s is %0.2f" % (c2, c2.getArea())
    print "Perimeter of a %s is %0.2f" % (c2, c2.getPerimeter())
    #-------------------

    #Test containsPoint() method
    print "\nResult of c1.containsPoint(c2.getX( ), c2.getY( )) is",
    print c1.containsPoint(c2.getX( ), c2.getY( ))

    #Test contains() method
    if c1.contains(c2):
        print "\n%s contains %s" % (c1, c2)
    else: 
        print "\n%s does not contain %s" % (c1, c2)
                                          
    print "\nResult of c2.contains(c1) is",
    print c2.contains(c1)
    #----------------

    #Test overlap() method
    if c1.overlaps(c2):
        print "\n%s overlaps with %s" % (c1,c2)
    else: 
        print "\n%s does not overlap with %s" % (c1,c2)
    #--------------

    #Test overloaded in operator                                     
    print "\nResult of c2 in c1 is", c2 in c1

    #Testing overloaded comparison and equality operators
    #Something similar to this
    print "\nTesting overloaded comparison operators..."
    print "c1 == c2?", c1 == c2
    print "c1 != c2?", c1 != c2
    print "c1 < c2?", c1 < c2
    print "c1 <= c2?", c1 <= c2
    print "c1 > c2?", c1 > c2
    print "c1 >= c2?", c1 >= c2
    print 'c1 == "Hello"?', c1 == "Hello"
    print 'c1 != "Hello"?', c1 != "Hello"
    
main()
