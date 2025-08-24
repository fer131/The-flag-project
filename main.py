import pygame
import consts
import soldier
import game_field
import screen

state = {
    "player_pos": soldier.soldier_pos,
    "player_body": [],
    "player_legs": [],
    "state": consts.RUNNING_STATE,
    "is_window_open": True,
    "flag_indexes": []
}

def main():
    pygame.init()
    game_field.create_grid()
    game_field.mine_placer(game_field.game_field)
    game_field.mine_indexes(game_field.game_field)
    game_field.flag_indexes(state)

    while state["is_window_open"]:

        handle_user_events()
        print(state["player_body"])
        print(state["flag_indexes"])
        if game_field.touching_mine(state):
            state["state"] = consts.LOSE_STATE
            state["is_window_open"] = False

        if game_field.touching_flag(state):
            state["state"] = consts.WIN_STATE
            state["is_window_open"] = False


        soldier.soldier_pos = state["player_pos"]
        soldier.player_pos_calc(state)
        screen.draw_screen(state)

        if state["state"] == consts.SHOW_MINES:
            pygame.time.wait(1000)
            pygame.event.clear()
            state["state"] = consts.RUNNING_STATE

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state["state"] = consts.SHOW_MINES
            if event.key == pygame.K_LEFT:
                soldier.soldier_left(state)
            if event.key == pygame.K_RIGHT:
                soldier.soldier_right(state)
            if event.key == pygame.K_UP:
                soldier.soldier_up(state)
            if event.key == pygame.K_DOWN:
                soldier.soldier_down(state)


main()