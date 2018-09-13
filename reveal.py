import random


class Cla1:

    def make_board(self, x, y, z):  # c = x (width) d = y (height) e = z (num bombs)
        global board
        board = []
        # Declaration of board and adding rows/columns
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
        n = 0
        while n < z:
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
        count = 0

        if 0 <= posx-1 < x and 0 <= posy < y:  # Left
            if board[posx-1][posy] == "*":  # if the adjacent is the bomb
                count += 1

        if 0 <= posx+1 < x and 0 <= posy < y:  # Right
            if board[posx+1][posy] == "*":
                count += 1

        if 0 <= posx < x and 0 <= posy-1 < y:  # Up
            if board[posx][posy-1] == "*":
                count += 1

        if 0 <= posx < x and 0 <= posy+1 < y:  # Down
            if board[posx][posy+1] == "*":
                count += 1

        if 0 <= posx-1 < x and 0 <= posy-1 < y:  # Upper Left
            if board[posx-1][posy-1] == "*":
                count += 1

        if 0 <= posx-1 < x and 0 <= posy+1 < y:  # Lower Left
            if board[posx-1][posy+1] == "*":
                count += 1

        if 0 <= posx+1 < x and 0 <= posy-1 < y:  # Upper Right
            if board[posx+1][posy-1] == "*":
                count += 1

        if 0 <= posx+1 < x and 0 <= posy+1 < y:  # Lower Right
            if board[posx+1][posy+1] == "*":
                count += 1
        return count

    def check_isbomb(self, x, y, posx, posy):

        if 0 <= posx < x and 0 <= posy < y:  # make sure is not out of bound
            if board[posx][posy] == "*":
                return True
            else:
                return False

    def reveal_nums(self, x, y):
        l = 0
        for j in range(x):
            for i in range(y):
                if cla1.check_isbomb(x, y, i, j) is False:
                    board = cla1.recursion(i, j)
                else:
                    l = l

    def recursion(self, posx, posy):
        if cla1.search(posx, posy) == 0 and board[posx][posy] == "-":
            board[posx][posy] = "0"  # if revealing tile has 0 bomb adjacent & is unrevealed,reveal

            if 0 <= posx-1 < x and 0 <= posy < y:  # make sure is in the bound
                board[posx][posy] = "0"
                cla1.recursion(posx-1, posy)  # go through it again since there is no bomb adjacent on the first tile

            if 0 <= posx+1 < x and 0 <= posy < y:
                board[posx][posy] = "0"
                cla1.recursion(posx+1, posy)

            if 0 <= posx < x and 0 <= posy-1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx, posy-1)

            if 0 <= posx < x and 0 <= posy+1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx, posy+1)

            if 0 <= posx-1 < x and 0 <= posy-1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx-1, posy-1)

            if 0 <= posx-1 < x and 0 <= posy+1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx-1, posy-1)

            if 0 <= posx+1 < x and 0 <= posy-1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx+1, posy-1)

            if 0 <= posx+1 < x and 0 <= posy+1 < y:
                board[posx][posy] = "0"
                cla1.recursion(posx+1, posy+1)
        else:
            if cla1.search(posx, posy) == 0:
                board[posx][posy] = "0"
            else:
                board[posx][posy] = count
        return board


print("Welcome to Pysweeper!")
print("Input Board Attributes :)")
print("Width = ")
w = input()
print("Height = ")
h = input()
print("Number of Bombs =")
b = input()

while int(b) > (int(w)*int(h))-1:
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


print()
cla1.reveal_nums(x, y)
cla1.print_board()

print()
print("Now we can use gooey to reveal single tiles.")
print("Logic step 1: If tile is bomb, game over, and show board(reveal all tiles)")
print("Logic step 2-3: If tile > 0 and not bomb , reveal tile # at clicked position")
print("Logic step 2-3: If tile = 0 and not bomb, reveal tile(s)")
print("Logic step 4: If past logic step 1-3, loop till user (Wins|Loses). Won ->(if ALL_REVEALED=true then WON)")
