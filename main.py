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
    "flag_indexes": [],
    "mine_indexes": []
}

def main():
    pygame.init()
    game_field.create_grid()
    game_field.mine_placer(game_field.game_field)
    game_field.mine_indexes(state, game_field.game_field)
    game_field.flag_indexes(state)
    print(state["flag_indexes"])

    while state["is_window_open"]:
        handle_user_events()
        soldier.player_pos_calc(state)
        screen.draw_screen()

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier.soldier_left(state)
            if event.key == pygame.K_RIGHT:
                soldier.soldier_right(state)
            if event.key == pygame.K_UP:
                soldier.soldier_up(state)
            if event.key == pygame.K_DOWN:
                soldier.soldier_down(state)

main()