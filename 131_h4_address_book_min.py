"""
Victoria Lynn Hagan 
Victoria014
3/4/2014
Homework 4 - CSC 131
"""

#This is the minimum requirement of the homework as I did not have time to write the optional code
from Tkinter import *
import tkMessageBox

class Address(Frame):
    def __init__(self):
        """Sets up the window and widgets"""
        Frame.__init__(self)
        self.master.title("Address Book")
        self.grid()

        #Label and Field for the name
        pane1 = Frame(self)
        pane1.grid(row = 0, column = 0)
        self._nameLabel = Label(pane1, text = "Name", width = 6)
        self._nameLabel.grid(row=0, column = 0)
        self._nameVar = StringVar()
        self._nameEntry = Entry(pane1, width = 40, 
                                      textvariable = self._nameVar)
        self._nameEntry.grid(row= 0, column= 1)
        
        #label and field for the street
        self._streetLabel = Label(pane1, text = "Street", width = 6)
        self._streetLabel.grid(row = 1, column = 0)
        self._streetVar = StringVar()
        self._streetEntry = Entry(pane1, width = 40,
                                      textvariable = self._streetVar)
        self._streetEntry.grid(row = 1, column = 1)

        #label and field for the city
        pane2 = Frame(self)
        pane2.grid(row = 1, column = 0)
        self._cityLabel = Label(pane2, text = "City", width = 6)
        self._cityLabel.grid(row = 0, column = 0)
        self._cityVar = StringVar()
        self._cityEntry = Entry(pane2,
                                      textvariable = self._cityVar)
        self._cityEntry.grid(row = 0, column = 1)

        #label and field for the state
        self._stateLabel = Label(pane2, text = "State")
        self._stateLabel.grid(row = 0, column = 2)
        self._stateVar = StringVar()
        self._stateEntry = Entry(pane2, width = 4,
                                      textvariable = self._stateVar)
        self._stateEntry.grid(row = 0, column = 3)

        #label and field for the zip
        self._zipLabel = Label(pane2, text = "Zip")
        self._zipLabel.grid(row = 0, column = 4)
        self._zipVar = StringVar()
        self._zipEntry = Entry(pane2, width = 5,
                                      textvariable = self._zipVar)
        self._zipEntry.grid(row = 0, column = 5)

        #Add button 
        pane3 = Frame(self)
        pane3.grid(row = 3, column = 0)
        self._addButton = Button(pane3,
                                 text = "Add",
                                 command = self._addEntry)
        self._addButton.grid(row = 0, column = 0)

        #Find button 
        self._findButton = Button(pane3,
                                 text = "Find",
                                 command = self._findEntry)
        self._findButton.grid(row = 0, column = 1)

        #Remove button 
        self._removeButton = Button(pane3,
                                 text = "Remove",
                                 command = self._removeEntry)
        self._removeButton.grid(row = 0, column = 2)

        #Clear button 
        self._clearButton = Button(pane3,
                                 text = "Clear",
                                 command = self._clearEntry)
        self._clearButton.grid(row = 0, column = 3)

        #Save button 
        self._saveButton = Button(pane3,
                                 text = "Save",
                                 command = self._saveEntry)
        self._saveButton.grid(row = 0, column = 4)
        

    def _addEntry(self):
        tkMessageBox.showinfo( message = "Address for " + str(self._nameVar.get()) + " has been added.",
                               parent = self)

    def _findEntry(self):
        tkMessageBox.showinfo( message = "Address for " + str(self._nameVar.get()) + " has been found.",
                               parent = self)

    def _removeEntry(self):
        tkMessageBox.showinfo( message = "Address for " + str(self._nameVar.get()) + " has been removed.",
                               parent = self)

    def _clearEntry(self):
        tkMessageBox.showinfo( message = "Address for " + str(self._nameVar.get()) + " has been cleared.",
                               parent = self)

    def _saveEntry(self):
        tkMessageBox.showinfo( message = "Address for " + str(self._nameVar.get()) + " has been saved.",
                               parent = self)
       

def main():
    """Instantiate and pop up th window"""
    Address().mainloop()

main()

        
