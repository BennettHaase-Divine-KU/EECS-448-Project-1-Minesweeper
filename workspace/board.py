import random
from tile import tile

class Board:

    def __init__(self):
        self.board = []

    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        # Declaration of board and adding row/columns
        self.width=x
        self.length=y
        self.num_bombs=z


        for j in range(self.width):
            column = []
            for i in range(self.length):
                column.append(tile())
            self.board.append(column)

        return

    def print_board(self):
        cols = len(self.board)
        rows = 0
        if cols:
            rows = len(self.board[0])
        for j in range(rows):
            for i in range(cols):
                print(self.board[i][j].getIsBomb(), end=" ")
            print()
        print()
        return self.board

    def place_bomb(self):
        n=0
        while n<self.num_bombs:
            e = random.randint(0, self.width-1)
            f = random.randint(0, self.length-1)
            if(self.board[e][f].getIsBomb() == True):
                n = n
            else:
                self.board[e][f].setIsBomb(True)
                n = n + 1
        return self.board

    def get_tile(self,x,y):
        return self.board[x][y]
