import pygame
import random
import consts


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



def draw_screen():
    screen.fill(consts.GREEN)
    for pos in random_grass():
        screen.blit(image,pos)
        pygame.display.flip()

running=True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        draw_screen()

pygame.quit()











