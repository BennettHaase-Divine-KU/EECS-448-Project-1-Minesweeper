"""this class is going to be used to gain input for pysweeper metrics
learned from http://effbot.org/tkinterbook/entry.htm
"""
from tkinter import *
import sys

class inputGui:
    """User needs to instantiate a Tk() object and use that as the second argument to this constructor. Then call
        (Tk object).mainloop() to run GUI.
    """
    def __init__(self,master):
        """Constructor, Contains all Tk objects
        """
        master.title("Pysweeper")
        ##Width from user
        self.width = StringVar()
        ##Height from user
        self.height = StringVar()
        ##Bombs from user
        self.numBombs =  StringVar()
        Label(master, text="Max Values (Height: 40, Width: 72, Empty Tiles: 1088)").grid(row=0, column=1)
        Label(master, text="Height:", ).grid(row=1)
        Label(master, text="Width:").grid(row=2)
        Label(master, text="Number of bombs:").grid(row=3)
        ##Width Widget
        self.widthEntry = Entry(master, textvariable= self.width)
        ##Heigh Widget
        self.heightEntry = Entry(master, textvariable= self.height)
        ##Bomb Widget
        self.bombNum = Entry(master, textvariable= self.numBombs)
        self.widthEntry.grid(row=1, column=1)
        self.heightEntry.grid(row=2, column=1)
        self.bombNum.grid(row=3, column=1)
        Button(master, text = 'Quit', command=sys.exit).grid(row = 4, column = 0, pady =4)
        Button(master, text = 'Enter', command=master.destroy).grid(row = 4, column = 1, pady = 4)

    def getWidth(self):
        """Returns Width from user
        """
        return int(self.width.get())
    def getHeight(self):
        """Returns Height from user
        """
        return int(self.height.get())
    def getBombNum(self):
        """Returns Bombs from user
        """
        return int(self.numBombs.get())

"""Example
   screen = Tk()
   inputScreen = input_gui(screen)
   screen.mainloop()
"""


