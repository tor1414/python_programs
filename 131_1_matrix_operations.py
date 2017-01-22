"""
Victoria L Hagan
CSC 131
Lab 1
"""

def CreateMatrix():
    matrix = [ ]
    for i in range(3):
        current_row = raw_input("Enter a 3-by-4 matrix for row %s:" %i )
        current_row = current_row.split()
        for c in range(len(current_row)):
            current_row[c]= float(current_row[c])
        matrix.append(current_row)
    return matrix

def display(matrix):
    print "The matrix is"
    for row in matrix:
        print " ".join(map(str, row)) #covert to strings & join
    
def sumColumn(matrix, columnIndex):
    Sum = 0
    for row in range(len(matrix)):
        Sum = Sum + matrix[row][columnIndex]
    print "Sum of the elements in column",columnIndex,"is", Sum  
    

def main():
    matrix = CreateMatrix()
    print " "
    display(matrix)
    print " "
    for x in range(len(matrix[0])):
        sumColumn(matrix, x)

main()
