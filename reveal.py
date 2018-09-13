mport random


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
            if board[e][f] == "*":
                n = n
            else:
                if board[e][f] is not None:
                    board[e][f] = "*"
                    n = n + 1
        return board

    def check_isbomb(self, posx, posy):

        if board[posx][posy] == "*":
            return True
        else:
            return False

    def check(self, posx, posy, x, y):

        if board[posx][posy] == "*":
            y = y

        if posx <= x and board[posx+1][posy] is not 'null' and board[posx+1][posy] is "*":  # right
            board[posx][posy] += 1
            print ("true")

        if posx <= x and posy <= y and board[posx + 1][posy + 1] is "*":  # lower right
            board[posx][posy] += 1

        if posy <= y and board[posx][posy + 1] is "*":  # down
            board[posx][posy] += 1

        if posx >= 1 and board[posx-1][posy] is "*":  # left
            board[posx][posy] += 1

        if posx >= 1 and posy <= y and board[posx - 1][posy + 1] is "*":  # lower left
            board[posx][posy] += 1

        if posx >= 1 and posy >= 1 and board[posx-1][posy-1] is "*":  # upper left
            board[posx][posy] += 1

        if posy >= 1 and board[posx][posy-1] is "*":  # up
            board[posx][posy] += 1

        if posx <= x and posy >= 1 and board[posx+1][posy-1] is "*":  # upper right
            board[posx][posy] += 1

    def loop_check(self, x, y):
        l=0
        print()
        for j in range(x):
            for i in range(y):
                if cla1.check_isbomb(i, j) == False:
                    board = cla1.check(i, j, x, y)
                else:
                    l=l



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

""""
print("Enter the position you want to reveal")
print("X =")
h = input()
print("Y= ")
i = input()
posy = int(i)
posx = int(h)
"""
cla1.loop_check((x-1), (y-1))
print()
cla1.print_board()
print()
print("Now we can use gooey to reveal single tiles.")
print("Logic step 1: If tile is bomb, game over, and show board(reveal all tiles)")
print("Logic step 2-3: If tile > 0 and not bomb , reveal tile # at clicked position")
print("Logic step 2-3: If tile = 0 and not bomb, reveal tile(s)")
print("Logic step 4: If made it pasted logic step 1-3 then loop until user either wins or loses. Wins ->(if ALL_REVEALED= true then YOU WIN...")
