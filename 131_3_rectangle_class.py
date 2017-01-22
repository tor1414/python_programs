"""
Victoria Lynn Hagan 
Victoria014
2/3/2014
Lab 3 - CSC 131
"""

class Rectangle(object):
    """A rectangle is represented by the value of its width and its height"""
    def __init__(self, width = 1, height = 2):
        """Intializes width"""
        self._width = width
        """intializes height"""
        self._height = height

    def __str__(self):
        """Return a string representation of a rectangle"""
        return 'A rectangle with width ' + str(self._width) + ' and height ' + str(self._height)

    def getArea(self):
        """Returns area"""
        return self._width * self._height

    def getPerimeter(self):
        """Returns perimeter"""
        return self._width * 2 + self._height * 2

    def isSquare(self):
        """Tests to see if the rectangle is square"""
        if self._width == self._height:
            return True
        else:
            return False


def main():
    r1 = Rectangle(5, 3)
    print r1
    print "The area of this rectangle is %0.2f" % r1.getArea()
    print "The perimeter of this rectangle is %0.2f" % r1.getPerimeter()
    if r1.isSquare() == True:
        print "This rectangle is a square."
    else:
        print "This rectangle is NOT a square."
    
    r2 = Rectangle(2.5, 2.5)
    print "\n", r2
    print "The area of this rectangle is %0.2f" % r2.getArea()
    print "The perimeter of this rectangle is %0.2f" % r2.getPerimeter()
    if r2.isSquare() == True:
        print "This rectangle is a square."
    else:
        print "This rectangle is NOT a square."
    

    r3 = Rectangle()
    print "\n", r3
    print "The area of this rectangle is %0.2f" % r3.getArea()
    print "The perimeter of this rectangle is %0.2f" % r3.getPerimeter()
    if r3.isSquare() == True:
        print "This rectangle is a square."
    else:
        print "This rectangle is NOT a square."
        
main()


    
