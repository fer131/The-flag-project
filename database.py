import game_field
import screen
import pandas as pd

df = pd.read_csv("./database.csv")


def database_reset():
    x = [[(0, 0), [], [], False] for i in range(9)]
    df1 = pd.DataFrame(x, columns=['player_pos', 'field', 'bushes', 'was_pressed'])
    df1.to_csv('database.csv', index = False)

def save_game(num, states, bushes, field):
    row_num = num - 1
    df.at[row_num, 'player_pos'] = states["player_pos"]
    df.at[row_num, "field"] = field
    df.at[row_num, "bushes"] = bushes
    df.at[row_num, "was_pressed"] = states["was_pressed"]
    df.to_csv('database.csv', index=False)

def load_game(num, states):
    global df
    df = pd.read_csv("./database.csv")
    row_num = num - 1
    states["player_pos"] = eval(df.loc[row_num, "player_pos"])
    game_field.game_field = eval(df.loc[row_num, "field"])
    screen.grass_pos = eval(df.loc[row_num, "bushes"])
    states["was_pressed"] =  df.loc[row_num, "was_pressed"]
