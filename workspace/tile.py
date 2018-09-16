<<<<<<< HEAD
  class tile:
=======
"""@package docstring
Tile class
"""

class tile:
    """Tile class holds important values to be referenced by other classes"""
>>>>>>> 65495448b745c83c751bf4a2b1a3fb3e976a8d4a
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


