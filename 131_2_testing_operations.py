"""
Victoria Lynn Hagan 
Victoria014
1/24/2014
Lab 2 - CSC 131
"""

def evenFilter(data):
    return [data[i] for i in data if i%2 == 0]

def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    m = map(lambda x : x**3, a)
    print m

    fl= filter(lambda x: x%3 == 0, a)
    print fl

    rl = reduce(lambda x,y: str(x)+str(y), a)
    print rl

    lc1= [x**3 for x in a]
    print lc1

    lc2= [x for x in a if x%3 == 0]
    print lc2

    lc3= [x**3 for x in a if x%3 == 0]
    print lc3

    data = {1: "one", 3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}
    print evenFilter(data)

main()
