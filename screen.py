import pygame
import random
import consts
import guard
import soldier
import game_field
import teleport

CELL = consts.SPACE_BETWEEN_ITEMS
WIDTH = consts.WINDOW_WIDTH
HEIGHT=consts.WINDOW_HEIGHT

screen = pygame.display.set_mode((1000,500))

pygame.font.init()


imp = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(imp, consts.GRASS_SIZE)

mine = pygame.image.load("mine.png")
mine_img = pygame.transform.scale(mine, consts.MINE_SIZE)

flag=pygame.image.load("flag.png")
flag_img = pygame.transform.scale(flag, consts.FLAG_SIZE)


def random_grass():
    grass_positions=[]
    for i in range(consts.GRASS_NUMBER):
        x=random.randint(0,1000-consts.GRASS_SIZE[0])
        y=random.randint(0,500-consts.GRASS_SIZE[1])
        grass_positions.append((x,y))
    return grass_positions

grass_pos = random_grass()

def draw_grid(surface):
    for c in range(consts.GRID_COLS+1):
        x=c*CELL
        pygame.draw.line(surface,consts.GRID_LINE_COLOR,(x,0),(x,HEIGHT),1)
    for r in range(consts.GRID_ROWS+1):
        y=r*CELL
        pygame.draw.line(surface,consts.GRID_LINE_COLOR,(0,y),(WIDTH,y),1)

def draw_mines(field):
    counter_row = 0
    while counter_row < consts.GRID_ROWS:
        counter_col = 0
        while counter_col < consts.GRID_COLS:
            if field[counter_row][counter_col]["mine"]:
                screen.blit(mine_img, (field[counter_row][counter_col]["x"], field[counter_row][counter_col]["y"]))
                counter_col += 3
            else:
                counter_col += 1
        counter_row += 1

def draw_traps(field):
    counter_row = 0
    while counter_row < consts.GRID_ROWS:
        counter_col = 0
        while counter_col < consts.GRID_COLS:
            if field[counter_row][counter_col]["trap"]:
                screen.blit(teleport.trap_img, (field[counter_row][counter_col]["x"], field[counter_row][counter_col]["y"]))
                counter_col += 3
            else:
                counter_col += 1
        counter_row += 1


def get_flag_loc():
    cell = (game_field.calc_x(consts.GRID_COLS - consts.FLAG_ITEM_WIDTH, 0),
                              game_field.calc_y(consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT))
    return cell

def draw_flag(surface):
    pos = get_flag_loc()
    surface.blit(flag_img, pos)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen.blit(text_img, location)

def draw_welcome_message():
    draw_message(consts.WELCOME_MESSAGE,
                 consts.WELCOME_MESSAGE_SIZE, "white", consts.WELCOME_MESSAGE_POS)

def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE,
                 consts.WIN_LOSE_MESSAGE_SIZE, "white", consts.LOSE_WIN_MESSAGE_POS)

def draw_win_message():
    draw_message(consts.WIN_MESSAGE,
                 consts.WIN_LOSE_MESSAGE_SIZE, "white", consts.LOSE_WIN_MESSAGE_POS)

def draw_screen(states, guard_state):
    screen.fill(consts.GREEN)
    draw_welcome_message()

    if states["state"] == consts.SHOW_MINES:
        screen.fill(consts.BLACK)
        draw_grid(screen)
        draw_mines(game_field.game_field)
        draw_traps(game_field.game_field)
    else:
        for pos in grass_pos:
            screen.blit(grass_img, pos)
    draw_flag(screen)

    if states["state"] == consts.LOSE_STATE:
        draw_lose_message()

    if states["state"] == consts.WIN_STATE:
        draw_win_message()

    screen.blit(soldier.soldier, soldier.player_topleft_pixel(soldier.soldier_pos))
    screen.blit(guard.guard_img, guard.guard_topleft_pixel(guard_state))
    pygame.display.flip()
    if states["state"] == consts.LOSE_STATE or states["state"] == consts.WIN_STATE:
        pygame.time.wait(3000)
        states["is_window_open"] = False
































