import pygame
import consts
import random

imp = pygame.image.load("teleport.png")
trap_img = pygame.transform.scale(imp, consts.MINE_SIZE)

trap_positions = []
traps = []

def trap_placer(field):
    trap_count = consts.TRAP_COUNT
    while trap_count > 0:
        can_place = True
        random_row = random.randint(4, 20)
        random_col = random.randint(0, consts.GRID_COLS - 4)

        for i in range(3):
            if field[random_row][random_col + i]["mine"] or field[random_row][random_col + i]["trap"]:
                can_place = False

        if can_place:
            trap_list = []
            for i in range(3):
                field[random_row][random_col + i]["trap"] = True
                trap_list.append(tuple((random_row, random_col + i)))
            traps.append(trap_list)
            trap_count -= 1

def trap_indexes(trap_list):
    for trap in trap_list:
        for index in trap:
            trap_positions.append(index)

def touching_trap(states):
    for pos in states["player_legs"]:
        if pos in trap_positions:
            return True
    return False

def random_teleport(states):
    choice = random.choice(traps)
    for pos in states["player_legs"]:
        if pos in choice:
            choice = random.choice(traps)
    else:
        states["player_pos"] = tuple((choice[0][0] - consts.PLAYER_ITEM_HEIGHT, choice[0][1]))
