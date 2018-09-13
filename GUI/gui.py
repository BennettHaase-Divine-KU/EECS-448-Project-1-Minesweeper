# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

import pygame

pygame.init()
# definition of colors
WHITE = (255,255,255)
GREY = (211,211,211)
BLACK = (0,0,0)
DARKGREY = (169,169,169)
# grid width and height
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

pygame.display.init()
#create the screen surface
screen = pygame.display.set_mode((255,255))
pygame.display.set_caption("Minesweeper")

#main draw loop
program_end = False
font = pygame.font.SysFont('Ariel',16)

#looping multiple rects
row = 10
column = 10

while not program_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
    screen.fill(DARKGREY)

    grid = [[0] * 10 for i in range(10) ]
    for row in range(10):
        for column in range(10):
           grid[column][row]  = pygame.draw.rect(screen,GREY,[(MARGIN+WIDTH)*column+MARGIN,(HEIGHT+MARGIN)*row+MARGIN,WIDTH,HEIGHT])
           screen.blit(font.render("1",True,BLACK),grid[column][row])
    pygame.display.flip()   

pygame.quit()