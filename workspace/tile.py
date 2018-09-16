"""@package docstring
Tile class
"""

class tile:
    """Tile class holds important values to be referenced by other classes"""
    def __init__(self):
        """Default Constructor"""
        self.isBomb=False
        self.isVisible=False
        self.isFlagged=False
        self.adjBomb=0

    def  config(self, isBomb, isVisible, isFlaged, adjBomb):
        """Initialises all values if given them"""
        self.isBomb = isBomb
        self.isVisible = isVisible
        self.isFlagged = isFlaged
        self.adjBomb = adjBomb


