# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids
from workspace.tile import tile
from workspace.executive import executive
from GUI.inputgui import inputGui
from tkinter import *

import pygame


def draw_main_board():
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
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
            if exe.gameBoard.board[j][i].isBomb == True and exe.gameBoard.board[j][i].isVisible == True:
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                temp = grid[j][i].move(-5, -5)
                screen.blit(bomb, temp)
            if exe.gameBoard.board[j][i].adjBomb > 0 and exe.gameBoard.board[j][i].isVisible == True:
                temp = grid[j][i].move(5, 5)
                screen.blit(font.render(str(exe.gameBoard.board[j][i].adjBomb), True, BLACK), (temp))
            if exe.gameBoard.board[j][i].isFlagged == True and exe.gameBoard.board[j][i].isVisible == False:
                screen.blit(flag, grid[j][i])
    pygame.display.flip()


def get_user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if(event.button == 1):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                if(c >= column):
                    c = column - 1
                if(r >= row):
                    r = row - 1
                print(c, r)
                exe.gameBoard.reveal_tile(c,r)

            elif(event.button == 3):
                pos = pygame.mouse.get_pos()
                c = pos[0] // (WIDTH + MARGIN)
                r = pos[1] // (HEIGHT + MARGIN)
                exe.gameBoard.flag_tile(c,r)
    return False


#Program Start
pygame.init()
pygame.display.init()

# definition of colors
WHITE = (255, 255, 255)
GREY = (211, 211, 211)
BLACK = (0, 0, 0)
DARKGREY = (169, 169, 169)


# tile width and height constant
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

# get board info
incorrect = True
try:
    while (incorrect == True):
        screen = Tk()
        inputScreen = inputGui(screen)
        screen.mainloop()
        board_width = inputScreen.getWidth()
        board_height = inputScreen.getHeight()
        board_bomb = inputScreen.getBombNum()
        if (board_width >= 2) and (board_height >= 2) and (board_bomb >= 1) and 1 <= ((board_width * board_height) - board_bomb) <= 1088:
            incorrect = False

except ValueError:
    board_width = 2
    board_height = 2
    board_bomb = 1
    pass


# calculate the required screen size based on amount of tiles
screen_width = (int(board_width) * 20) + ((int(board_width)+1)*5)
screen_height = (int(board_height) * 20) + ((int(board_height)+1)*5)

# create the screen surface
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pysweeper")
icon = pygame.image.load("MemoryLeakLogo.png")
pygame.display.set_icon(icon)
# create tile grid
board = [[tile() for i in range(int(board_width))]for j in range(int(board_height))]

# main draw loop
program_end = False
font = pygame.font.SysFont('Ariel', 22)

# looping multiple rects
row = int(board_height)
column = int(board_width)

# game logic grid
grid = [[0] * row for i in range(column)]
bomb = pygame.image.load("bomb.png")
flag = pygame.image.load("flag.png")


#Sets clock rate
clock = pygame.time.Clock()
exe = executive(int(board_height), int(board_width), int(board_bomb))
exe.run()
game_state = 0
while not program_end and game_state == 0:
    # game loop
    program_end = get_user_input()

    draw_main_board()
    game_state = exe.checkWinLose()
    clock.tick(60)


if (game_state == 2):
            print("YOU LOSE")
elif (game_state == 1):
            print("YOU WIN")
pygame.quit()
