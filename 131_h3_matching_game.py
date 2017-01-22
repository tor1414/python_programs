"""
Victoria Lynn Hagan 
Victoria014
3/5/2014
Homework 3 - CSC 131
"""
import random

class Card(object):
    """ A card object with a rank stores both the card's value and
face (a string or Boolean variable to indicate whether the card is facing
up or down)."""

    def __init__(self, rank, face = False):
        """Creates a card with the given rank and suit."""
        self.rank = rank + 1
        self.face = 0
        
    def __str__(self):
        """Returns the string representation of a card."""
        return str(self.rank)

    def getRank(self):
        return self.rank

    def getFace(self):
        return self.face
    
    def showFace(self):
        self.face = 1
        return self.face

    def showBack(self):
        self.face = 0
        return self.face


class Deck(object):
    """ A deck containing 52 cards."""
    def __init__(self, count):
        self._cards = []
        for rank in range(count):
            c = Card(rank)
            self._cards.append(c)
            d = Card(rank)
            self._cards.append(d)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self._cards)

    def deal(self):
        """Removes and returns the top card or None 
        if the deck is empty."""
        if len(self) == 0:
           return None
        else:
           return self._cards.pop(0)

    def __len__(self):
       """Returns the number of cards left in the deck."""
       return len(self._cards)
    

class Game(object):
    """A maching game using cards"""
    BOARD = [ ]
    def __init__(self, rows, columns):
        """Includes a 2D list (of card objects) representing the game board
where the cards are placed, # of rows & # of columns of the game board."""
        self._rows = rows
        self._columns = columns
        self._count = (self._rows * self._columns)/2
        self._deck = Deck(self._count)
        self._deck.shuffle()
        self._board = [ ]
        for i in range(self._rows):
            row = [ ]
            for j in range(self._columns):
                x = '*'
                row.append(x)
            self._board.append(row)
        
         
    def play(self):
        """simulates playing the game"""
        self.populateBoard()
        self.displayBoard()
        while True:
            try:
                if self.GameOver() == True:
                    break
                
                card1 = raw_input("Enter cordinates for first card in the format: x y " ).split()
                card1 = (map(int, card1))
                card2 = raw_input("Enter cordinates for second card in the format: x y " ).split()
                card2 = (map(int, card2))
                x1 = card1[0]-1
                y1 = card1[1]-1
                x2 = card2[0]-1
                y2 = card2[1]-1
                
                if len(card1)!= 2 or len(card2)!= 2 or card1 == card2:
                    print "***INVALID COORDINATES! Try again. Do not use parenthese or commas.***"

                elif self._board[x1][y1].getRank() == self._board[x2][y2].getRank():
                    print "A MATCH!"
                    self._board[x1][y1].showFace()
                    self._board[x2][y2].showFace()
                    self.displayBoard()
            
                else:
                    self._board[x1][y1].showBack()
                    self._board[x2][y2].showBack()
                    print "Not an identical pair. Found "+ str(self._board[x1][y1].getRank()) + " at (" + str(card1[0]) + "," + str(card1[1]) + ") and " + str(self._board[x2][y2].getRank()) + " at (" + str(card2[0]) + "," + str(card2[1]) + ")."  
                    self.displayBoard()

            except ValueError:
                print "***INVALID COORDINATES! Try again. Do not use parenthese or commas.***"
            except IndexError:
                print "***INVALID COORDINATES! Try again. Do not use parenthese or commas.***"

    def GameOver(self):
        """checks whether or not the game is over"""
        faces = [ ]
        for i in range(self._rows):
            for j in range(self._columns):
                if self._board[i][j].getFace() == 0:
                    return False
        return True   

    def displayBoard(self):
        """displays the board"""
        display = [ ]
        for i in range(self._rows):
            row = [ ]
            for j in range(self._columns):
                if self._board[i][j].getFace() == 0:
                    x = '*'
                    row.append(x)
                else:
                    x = self._board[i][j]
                    row.append(x)
            display.append(row)

        for row in display:
            print " ".join(map(str, row))

    def populateBoard(self):
        """creates the initial 2D list of identical pairs of cards with
all the cards facing down"""
        for i in range(self._rows):
            for j in range(self._columns):
                self._board[i][j] = self._deck.deal()

def main():
    while True:
        # Force user to enter valid value for number of rows
        while True:
            rows = raw_input("Enter number of rows ")
            if rows.isdigit() and ( 1 <= int(rows) <= 9):
                rows = int(rows)
                break
            else:
                print "    ***Number of columns must be between 1 and 9! Try again.***"
                # Adding *** and indenting error message makes it easier for the user to see

        # Force user to enter valid value for number of columns
        while True:
            columns = raw_input("Enter number of columns ")
            if columns.isdigit() and ( 1 <= int(columns) <= 9):
                columns = int(columns)
                break
            else:
                print "    ***Number of columns must be between 1 and 9! Try again.***"

        if rows * columns % 2 == 0:
            break
        else:
            print "    ***The value of rows X columns must be even. Try again.***"

    game = Game(rows, columns)
    game.play()
main()
