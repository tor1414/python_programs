"""
Victoria Lynn Hagan 
Victoria014
05/06/2014
Lab 13 - CSC 131
"""
import random
#--------------Node---------------

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class TwoWayNode(Node):

    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

#----------Linked Stack-----------

class LinkedStack(object):
    """ Link-based stack implementation."""

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        self._top = Node(newItem, self._top)
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        oldItem = self._top.data
        self._top = self._top.next
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        return self._top.data

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from bottom to top."""
        
        # Helper recurses to end of nodes
        def strHelper(probe):
            if probe is None:
                return ""
            else:
                return strHelper(probe.next) + \
                       str(probe.data) + " "
            
        return strHelper(self._top)

#------------Lab13.py-------------
class PezCandy(object):

    COLORS = ["red", "green", "blue", "yellow", "orange"]
    SIZE = 15
    def __init__(self):
        self.s = LinkedStack()
        self.fill()

    def fill(self):
        '''This method fills the stack self.s with 15 pieces of candy with
           random colors'''
        for i in range(PezCandy.SIZE):
            self.s.push(random.choice(PezCandy.COLORS))

    def displayContents(self):
        s2 = LinkedStack()
        print "\nContents of Joe's Pez candy: "
        while not self.s.isEmpty():
            candy = self.s.pop()
            print candy,
            s2.push(candy)
            
        #now candy is stored in stack s2 in the reverse order. Move it back to original stack
        while not s2.isEmpty():
            self.s.push(s2.pop())

    #------Additional Code--------

    def eatFavoriteCandy(self):
        '''This method simulates eating the favorite candy by removing
           the candy with the favorite color from the stack'''

        if self.s._top == None:
            return 

        if self.s._top.data == "orange":
            self.s._top = self.s._top.next
            self.s._size -= 1
        
        probe = self.s._top
        while probe.next != None:
            while probe.next != None and probe.next.data != "orange":
                probe = probe.next 
            if probe.next == None:
                return 
            else:
                probe.next = probe.next.next
                self.s._size -= 1
                   

def main():
   candy = PezCandy()
   candy.displayContents()
   candy.eatFavoriteCandy()
   candy.displayContents()

main()

"""
Instructions


[Stacks] In each plastic container of Pez candy, the colors are stored in
random order. Your little brother Joe only likes the orange ones, so he
painstakingly takes out all the candies, one by one, eats the orange ones,
and keeps the others in order, so that he can return them to the container
in exactly the same order as before - minus the orange candies, of course.
Complete the code for a program called lab13.py that uses stacks to simulate
this process by writing the code for the method eatFavoriteCandy( ). The
Pez candy container is assumed to contain originally 15 pieces of candy
with possible colors chosen randomly from the
set {red, green, blue, yellow, orange}.

"""
