# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

import pygame

pygame.init()
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

# calculate screen size based of tile size
pygame.display.init()
# create the screen surface
w = input("Width?")
h = input("Height?")
screen_width = int(w)
screen_height = int(h)
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")

# main draw loop
program_end = False
font = pygame.font.SysFont('Ariel', 22)

# looping multiple rects
row = (screen_height // 20)
column = (screen_width // 20)

# game logic grid
gamelogic = [[0] * row for i in range(column)]
grid = [[0] * row for i in range(column)]
bomb = pygame.image.load("bomb.png")
# TODO: Set the clock rate to a specific FPS

while not program_end:
    # TODO: Click will reveal the tile
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = pos[0] // (WIDTH + MARGIN)
            r = pos[1] // (HEIGHT + MARGIN)
            gamelogic[c][r] = 9
            print("Click", pos, "Grid coordinates: ", r, c)
    screen.fill(DARKGREY)
    #TODO: add in cases for flagging, bombs, 1-4
    for i in range(row):
        for j in range(column):
            color = GREY

            grid[j][i] = pygame.draw.rect(screen, color,
                                          [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                           HEIGHT])
            if gamelogic[j][i] == 1:
                color = WHITE
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                screen.blit(font.render("1", True, BLACK), (grid[j][i]))
            if gamelogic[j][i] == 9:
                color = WHITE
                temp = grid[j][i].move(-5,-5)
                grid[j][i] = pygame.draw.rect(screen, color,
                                              [(MARGIN + WIDTH) * j + MARGIN, (HEIGHT + MARGIN) * i + MARGIN, WIDTH,
                                               HEIGHT])
                screen.blit(bomb,temp)
    pygame.display.flip()

pygame.quit()
