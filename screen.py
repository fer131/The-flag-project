import pygame

import consts


screen = pygame.display.set_mode((1000,500))
imp = pygame.image.load("grass.png")
image = pygame.transform.scale(imp, consts.GRASS_SIZE)

def random_grass():


    pass

def draw_screen():

    screen.fill(consts.GREEN)
    screen.blit(image, (0, 0))
    pygame.display.flip()
while True:
    draw_screen()





