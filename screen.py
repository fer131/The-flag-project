import pygame

import consts

screen = pygame.display.set_mode((1000,500))

def draw_screen():

    screen.fill(consts.GREEN)
    pygame.display.flip()
while True:
    draw_screen()


