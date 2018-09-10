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


    #Getters
    def getIsBomb(self):
        return self.isBomb
    def getisVisible(self):
        return self.isVisible
    def getIsFlagged(self):
        return self.isFlagged
    def getAdjBomb(self):
        return self.adjBomb

    #Setters
    def setIsBomb(self, val):
        self.isBomb=val
    def setIsVisible(self, val):
        self.isVisible=val
    def setIsFlagged(self,val):
        self.isFlagged=val
    def setAdjBomb(self,val):
        self.adjBomb=val

