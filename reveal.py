print("Input x,y values")
print("X = ")
a = input()
print("Y = ")
b = input()
x = int(a)
y = int(b)
count = 0

# declaration and adding columns
board = []
for j in range(x):
    column = []
    for i in range(y):
        column.append("0")
    board.append(column)

# filling with data
for i in range(0, x):  # top and bottom row
    board[1][1] = "*"
    board[1][3] = "*"

for j in range(0, y):  # first and last column
    board[3][1] = "*"
    board[3][3] = "*"

cols = len(board)
rows = 0
if cols:
    rows = len(board[0])
for j in range(rows):
    for i in range(cols):
        print(board[i][j], end=" ")
    print()

print("Enter the position you want to reveal")
print("X =")
a = input()
print("Y= ")
b = input()
posx = int(a)
posy = int(b)


def check(posx,posy):
    global count
    if posx>=x or posy>=y or posx<0 or posy<0:
        print("can't reveal the position out of bound")
        status = False
    if board[posx][posy]=="*":
        print("game over")
        status = False
    if board[posx-1][posy]=="*":
        count+=1
    if board[posx+1][posy]=="*":
        count+=1
    if board[posx][posy-1]=="*":
        count+=1
    if board[posx][posy+1]=="*":
        count+=1
    if board[posx-1][posy-1]=="*":
        count+=1
    if board[posx+1][posy-1]=="*":
        count+=1
    if board[posx-1][posy+1]=="*":
        count+=1
    if board[posx+1][posy+1]=="*":
        count+=1

def reveal(posx,posy):
    if count == "0":
        reveal(posx,posy-1)
        reveal(posx,posy+1)
        reveal(posx-1,posy)
        reveal(posx+1,posy)
        reveal(posx-1,posy-1)
        reveal(posx-1,posy+1)
        reveal(posx+1,posy-1)
        reveal(posx+1,posy+1)
    else:
        board = check(posx,posy)



reveal(posx,posy)
board[posx][posy] = count
for j in range(rows):
    for i in range(cols):
        print(board[i][j], end=" ")
    print()
