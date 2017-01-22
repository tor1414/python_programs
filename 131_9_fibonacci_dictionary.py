"""
Victoria Lynn Hagan 
Victoria014
4/8/2014
Lab 9 - CSC 131
"""

class Counter(object):
    def __init__(self):
        self.number = 0

    def increment(self):
        self.number += 1

    def __str__(self):
        return str(self.number)
    
def fib(n, dic, counter):
        counter.increment()
        if n not in dic:
            if n < 3:
                dic[n] = 1
                #return dic[n]
            else:
                dic[n] = fib(n-1, dic, counter) + fib(n-2, dic, counter)
                #return dic[n]
        return dic[n]

def main():
    problemSize = 1
    print "%12s%15s%15s" % ("Problem Size", "Calls", "Result")
    
    for count in xrange(7):
        d = {} # empty dictionary
        counter = Counter()
        result = fib(problemSize, d, counter)

        print "%12d%15s%15d" % (problemSize, counter, result)
        problemSize *= 2      

main()



        
