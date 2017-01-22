"""
Victoria Lynn Hagan 
Victoria014
3/4/2014
Lab 6 - CSC 131
"""

from Tkinter import *
import math

class Temperature(Frame):
    def __init__(self):
        """Sets up the window and widgets"""
        Frame.__init__(self)
        self.master.title("Temperature Conversion")
        self.grid()

        #Label and Field for the Farenheit
        self._farenheitLabel = Label(self, text = "Farenheit")
        self._farenheitLabel.grid(row=0, column = 0)
        self._farenheitVar = DoubleVar()
        self._farenheitEntry = Entry( self,
                                      textvariable = self._farenheitVar)
        self._farenheitVar.set(32.0)
        #self._farenheitEntry.delete(0, END)
        #self._farenheitEntry.insert(0, 32.0)
        self._farenheitEntry.grid(row= 1, column= 0)
        
        #label and field for the Celsius
        self._celsiusLabel = Label(self, text = "Celsius")
        self._celsiusLabel.grid(row = 0, column = 1)
        self._celsiusVar = DoubleVar()
        self._celsiusEntry = Entry( self,
                                      textvariable = self._celsiusVar)
        self._celsiusEntry.grid(row = 1, column = 1)

        #command button 1
        self._f2cbutton = Button(self,
                                 text = ">>>>",
                                 command = self._convertf2c)
        self._f2cbutton.grid(row = 2, column = 0)

        #command button 2
        self._c2fbutton = Button(self,
                                 text = "<<<<",
                                 command = self._convertc2f)
        self._c2fbutton.grid(row = 2, column = 1)

    def _convertf2c(self):
        """Event handler for button 1"""
        farenheit = self._farenheitVar.get()
        convertf2c = ((farenheit - 32) * 5/9)
        self._celsiusVar.set("%.2f" % convertf2c)

    def _convertc2f(self):
        """Event handler for button 2"""
        celsius = self._celsiusVar.get()
        convertc2f = ((celsius * 9/5) + 32)
        self._farenheitVar.set("%.2f" % convertc2f)

def main():
    """Instantiate and pop up th window"""
    Temperature().mainloop()

main()

        
