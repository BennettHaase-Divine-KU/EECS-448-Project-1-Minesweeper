import random


class Cla1:

    def __init__(self):
        self.board = []

    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        # Declaration of board and adding row/columns

        for j in range(x):
            column = []
            for i in range(y):
                column.append(0)
            self.board.append(column)

        # Filling with data (Creating a Border)
        for i in range(0, x):  # top and bottom row
            self.board[i][0] = "B"
            self.board[i][y-1] = "B"

        for j in range(0, y):  # first and last column
            self.board[0][j] = "B"
            self.board[x-1][j] = "B"

        return


    def print_board(self):
        cols = len(self.board)
        rows = 0
        if cols:
            rows = len(self.board[0])
        for j in range(rows):
            for i in range(cols):
                print(self.board[i][j], end=" ")
            print()

        return self.board


    def place_bomb(self, z):
        n=0
        while n<z:
            e = random.randint(1, x-2)
            f = random.randint(1, y-2)
            if(self.board[e][f] == "X"):
                n = n
            else:
                self.board[e][f] = "X"
                n = n + 1

        return self.board


print("Welcome to Pysweeper!")
print("Input Board Attributes :)")
print("Width = ")
w = input()
print("Height = ")
h = input()
print("Number of Bombs =")
b = input()
while int(b)>(int(w)*int(h))-1:
    print("Error enter a valid number of Bombs.")
    b = input()

print()

x = int(w)+2  # Width
y = int(h)+2  # Height
z = int(b)  # Number of bombs


cla1 = Cla1()
cla1.make_board(x, y, z)
cla1.print_board()
cla1.place_bomb(z)
print()
cla1.print_board()