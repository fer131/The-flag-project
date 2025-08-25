import pygame
import consts
import soldier
import game_field
import screen
import database
import teleport


state = {
    "player_pos": soldier.soldier_pos,
    "player_body": [],
    "player_legs": [],
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "was_pressed": False
}

def main():
    pygame.init()
    game_field.create_grid()
    game_field.mine_placer(game_field.game_field)
    game_field.flag_indexes()
    teleport.trap_placer(game_field.game_field)
    print(teleport.trap_positions)
    print(teleport.traps)

    while state["is_window_open"]:

        handle_user_events()
        game_field.mine_indexes(game_field.game_field)

        if teleport.touching_trap(state):
            teleport.random_teleport(state)

        if game_field.touching_mine(state):
            state["state"] = consts.LOSE_STATE

        if game_field.touching_flag(state):
            state["state"] = consts.WIN_STATE


        soldier.soldier_pos = state["player_pos"]
        soldier.player_pos_calc(state)
        screen.draw_screen(state)

        if state["state"] == consts.SHOW_MINES:
            pygame.time.wait(1000)
            pygame.event.clear()
            state["was_pressed"] = True

            state["state"] = consts.RUNNING_STATE


def handle_user_events():
    global time_down
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not state["was_pressed"]:
                state["state"] = consts.SHOW_MINES
            if event.key == pygame.K_LEFT:
                soldier.soldier_left(state)
            if event.key == pygame.K_RIGHT:
                soldier.soldier_right(state)
            if event.key == pygame.K_UP:
                soldier.soldier_up(state)
            if event.key == pygame.K_DOWN:
                soldier.soldier_down(state)
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                             pygame.K_7, pygame.K_8, pygame.K_9
                             ]:
                time_down = pygame.time.get_ticks()
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                             pygame.K_7, pygame.K_8, pygame.K_9
                             ]:
                press_time = (pygame.time.get_ticks() - time_down) / 1000
                key = consts.KEYS_DICT[event.key]
                if press_time < 1:
                    database.load_game(key, state)
                else:
                    database.save_game(key, state, screen.grass_pos, game_field.game_field)




main()

