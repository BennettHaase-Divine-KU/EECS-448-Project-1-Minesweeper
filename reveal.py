import random


class Cla1:


    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        global board
        board = []
        # Declaration of board and adding posx/columns
        for j in range(x):
            column = []
            for i in range(y):
                column.append("-")
            board.append(column)
        return


    def print_board(self):
        cols = len(board)
        posxs = 0
        if cols:
            posxs = len(board[0])
        for j in range(posxs):
            for i in range(cols):
                print(board[i][j], end=" ")
            print()
        return board


    def place_bomb(self, z):
        n=0
        while n<z:
            e = random.randint(0, x-1)
            f = random.randint(0, y-1)
            if board[e][f] == "*":
                n = n
            else:
                board[e][f] = "*"
                n = n + 1
        return board


    def search(self, posx, posy):
        global count

        if posx-1<x and posx-1>=0 and posy<y and posy>=0:    #make sure is not out of bound
            if board[posx-1][posy]=="*":  #if the adjacent is the bomb
                count+=1

        if posx+1<x and posx+1>=0 and posy< y and posy>=0:
            if board[posx+1][posy]=="*":
                count+=1

        if posx<x and posx>=0 and posy-1< y and posy-1>=0:
            if board[posx][posy-1]=="*":
                count+=1

        if posx<x and posx>=0 and posy+1< y and posy+1>=0:
            if board[posx][posy+1]=="*":
                count+=1

        if posx-1<x and posx-1>=0 and posy-1< y and posy-1>=0:
            if board[posx-1][posy-1]=="*":
                count+=1

        if posx-1<x and posx-1>=0 and posy+1< y and posy+1>=0:
            if board[posx-1][posy+1]=="*":
                count+=1

        if posx+1<x and posx+1>=0 and posy-1< y and posy-1>=0:
            if board[posx+1][posy-1]=="*":
                count+=1

        if posx+1<x and posx+1>=0 and posy+1< y and posy+1>=0:
            if board[posx+1][posy+1]=="*":
                count+=1
        return count


        def reveal(self, posx, posy):
            if board[posx][posy]=="*":
                return False
            else:
                recursion(posx, posy)
                return True

        def recursion(self, posx, posy):
            if search(posx,posy)==0 and board[posx][posy]=="-": #if the tile you reveal has 0 bomb adjacentand is unrevealed,you can reveal
                board[posx][posy]="0"
                if posx-1<x and posx-1>=0 and posy<y and posy>=0: #make sure is in the bound
                    board[posx][posy]="0"
                    recursion(posx-1,posy) # go through it again since there is no bomb adjacent on the first tile

                if posx+1<x and posx+1>=0 and posy< y and posy>=0:
                    board[posx][posy]="0"
                    recursion(posx+1,posy)

                if posx<x and posx>=0 and posy-1< y and posy-1>=0:
                    board[posx][posy]="0"
                    recursion(posx,posy-1);

                if posx<x and posx>=0 and posy+1< y and posy+1>=0:
                    board[posx][posy]="0"
                    recursion(posx,posy+1)

                if posx-1<x and posx-1>=0 and posy-1< y and posy-1>=0:
                    board[posx][posy]="0"
                    recursion(posx-1,posy-1)

                if posx-1<x and posx-1>=0 and posy+1< y and posy+1>=0:
                    board[posx][posy]="0"
                    recursion(posx-1,posy-1)

                if posx+1<x and posx+1>=0 and posy-1< y and posy-1>=0:
                    board[posx][posy]="0"
                    recursion(posx+1,posy-1)

                if posx+1<x and posx+1>=0 and posy+1< y and posy+1>=0:
                    board[posx][posy]="0"
                    recursion(posx+1,posy+1)
            else:
                if search(posx,posy)==0:
                    board[posx][posy]="0"
                else:
                    board[posx][posy]= count
            return board


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


x = int(w)  # Width
y = int(h)  # Height
z = int(b)  # Number of bombs

cla1 = Cla1()
cla1.make_board(x, y, z)
cla1.place_bomb(z)
print()
cla1.print_board()

while True:

    print("Enter the position you want to reveal")
    print("X =")
    h = input()
    print("Y= ")
    i = input()
    posy = int(i)
    posx = int(h)

    if cla1.reveal(posx,posy)==False:
        print("Game Over!")
        break
