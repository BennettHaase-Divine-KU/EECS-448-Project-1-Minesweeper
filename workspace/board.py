import random
from workspace.tile import tile
"""@package docstring
 Board class

"""
class Board:
    """ Creates an array of tile objects and has methods to interact with those tiles
    """
    def __init__(self):
        self.board = []

    """Creates an array of empty tile objects
    """
    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        # Declaration of board and adding row/columns
        self.width=x
        self.length=y
        self.num_bombs=z
        self.num_flagged=0

        for j in range(self.width):
            column = []
            for i in range(self.length):
                column.append(tile())
            self.board.append(column)

        return
    """Prints the hidden array to terminal
    only for debugging
    """
    def print_board(self):
        cols = len(self.board)
        rows = 0
        if cols:
            rows = len(self.board[0])
        for j in range(rows):
            for i in range(cols):
                if(self.board[i][j].isBomb == True and self.board[i][j].isVisible==True):
                    print("*", end=" ")
                elif(self.board[i][j].isVisible==True):
                    print(self.board[i][j].adjBomb, end=" ")
                else:
                    print("?", end=" ")
            print()
        print()
        return self.board

    """ Randomly places bombs
    """
    def place_bomb(self):
        n=0
        while n<self.num_bombs:
            e = random.randint(0, self.width-1)
            f = random.randint(0, self.length-1)
            if(self.board[e][f].isBomb == True):
                n = n
            else:
                self.board[e][f].isBomb = True
                n = n + 1
        return self.board



    """Prints the true array to terminal
        only for debugging
    """
    def print_board_true(self):
        cols = len(self.board)
        rows = 0
        if cols:
            rows = len(self.board[0])
        for j in range(rows):
            for i in range(cols):
                if (self.board[i][j].isBomb == True):
                    print("*", end=" ")
                else:
                    print(self.board[i][j].adjBomb, end=" ")
            print()
        print()
        return self.board
    """Sets in the tile object the number of adjacent bombs
    """
    def setAdjBomb(self):
        cols = len(self.board)
        rows = 0
        if cols:
            rows = len(self.board[0])
        for j in range(rows):
            for i in range(cols):
                self.board[i][j].adjBomb=self.search(i,j)

    """Returns the number of adjacent bombs at a position
    """
    def search(self, posx, posy):
        count=0

        if 0 <= posx-1 < self.width and 0 <= posy < self.length:  # make sure is not out of bound
            if self.board[posx-1][posy].isBomb == True:  # if the adjacent is the bomb
                count += 1

        if 0 <= posx+1 < self.width and 0 <= posy < self.length:
            if self.board[posx+1][posy].isBomb == True:
                count += 1

        if 0 <= posx < self.width and 0 <= posy-1 < self.length:
            if self.board[posx][posy-1].isBomb == True:
                count += 1

        if 0 <= posx < self.width and 0 <= posy+1 < self.length:
            if self.board[posx][posy+1].isBomb == True:
                count += 1

        if 0 <= posx-1 < self.width and 0 <= posy-1 < self.length:
            if self.board[posx-1][posy-1].isBomb == True:
                count += 1

        if 0 <= posx-1 < self.width and 0 <= posy+1 < self.length:
            if self.board[posx-1][posy+1].isBomb == True:
                count += 1

        if 0 <= posx+1 < self.width and 0 <= posy-1 < self.length:
            if self.board[posx+1][posy-1].isBomb == True:
                count += 1

        if 0 <= posx+1 < self.width and 0 <= posy+1 < self.length:
            if self.board[posx+1][posy+1].isBomb == True:
                count += 1
        return count

    """Reveals a tile at a position
    3 main cases: Tile not adjacent to a bomb, tile is adjacent to a bomb, tile is a bomb
    if tile is not a bomb reveal tiles around it
    if tile is adjacent to a bomb just reveal that tile
    if tile is a bomb check_win_lose method will take care of game over state
    """
    def reveal_tile(self, posx, posy):
        if self.board[posx][posy].adjBomb == 0 and self.board[posx][posy].isVisible==False and self.board[posx][posy].isFlagged==False:  # if the tile you reveal has 0 bomb adjacentand is unrevealed,you can reveal
            if 0 <= posx-1 < self.width and 0 <= posy < self.length:  # make sure is in the bound
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx - 1, posy)  # go through it again since there is no bomb adjacent on the first tile

            if 0 <= posx+1 < self.width and 0 <= posy < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx + 1, posy)

            if 0 <= posx < self.width and 0 <= posy-1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx, posy - 1)

            if 0 <= posx<self.width and 0 <= posy+1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx, posy + 1)

            if 0 <= posx-1 < self.width and 0 <= posy-1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx - 1, posy - 1)

            if 0 <= posx-1 < self.width and 0 <= posy+1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx - 1, posy + 1)

            if 0 <= posx+1<self.width and 0 <= posy-1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx + 1, posy - 1)

            if 0 <= posx+1 < self.width and 0 <= posy+1 < self.length:
                self.board[posx][posy].isVisible = True
                self.reveal_tile(posx + 1, posy + 1)

        elif(self.board[posx][posy].isVisible==False and self.board[posx][posy].isFlagged==False): #If tile is not revealded but has adjacent bombs just reveal tile
            self.board[posx][posy].isVisible = True

    """flagging a tile
    flagging all tiles will win game
    num of flagged cannot exceed number of bombs
    """
    def flag_tile(self, posx, posy):
        if(self.num_flagged<self.num_bombs and self.board[posx][posy].isFlagged == False):
            self.board[posx][posy].isFlagged= True
            self.num_flagged=self.num_flagged+1
        else:
            self.board[posx][posy].isFlagged = False
            self.num_flagged = self.num_flagged - 1