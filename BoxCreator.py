import random
print("Input Board Attributes :)")
print("Width = ")
w = input()
print("Height = ")
h = input()
print("Number of Bombs =")
b = input()

x = int(w)+2
y = int(h)+2
z = int(b)

# declaration and adding columns
board = []
for j in range(x):
    column = []
    for i in range(y):
        column.append(0)
    board.append(column)

# filling with data
for i in range(0, x):  # top and bottom row
    board[i][0] = "B"
    board[i][y-1] = "B"

for j in range(0, y):  # first and last column
    board[0][j] = "B"
    board[x-1][j] = "B"

cols = len(board)
rows = 0
if cols:
    rows = len(board[0])
for j in range(rows):
    for i in range(cols):
        print(board[i][j], end=" ")
    print()

n=0
while n<z:
    e = random.randint(1, x-2)
    f = random.randint(1, y-2)
    if(board[e][f] == "X"):
        n = n
    else:
        board[e][f] = "X"
        n = n + 1

#print()

#rows = 0
#if cols:
#    rows = len(board[0])
#for j in range(rows):
#    for i in range(cols):
#        print(board[i][j], end=" ")
#    print()
