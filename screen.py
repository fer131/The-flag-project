import pygame
import random

from pygame.examples.moveit import WIDTH, HEIGHT

import consts

CELL = consts.SPACE_BETWEEN_ITEMS
WIDTH = consts.WINDOW_WIDTH
HEIGHT=consts.WINDOW_HEIGHT

screen = pygame.display.set_mode((1000,500))
imp = pygame.image.load("grass.png")
image = pygame.transform.scale(imp, consts.GRASS_SIZE)

def random_grass():
    grass_positions=[]
    for i in range(consts.GRASS_NUMBER):
        x=random.randint(0,1000-consts.GRASS_SIZE[0])
        y=random.randint(0,500-consts.GRASS_SIZE[1])
        grass_positions.append((x,y))
    return grass_positions

def draw_grid(surface):
    for c in range(consts.GRID_COLS+1):
        x=c*CELL
        pygame.draw.line(surface,consts.GRID_LINE_COLOR,(x,0),(x,HEIGHT),1)
    for r in range(consts.GRID_ROWS+1):
        y=r*CELL
        pygame.draw.line(surface,consts.GRID_LINE_COLOR,(0,y),(WIDTH,y),1)



def draw_screen():
    screen.fill(consts.GREEN)
    draw_grid(screen)



    pygame.display.flip()

running=True
while running:
    draw_screen()


def make_cells(r,c,horizontal,length):
    cells=[]
    if horizontal:
        for i in range(length):
            cells.append((r,c+i))
        else:
            for i in range(length):
                cells.append((r+i, c))
    return cells

def generate_mines():
    mines=[]
    occupied=set()
    while len(mines)<consts.MINE_COUNT:
        horizontally=random.choice([True,False])
        L=consts.MINE_LINE
        if horizontally:
            r=random.randint(0,consts.GRID_ROWS-1)
            c=random.randint(0,consts.GRID_COLS-1)
        else:
            r = random.randint(0, consts.GRID_ROWS - L)
            c = random.randint(0, consts.GRID_COLS - 1)

            cells=make_cells(r,c,horizontally,L)

            overlap=False
            for cell in cells:
                if cell in occupied:
                    overlap=True
                    break
                if overlap:
                    continue
            for cell in cells:
                occupied.add(cell)
                mines.append(cells)
    return mines

def draw_mines(surface, mines):
    for cells in mines:
        for(r,c) in cells:
            rect=pygame.rect(c*CELL,r*CELL,CELL,CELL)
            pygame.draw.rect(surface,consts.MINE_FILL_COLOR, rect)
            pygame.draw.rect(surface, consts.MINE_BORDER_COLOR, rect,1)






















