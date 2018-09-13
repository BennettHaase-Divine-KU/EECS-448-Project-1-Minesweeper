from random import randint

def mine(n,bombs):
    board = createboard(n)
    board = addbombs(board,bombs)
    board = changenum(board)
    return board
def createtable(n):
    return[[0]*n for i in range(n)]

def addbombs(board, bombs):
    for i in range (bombs):
        isbomb = False
        while not isbomb:
                x = randint(0, len(table)-1)
                y = randint(0, len(table)-1)
                if board[x][y]!= "*":
                    board[x][y] = "*"
                isbomb = True
    return board


def changenum(board):
    for i in range(x):
        for j in range(y):
            if board[i][y]=="*":
                board = top(board,i,j)
                board = bottom(board,i,j)
                board = left(board,i,j)
                board = right(board,i,j)
                board = topleft(board,i,j)
                board = bottomleft(board,i,j)
                board = topright(board,i,j)
                board = bottomright(board,i,j)
    return board

def top(board,i,j):
    if i-1 >= 0:
        if board[i-1][j]=="*":
            board[i-1][j]+=1
    return board

def bottom(board,i,j):
    if i+1 < x:
        if board[i+1][j]=="*":
            board[i+1][j]+=1
    return board

def left(board,i,j):
    if j-1 >=0:
        if board[i][j-1]=="*":
            board[i][j-1]+=1
    return board

def right(board,i,j):
    if j+1 < y:
        if board[i][j+1]=="*":
            board[i][j+1]+=1
    return board

def topleft(board,i,j):
    if x-1>=0 and y-1>=0:
        if board[i-1][j-1]=="*":
            board[i-1][j-1]+=1
    return board

def bottomleft(board,i,j):
    if i+1<x and j-1>=0:
        if board[i+1][j-1]=="*":
            board[i+1][j-1]+=1
    return board

def topright(board,i,j):
    if i-1>=0 and j+1< y:
        if board[i-1][j+1]=="*":
            board[i-1][j+1]+=1
    return board

def bottomright(board,i,j):
    if i+1<x and j+1<y:
        if board[i+1][j+1]=="*":
            board[i+1][j+1]+=1
    return board

def pr(board):
    for i in board:
        print(i)
