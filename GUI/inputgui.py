#this class is going to be used to gain input for pysweeper metrics
# learned from http://effbot.org/tkinterbook/entry.htm
from tkinter import *


class input_gui:
    """User needs to instantiate a Tk() object and use that as the second argument to this constructor. Then call
        (Tk object).mainloop() to run GUI."""
    def __init__(self,master):
        master.title("Pysweeper")
        Label(master, text="Height:", ).grid(row=0)
        Label(master, text="Width:").grid(row=1)
        Label(master, text="Number of bombs:").grid(row=2)
        self.widthEntry = Entry(master)
        self.heightEntry = Entry(master)
        self.bombNum = Entry(master)

        self.widthEntry.grid(row=0, column=1)
        self.heightEntry.grid(row=1, column=1)
        self.bombNum.grid(row=2, column=1)
        Button(master, text = 'Quit', command=master.quit).grid(row = 3, column = 0, pady =4)
        Button(master, text = 'Enter', command=master.quit).grid(row = 3, column = 1, pady = 4)

    def getWidth(self):
        return int(self.widthEntry.get())
    def getHeight(self):
        return int(self.heightEntry.get())
    def getBombNum(self):
        return int(self.bombNum.get())
# Example
#   screen = Tk()
#   inputScreen = input_gui(screen)
#   screen.mainloop()


