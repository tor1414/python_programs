"""
Victoria Lynn Hagan 
Victoria014
05/06/2014
Lab 12 - CSC 131
"""

import random

#---------------Node Code----------------

class Node(object):

    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next

class TwoWayNode(Node):

    def __init__(self, data, previous = None, next = None):
        Node.__init__(self, data, next)
        self.previous = previous

#---------------Queue Code----------------

class LinkedQueue(object):
    """ Link-based queue implementation."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        newNode = Node (newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode  
        self._size += 1

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._front.data

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result

#----------nToFront Function----------
    
def nToFront(q, n):
    '''The method moves the nth element of the queue to the front,
        leaving the order of all other elements unchanged.'''
    if n <0 or n >= len(q):
        print "***Invalid Index***"

    probe = q._front
    currentIndex = 0
    while n > 1 and probe != None:
        if currentIndex == n:
            break
        currentIndex += 1
        probe = probe.next

    x = probe.next.data
    q._front = Node(x, q._front)
    probe.next = probe.next.next

    
        

def main():
    COLORS = ["red", "green", "blue", "yellow", "orange"]
    SIZE = 15
    q = LinkedQueue()
    for i in range(SIZE):
        q.enqueue(random.choice(COLORS))
    print q
    nToFront(q, 9)
    print q 

main()



"""
Instructions


[Queues] Write a Python function called nToFront that takes as parameters
a queue q and an integer n. The method moves the nth element of the queue
to the front, leaving the order of all other elements unchanged. In the
ordering, the first element is the front of the queue, the second element
is the element after the front, and so forth. The figure below illustrates
the action of nToFront( ) for a queue of integer values and n = 4. Use only
Queue operations (i.e., the only data structure you can use for your
solution is that of a queue; you can use more than one queue object if you
need).

      Before
 --- --- --- --- ---
| 8 | 5 | 2 | 3 | 7 |
 --- --- --- --- ---
front           rear

      After
 --- --- --- --- ---
| 3 | 8 | 5 | 2 | 7 |
 --- --- --- --- ---
front                 rear   

 
Name your file lab12.py. Make sure to include your name and the name of your
eccentric folder at the top of the file in a docstring. When you are done,
demonstrate your code to the instructor and and upload an electronic copy of
your solution to your CSC131 upload folder in a folder called  LABS\lab13.
"""
