import consts
import random
import copy

game_field = []
mine_index = []


def create_grid():
    global game_field
    game_field =[
    create_grid_row(row, row_start=0, row_length=consts.GRID_COLS)
        for row in
        range(consts.GRID_ROWS)
    ]

def create_grid_row(row_index, row_start, row_length):
    return [create_item(calc_x(col, row_start),
            calc_y(row_index)) for col in range(row_length)]

def calc_x(col, row_start):
    item_x = row_start + col * consts.SPACE_BETWEEN_ITEMS
    return item_x

def calc_y(row):
    return row * consts.SPACE_BETWEEN_ITEMS

def create_item(x, y):
    return {
        "x": x,
        "y": y,
        "mine": False
    }

def mine_placer(field):
    for i in range(0, consts.PLAYER_ITEM_HEIGHT):
        counter1 = consts.PLAYER_ITEM_WIDTH
        while counter1 < consts.GRID_COLS - 2:
        # for j in range(consts.PLAYER_ITEM_WIDTH, consts.GRID_COLS - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][counter1]["mine"] = True
                counter1 += 3
            else:
                counter1 += 1
    for i in range(consts.PLAYER_ITEM_HEIGHT, consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT):
        counter2 = 0
        while counter2 < consts.GRID_COLS - 2:
        # for j in range(0, consts.GRID_COLS - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][counter2]["mine"] = True
                counter2 += 3
            else:
                counter2 += 1
    for i in range(consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT, consts.GRID_ROWS):
        counter3 = 0
        while counter3 < consts.GRID_COLS - consts.FLAG_ITEM_WIDTH - 2:
        # for j in range(0, consts.GRID_COLS - consts.FLAG_ITEM_WIDTH - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][counter3]["mine"] = True
                counter3 += 3
            else:
                counter3 += 1

    copy_grid = copy.deepcopy(field)

    for i in range(consts.GRID_ROWS):
        for j in range(consts.GRID_COLS - 2):
            if copy_grid[i][j]["mine"]:
                for k in range(1, 3):
                    field[i][j + k]["mine"] = True


def mine_indexes(field):
    for row in range(consts.GRID_ROWS):
        for col in range(consts.GRID_COLS):
            if field[row][col]["mine"]:
                mine_index.append(tuple((row, col)))

def flag_indexes(states):
    start_pos = (consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT,
                 consts.GRID_COLS - consts.FLAG_ITEM_WIDTH)
    for i in range(consts.FLAG_ITEM_HEIGHT):
        for j in range(consts.FLAG_ITEM_WIDTH):
            states["flag_indexes"].append(tuple((start_pos[0] + i, start_pos[1] + j)))

def touching_flag(states):
    for pos in states["player_body"]:
        if pos in states["flag_indexes"]:
            return True
    return False

def touching_mine(states):
    for pos in states["player_legs"]:
        if pos in mine_index:
            return True
    return False

