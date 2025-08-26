import pygame
import consts

imp = pygame.image.load("snake.png")
guard_img = pygame.transform.scale(imp, consts.SOLDIER_SIZE)

guard_state = {
    "guard_pos": (0, 0),
    "guard_direction": "",
    "guard_positions": []
}

def guard_start(state):
    state["guard_pos"] = consts.GUARD_START_POS
    state["guard_direction"] = consts.GUARD_START_DIRECTION

def guard_positions(state):
    state["guard_positions"].clear()
    for i in range(4):
        for j in range(2):
            state["guard_positions"].append(tuple((i, j)))

def touching_guard(state, guard):
    for pos in state["player_legs"]:
        if pos in guard["guard_positions"]:
            return True
    return False

def guard_move(state):
    if state["guard_direction"] == "right":
        if state["guard_pos"] == (state["guard_pos"][0], consts.GRID_COLS - consts.PLAYER_ITEM_WIDTH):
            state["guard_direction"] = "left"
        else:
            state["guard_pos"] = tuple((state["guard_pos"][0],
                                          state["guard_pos"][1] + 1))
    else:
        if state["guard_pos"] == (state["guard_pos"][0], 0):
            state["guard_direction"] = "right"
        else:
            state["guard_pos"] = tuple((state["guard_pos"][0],
                                          state["guard_pos"][1] - 1))
