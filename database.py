import pandas as pd

df = pd.read_csv("./database.csv")


def database_reset():
    x = [[(0, 0), [], [], []] for i in range(9)]
    df1 = pd.DataFrame(x, columns=['player_pos', 'field', 'bushes', 'was_pressed'])
    df1.to_csv('database.csv', index = False)

def save_game(num, states, bushes, field):
    row_num = num - 1
    df.loc[row_num, "player_pos"] = states["player_pos"]
    df.loc[row_num, "field"] = field
    df.loc[row_num, "bushes"] = bushes
    df.loc[row_num, "was_pressed"] = states["was_pressed"]
    df.to_csv('database.csv', index=False)

def load_game(num, states, field, bushes):
    row_num = num - 1
    states["player_pos"] = df.loc[row_num, "player_pos"]
    field = df.loc[row_num, "field"]
    bushes = df.loc[row_num, "bushes"]
    states["was_pressed"] =  df.loc[row_num, "was_pressed"]

