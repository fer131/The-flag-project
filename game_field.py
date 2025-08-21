import consts
import random
import copy

game_field = []

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
    counter = 0
    for i in range(0, consts.PLAYER_ITEM_HEIGHT):
        for j in range(consts.PLAYER_ITEM_WIDTH, consts.GRID_COLS - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][j]["mine"] = True
    for i in range(consts.PLAYER_ITEM_HEIGHT, consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT):
        for j in range(0, consts.GRID_COLS - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][j]["mine"] = True
    for i in range(consts.GRID_ROWS - consts.FLAG_ITEM_HEIGHT, consts.GRID_ROWS):
        for j in range(0, consts.GRID_COLS - consts.FLAG_ITEM_WIDTH - 2, 3):
            if random.randint(1, 100) <= consts.MINE_PERCENTAGE:
                field[i][j]["mine"] = True

    copy_grid = copy.deepcopy(field)

    for i in range(consts.GRID_ROWS):
        for j in range(consts.GRID_COLS - 2):
            if copy_grid[i][j]["mine"]:
                for k in range(1, 3):
                    field[i][j + k]["mine"] = True
    return counter




create_grid()
mine_placer(game_field)
print(game_field)
