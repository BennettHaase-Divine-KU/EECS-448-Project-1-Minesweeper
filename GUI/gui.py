# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

import pygame

pygame.init()
# definition of colors
WHITE = (255,255,255)
GREY = (211,211,211)
BLACK = (0,0,0)
DARKGREY = (169,169,169)
# tile width and height constant
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

#calculate screen size based of tile size
pygame.display.init()
#create the screen surface
w = input("Width?")
h = input("Height?")
screen_width = int(w)
screen_height = int(h)
size = screen_width, screen_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Minesweeper")

#main draw loop
program_end = False
font = pygame.font.SysFont('Ariel',16)

#looping multiple rects
row = screen_height//20
column = screen_width//20

while not program_end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_end = True
    screen.fill(DARKGREY)

    grid = [[0] * row for i in range(column) ]
    for i in range(row):
        for j in range(column):
           grid[j][i]  = pygame.draw.rect(screen,GREY,[(MARGIN+WIDTH)*j+MARGIN,(HEIGHT+MARGIN)*i+MARGIN,WIDTH,HEIGHT])
           screen.blit(font.render("1",True,BLACK),grid[j][i].center)
    pygame.display.flip()

pygame.quit()