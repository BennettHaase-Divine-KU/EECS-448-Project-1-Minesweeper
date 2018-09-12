import random
from tile import tile

class Board:

    def __init__(self):
        self.board = []

    #Initilises the board
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
    #Prints the board to terminal where hidden tiles are '?' and revealed tiles are either '*' or a num
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

    #Initilises the bombs on the board
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

    #reveals a tile at x,y
    def reveal_tile(self,x_pos,y_pos):
        self.board[x_pos][y_pos].isVisible=True;
        if(self.board[x_pos][y_pos].isBomb==True):
            return 2
        else:
            return 0

    #Prints a debug version of the board to terminal
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



