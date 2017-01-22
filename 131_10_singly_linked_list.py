"""
Victoria Lynn Hagan 
Victoria014
4/22/2014
Lab 11 - CSC 131
"""
#---------------Node Class--------------------
class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

#---------------List Class--------------------

class SinglyLinkedStructure(object):
    def __init__(self, seq = None):
        #references the begining of the list
        self.head = None
        #holds the size of node list
        self.size = 0
        #intitalizes the sequence into nodes
        if seq is not None:
            for i in seq:
                self.append(i)
        
    def __str__(self):
        '''returns a string value of all nodes'''
        result = ""
        p = self.head
        while p != None:
            result += str(p.data)
            result += " "
            p = p.next
        return result    

    def append(self, value):
        '''adds a new node to the existing list of nodes'''
        if self.head is None:
            self.head = Node(value)
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = Node(value)
        
        self.size += 1
            

    def __len__(self):
        '''returns the number of nodes in an existing list of nodes'''
        return self.size

def main():
    l1 = SinglyLinkedStructure()
    print 'Empty singly linked structure'
    print l1
    print len(l1)
    print
    l1.append('Hello,')
    l1.append('how')
    l1.append('are')
    l1.append('you?')
    
   
    print l1
    print len(l1)
    print
    
    seq = range(1,6)
    l2 = SinglyLinkedStructure(seq)
    print l2
    print len(l2)
    print

    t = tuple([x*10 for x in seq])
    print t
    print

    l2 = SinglyLinkedStructure(t)
    print l2
    print len(l2)
    print

    l2 = SinglyLinkedStructure("abcxyz")
    print l2
    print len(l2)

main()

"""
We will try to match the following output:
>>> 
Empty singly linked structure

0

Hello, how are you? 
4

1 2 3 4 5 
5

(10, 20, 30, 40, 50)

10 20 30 40 50 
5

a b c x y z 
6
>>>
"""




        
