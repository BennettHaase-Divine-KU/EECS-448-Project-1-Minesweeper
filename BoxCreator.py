x = 10
y = 10

board = []
for j in range(x):
    column = []
for i in range(y):
    column.append(0)
    board.append(column)

# filling with data
for i in range(0, x): # top and bottom row
     board[i][0] = 1
     board[i][y-1] = 1

for j in range(0, y): # first and last column
    board[0][j] = 1
    board[x-1][j] = 1

    cols = len(board)
    rows = 0

    if cols:
        rows = len(board[0])
        for j in range(rows):
            print()
            for i in range(cols):
                print(board[i][j], end = "")

