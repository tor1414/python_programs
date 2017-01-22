"""
Victoria Lynn Hagan 
Victoria014
3/25/2014
Lab 8 - CSC 131
"""

from Tkinter import *


class Traffic(Frame):
    def __init__(self):
        """Sets up the window and widgets"""
        Frame.__init__(self)
        self.master.title("GUIs drawing geometric shapes")
        self.grid()

        #create a canvas and place in this frame
        self.canvas = Canvas(self, width = 300, height = 400, 
            bg = "light sky blue" )
        self.canvas.grid(row = 0, column = 0)
        
        self.canvas.create_line(0, 150, 300, 150, width = 40, fill = "slate gray")
        self.canvas.create_rectangle(0, 100, 50, 300, fill = "lime green")
        self.canvas.create_rectangle(100, 50, 200, 350,
                                         fill = "black", width = 9)
        self.canvas.create_oval(100, 50, 200, 150,
                                         fill = "white")
        self.canvas.create_oval(100, 150, 200, 250,
                                         fill = "white")
        self.canvas.create_oval(100, 250, 200, 350,
                                         fill = "green")

        
        dx = 1
        while True:
            self.canvas.after(2000) # Sleep for 2 seconds
            self.canvas.update() # Update canvas
            if dx == 1:
                self.canvas.create_oval(100, 50, 200, 150,
                                         fill = "white")
                self.canvas.create_oval(100, 150, 200, 250,
                                         fill = "white")
                self.canvas.create_oval(100, 250, 200, 350,
                                         fill = "green")
                dx += 1
            elif dx == 2:
                self.canvas.create_oval(100, 50, 200, 150,
                                         fill = "white")
                self.canvas.create_oval(100, 150, 200, 250,
                                         fill = "yellow")
                self.canvas.create_oval(100, 250, 200, 350,
                                         fill = "white")
                dx += 1    
            else:
                self.canvas.create_oval(100, 50, 200, 150,
                                         fill = "red")
                self.canvas.create_oval(100, 150, 200, 250,
                                         fill = "white")
                self.canvas.create_oval(100, 250, 200, 350,
                                         fill = "white")
                dx = 1
                
    


def main():
    Traffic().mainloop()


main()



        
