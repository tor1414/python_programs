"""
Victoria Lynn Hagan 
Victoria014
1/30/2014
Homework 1 - CSC 131
Program that uses 2D lists to verify whether or not a Sudoku solution is valid
"""

def checkLst(lst):
    """returns True if lst (may represent row, column or a block) has the values 1 to 9"""
    #replace pass by the necessary code
    a = []
    for value in lst:
        if value not in a:
            a.append(value)
        else:
            return False

def isValid(grid):
    """returns True if solution is valid and False otherwise"""

    #verify that every row has the numbers from 1 to 9
    #your code goes here
    for row in range(len(grid)):
        if checkLst(grid[row]) == False:
            return False

    #verify that every column has the numbers from 1 to 9
    #your code goes here
    for row in range(len(grid)):
        lst = []
        for column in range(len(grid[0])):
            lst.append(grid[row][column])
        if checkLst(lst) == False:
            return False

    #verify that every 3-by-3 box has the numbers from 1 to 9
    #Boxes will be processed in a left to right, top to bottom order
    startRow = 0 #row coordinate of starting cell in a 3-by-3 box
    startColumn = 0 #column coordinate of starting cell in a 3-by-3 box
    for boxNumber in range(0, 9): 
        currentBox = []
        for row in range(startRow, startRow + 3):
            for column in range(startColumn, startColumn + 3):
                currentBox.append(grid[row][column])
        #display(currentBox)
        if checkLst(currentBox) == False:
            return False
        startColumn += 3 #time to move to the next box
        if startColumn == 9: #time to move to the next row of boxes
            startColumn = 0
            startRow += 3
            
    #if here, then solution must have passed all verification
    return True 


def main():
    file_names_list = ["sudokuSample.txt"]
    
    for file_name in file_names_list:
        grid = [] #to store solution read from file
        f = open(file_name)
        for line in f:
            line = line.split()
            line = map(int, line) # convert strings to integres
            grid.append(line)

        if isValid(grid):
            print "valid solution"
        else:
            print "invalid solution"
        

main()
