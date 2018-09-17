"""@package docstring
Tile class
"""

class tile:
    """Tile class holds important values to be referenced by other classes
    """
    def __init__(self):
        """Default Constructor creates blank tile
        """

        ##If this tile is a Bomb
        self.isBomb=False
        ##If this tile is visible to user
        self.isVisible=False
        ##If this tile has been flagged by user
        self.isFlagged=False
        ##Number of adjacent bombs to the tile
        self.adjBomb=0

    def  config(self, isBomb, isVisible, isFlaged, adjBomb):
        """Initialises all values if given them
        """
        self.isBomb = isBomb
        self.isVisible = isVisible
        self.isFlagged = isFlaged
        self.adjBomb = adjBomb



