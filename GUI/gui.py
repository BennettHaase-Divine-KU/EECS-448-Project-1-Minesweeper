# import the pygame library, all this learned from
# http://programarcadegames.com/index.php?lang=en&chapter=array_backed_grids

import pygame

# definition of colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
# grid width and height
WIDTH = 20
HEIGHT = 20

# margin between tiles
MARGIN = 5

#2D array for the grid
grid = []

for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

grid[1][5] = 1

pygame.init()

WINDOW_SIZE = (255,255)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Minesweeper")

done = False

clock = pygame.time.Clock()

while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)

            grid[row][column] = 1
            print("Click", pos, "Grid Coordinates: ", row, column)

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color, [(MARGIN+WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN,
                                             WIDTH,HEIGHT   ])
    clock.tick(60)

    pygame.display.flip()

pygame.quit()