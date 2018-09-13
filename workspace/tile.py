class tile:
    def __init__(self):
        self.isBomb=False
        self.isVisible=False
        self.isFlagged=False
        self.adjBomb=0
    def _init_(self, isBomb, isVisible, isFlaged, adjBomb):
        self.isBomb = isBomb
        self.isVisible = isVisible
        self.isFlagged = isFlaged
        self.adjBomb = adjBomb


