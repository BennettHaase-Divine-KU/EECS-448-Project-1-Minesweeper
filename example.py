from random import randint

def mine(n,bombs):
    table = maketable(n)
    table = addbombs(table,bombs)
    table = changetable(table)
    return table

def maketable(n):
    return[[0]*n for i in range(n)]

def addbombs(table, bombs):
    for i in range (bombs):
        isbomb = False
        while not isbomb:
                x = randint(0, len(table)-1)
                y = randint(0, len(table)-1)
                if table[x][y]!= "*":
                    table[x][y] = "*"
                isbomb = True
    return table


def changetable(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j]=="*":
                table = top(table,i,j)
                table = bottom(table,i,j)
                table = left(table,i,j)
                table = right(table,i,j)
                table = topleft(table,i,j)
                table = bottomleft(table,i,j)
                table = topright(table,i,j)
                table = bottomright(table,i,j)
    return table

def top(table,i,j):
    if i-1 >= 0:
        if table[i-1][j]!="*":
            table[i-1][j]+=1
    return table

def bottom(table,i,j):
    if i+1 < len(table):
        if table[i+1][j]!="*":
            table[i+1][j]+=1
    return table

def left(table,i,j):
    if j-1 >=0:
        if table[i][j-1]!="*":
            table[i][j-1]+=1
    return table

def right(table,i,j):
    if j+1 < len(table):
        if table[i][j+1]!="*":
            table[i][j+1]+=1
    return table

def topleft(table,i,j):
    if i-1>=0 and j-1>=0:
        if table[i-1][j-1]!="*":
            table[i-1][j-1]+=1
    return table

def bottomleft(table,i,j):
    if i+1<len(table[i]) and j-1>=0:
        if table[i+1][j-1]!="*":
            table[i+1][j-1]+=1
    return table

def topright(table,i,j):
    if i-1>=0 and j+1< len(table):
        if table[i-1][j+1]!="*":
            table[i-1][j+1]+=1
    return table

def bottomright(table,i,j):
    if i+1<len(table[0]) and j+1<len(table):
        if table[i+1][j+1]!="*":
            table[i+1][j+1]+=1
    return table

def pr(table):
    for i in table:
        print(i)

print("Input x,y values")
print("X = ")
a = input()
print("Y = ")
b = input()
x = int(a)
y = int(b)

mine(x,y)
pr()
