# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
from workspace.tile import tile
from workspace.executive import executive
from GUI.inputgui import inputGui
from tkinter import *

import pygame

def print_board():
    screen.fill(DARKGREY)
    for i in range(row):
        for j in range(column):
            color = GREY

            if exe.gameBoard.board[j][i].isVisible == False:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])

            if exe.gameBoard.board[j][i].isVisible == True:
                color = WHITE
                grid[j][i] =  pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.gameBoard.board[j][i].isBomb == True and exe.gameBoard.board[j][i].isVisible == True :
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.gameBoard.board[j][i].adjBomb >  0 and exe.gameBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5,5)
                screen.blit(font.render(str(exe.gameBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.gameBoard.board[j][i].isFlagged == True and exe.gameBoard.board[j][i].isVisible == False:
                screen.blit(flag,grid[j][i])
    pygame.display.flip()

pygame.init()
pygame.display.init()

"""definition of colors
"""
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
BLACK = (0, 0, 0)
DARKGREY = (169, 169, 169)

# tile width and height constant
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5



w=2
h=2
b=1
incorrect = True


while (incorrect == True):
    try:
        screen = Tk()
        inputScreen = inputGui(screen)
        screen.mainloop()
        w = int(inputScreen.getWidth())
        h = int(inputScreen.getHeight())
        b = int(inputScreen.getBombNum())
        if (w >= 2) and (h >= 2) and (b >= 1) and 1 <= ((w*h)-b) <= 1088:
            incorrect = False
        if(incorrect == True):
            raise ValueError()

        break;
    except ValueError:
        badCase = Tk()
        Label(badCase, text="Please enter a valid integer.\n1<Width<73 and 1<Height<41\nNumber of bombs smaller than width*height\nEmpty tiles <1089", ).grid(row=0)
        Button(badCase, text="Ok", command=badCase.destroy).grid(row=1)
        badCase.mainloop()





"""calculate the required screen size based on amount of tiles
"""
screen_width = (int(w) * 20) + ((int(w)+1)*5)
screen_height = (int(h) * 20) + ((int(h)+1)*5)

""" create the screen surface
"""
size =  screen_height, screen_width
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pysweeper")
icon = pygame.image.load("MemoryLeakLogo.png")
pygame.display.set_icon(icon)
"""create tile grid
"""
board = [[tile() for i in range(int(w))]for j in range(int(h))]

"""main draw loop
"""
program_end = False
font = pygame.font.SysFont('Ariel', 22)

"""looping multiple rects
"""
row = int(w)
column = int(h)

"""game logic grid
"""
grid = [[0] * row for i in range(column)]
bomb = pygame.image.load("bomb.png")
flag = pygame.image.load("flag.png")


"""Sets clock rate
"""
clock = pygame.time.Clock()
exe = executive(int(w), int(h), int(b))
exe.run()
gamestate = 0
while not program_end and gamestate == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                if(c >= column):
                    c = column - 1
                if(r >= row):
                    r = row - 1
                exe.gameBoard.reveal_tile(c,r)

            elif(event.button == 3):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                exe.gameBoard.flag_tile(c,r)
    print_board()
    gamestate = exe.checkWinLose()

    clock.tick(60)

if (gamestate == 2):
    exe.gameBoard.reveal_all()
    print_board()
    loseCase = Tk()
    Label(loseCase, text="YOU LOSE!!", ).grid(row=0)
    loseCase.mainloop()
elif (gamestate == 1):
    winCase = Tk()
    Label(winCase, text="YOU WIN!!", ).grid(row=0)
    winCase.mainloop()
pygame.quit()
