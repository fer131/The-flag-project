import pygame
import consts
import game_field

imp = pygame.image.load("soldier.png")
soldier = pygame.transform.scale(imp, consts.SOLDIER_SIZE)

def player_pos_calc(states):
    states["player_body"].clear()
    states["player_legs"].clear()
    current_x = states["player_pos"][0]
    current_y = states["player_pos"][1]
    for j in range(0, consts.PLAYER_ITEM_HEIGHT - 1):
        for i in range(0, consts.PLAYER_ITEM_WIDTH):
            states["player_body"].append(tuple((current_x + i, current_y + j)))
    for i in range(2):
        states["player_legs"].append(tuple((current_x + i, current_y + consts.PLAYER_ITEM_HEIGHT - 1)))


