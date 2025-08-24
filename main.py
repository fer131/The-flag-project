import pygame
import consts
import soldier
import game_field

state = {
    "player_pos": (0, 0),
    "player_body": [],
    "player_legs": [],
    "state": consts.RUNNING_STATE,
    "is_window_open": True
}

def main():
    pygame.init()
    while True:
        handle_user_events()
        soldier.player_pos_calc(state)
        print(state["player_body"])
        print(state["player_legs"])



def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")
            if event.key == pygame.K_UP:
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")


main()