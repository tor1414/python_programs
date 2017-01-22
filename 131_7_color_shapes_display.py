"""
Victoria Lynn Hagan 
Victoria014
3/18/2014
Lab 7 - CSC 131
"""

from Tkinter import *


class Canvas1(Frame):
    def __init__(self):
        """Sets up the window and widgets"""
        Frame.__init__(self)
        self.master.title("GUIs drawing geometric shapes")
        self.grid()

        #create a canvas and place in this frame
        self.canvas = Canvas(self, width = 400, height = 300, 
            bg = "white")
        self.canvas.grid(row = 0, column = 0)

        #place buttons in a pane
        pane = Frame(self)
        pane.grid(row = 1, column = 0)
        self.f1 = IntVar()
        self.s1 = IntVar()
        filled = Checkbutton(pane, text = "Filled",
                                variable = self.f1, onvalue = 1, offvalue = 0)

        rectangle = Radiobutton(pane, text = "Rectangle",
                                  variable = self.s1, value = 1,
                                  command = self.displayRect)
        oval = Radiobutton(pane, text = "Oval",
                                  variable = self.s1, value = 2,
                                  command = self.displayOval)

        
        clear = Button(pane, text = "Clear", command = self.clearCanvas)

        rectangle.grid(row = 0, column = 0)
        oval.grid(row = 0, column = 1)
        filled.grid(row = 0, column = 2)
        clear.grid(row = 0, column = 3)

    

    #Display rectangle
    def displayRect(self):
        if self.f1.get() == 1:
            self.canvas.create_rectangle(50, 50, 250, 250,
                                         fill = "red", tags = "rect")
        else:
            self.canvas.create_rectangle(50, 50, 250, 250,
                                         tags = "rect1")

    def displayOval(self):
        if self.f1.get() == 1: 
            self.canvas.create_oval(50, 100, 250, 200,
                                         fill = "yellow", tags = "oval")
        else:
            self.canvas.create_oval(50, 100, 250, 200,
                                          tags = "oval1")

    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "oval1", "rect1")

def main():
    Canvas1().mainloop()


main()



        
