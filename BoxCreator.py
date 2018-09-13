import random


class Cla1:


    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        global board
        board = []
        # Declaration of board and adding row/columns
        for j in range(x):
            column = []
            for i in range(y):
                column.append(0)
            board.append(column)
        return


    def print_board(self):
        cols = len(board)
        rows = 0
        if cols:
            rows = len(board[0])
        for j in range(rows):
            for i in range(cols):
                print(board[i][j], end=" ")
            print()
        return board


    def place_bomb(self, z):
        n=0
        while n<z:
            e = random.randint(0, x-1)
            f = random.randint(0, y-1)
            if board[e][f] == "9":
                n = n
            else:
                board[e][f] = "9"
                n = n + 1
        return board


    def check(self, posx, posy):
        global count
        if board[posx][posy] is not None and board[posx][posy]=="9":
            print("Game over")
        if board[posx-1][posy] is not None and board[posx-1][posy]=="9":
            board[posx][posy] += 1
        if board[posx+1][posy] is not None and board[posx+1][posy]=="9":
            board[posx][posy] += 1
        if board[posx][posy-1] is not None and board[posx][posy-1]=="9":
            board[posx][posy] += 1
        if board[posx][posy+1] is not None and board[posx][posy+1]=="9":
            board[posx][posy] += 1
        if board[posx-1][posy-1] is not None and board[posx-1][posy-1]=="9":
            board[posx][posy] += 1
        if board[posx+1][posy-1] is not None and board[posx+1][posy-1]=="9" :
            board[posx][posy] += 1
        if board[posx-1][posy+1] is not None and board[posx-1][posy+1]=="9":
            board[posx][posy] += 1
        if board[posx+1][posy+1] is not None and board[posx+1][posy+1]=="9":
            board[posx][posy] += 1


    def reveal(self, posx, posy):
            board = cla1.check(posx, posy)
            cla1.print_board()


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

x = int(w)  # Width
y = int(h)  # Height
z = int(b)  # Number of bombs

cla1 = Cla1()
cla1.make_board(x, y, z)
cla1.place_bomb(z)
print()
cla1.print_board()


print("Enter the position you want to reveal")
print("X =")
h = input()
print("Y= ")
i = input()
posy = int(i)
posx = int(h)

cla1.reveal(posx, posy)