import pygame
import consts
import game_field

imp = pygame.image.load("soldier.png")
soldier = pygame.transform.scale(imp, consts.SOLDIER_SIZE)

soldier_pos = (0, 0)

def player_pos_calc(states):
    states["player_body"].clear()
    states["player_legs"].clear()
    current_row = states["player_pos"][0]
    current_col = states["player_pos"][1]
    for j in range(0, consts.PLAYER_ITEM_HEIGHT - 1):
        for i in range(0, consts.PLAYER_ITEM_WIDTH):
            states["player_body"].append(tuple((current_row + j, current_col + i)))
    for i in range(2):
        states["player_legs"].append(tuple((current_row + consts.PLAYER_ITEM_HEIGHT - 1,
                                            current_col + i)))

def player_topleft_pixel(pos):
    return tuple((game_field.calc_x(pos[1], 0) - 10, game_field.calc_y(pos[0])))

def soldier_left(states):
    if states["player_pos"][1] > 0:
        states["player_pos"] = tuple((states["player_pos"][0], states["player_pos"][1] - 1))
def soldier_right(states):
    if states["player_pos"][1] < consts.GRID_COLS - consts.PLAYER_ITEM_WIDTH:
        states["player_pos"] = tuple((states["player_pos"][0], states["player_pos"][1] + 1))
def soldier_up(states):
    if states["player_pos"][0] > 0:
        states["player_pos"] = tuple((states["player_pos"][0] - 1, states["player_pos"][1]))
def soldier_down(states):
    if states["player_pos"][0] < consts.GRID_ROWS - consts.PLAYER_ITEM_HEIGHT:
        states["player_pos"] = tuple((states["player_pos"][0] + 1, states["player_pos"][1]))





# key_press_times ={}
#
# def handle_user_event():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             state["is_window_open"]=False
#
#         if event.type==pygame.KEYDOWN:
#             if event.key in [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,
#                              pygame.K_7,pygame.K_8,pygame.K_9
#                              ]:
#                 key_press_times[event.key] = pygame.time.get_ticks()
#
#
#         if event.type == pygame.KEYUP:
#             if event.key in key_press_times:
#                 press_time=pygame.time.get_ticks()-key_press_times[event.key]
#                 numbers_1_to_9=int(pygame.key.name(event.key))
#
#                 if press_time<1000:
#                     print(numbers_1_to_9)
#                     # loaded_case=database.load_game(numbers_1_to_9)
#                 #     if loaded_case:
#                 #         state.update(loaded_case)
#                 # else:
#                 #     print(numbers_1_to_9)
#                 #     # database.save_game(numbers_1_to_9,state)
#                 #
#                 # del key_press_times[event.key]
# handle_user_event()




