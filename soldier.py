import pygame
import consts
import game_field

imp = pygame.image.load("soldier.png")
soldier = pygame.transform.scale(imp, consts.SOLDIER_SIZE)

soldier_pos = (0, 0)

def player_pos_calc(states):
    states["player_body"].clear()
    states["player_legs"].clear()
    current_x = states["player_pos"][0]
    current_y = states["player_pos"][1]
    for j in range(0, consts.PLAYER_ITEM_HEIGHT - 1):
        for i in range(0, consts.PLAYER_ITEM_WIDTH):
            states["player_body"].append(tuple((current_x + i, current_y + j)))
    for i in range(2):
        states["player_legs"].append(tuple((current_x + i,
                                            current_y + consts.PLAYER_ITEM_HEIGHT - 1)))

def player_topleft_pixel(pos):
    return tuple((game_field.calc_x(pos[0], 0), game_field.calc_y(pos[1])))

def soldier_left(states):
    if states["player_pos"][0] > 0:
        states["player_pos"] = tuple((states["player_pos"][0] - 1, states["player_pos"][1]))
def soldier_right(states):
    if states["player_pos"][0] < consts.GRID_COLS - 1:
        states["player_pos"] = tuple((states["player_pos"][0] + 1, states["player_pos"][1]))
def soldier_up(states):
    if states["player_pos"][1] > 0:
        states["player_pos"] = tuple((states["player_pos"][0], states["player_pos"][1] - 1))
def soldier_down(states):
    if states["player_pos"][1] < consts.GRID_ROWS:
        states["player_pos"] = tuple((states["player_pos"][0], states["player_pos"][1] + 1))


