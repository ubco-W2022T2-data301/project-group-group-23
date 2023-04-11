import pandas as pd
import matplotlib.pyplot as plt

def select_player_stats(url_or_path_to_csv_file):
    # Read in the data and select only the relevant columns and players
    df = (
        pd.read_csv('../data/processed/player_per_game_cleaned.csv')
        .loc[lambda x: x['player_name'].isin(['Stephen Curry', 'Ray Allen', 'Reggie Miller'])]
        [['player_name', 'season', 'points_per_game', 'three_point_percentage', 'games_played']]
        .loc[lambda x: (x['points_per_game'] >= 5) & ((x['points_per_game'] <= 40) | (x['points_per_game'] >= 30))]
    )
    return df

from IPython.display import display

def display_player_stats(player_stats):
    styles = [
        {'selector': 'caption', 'props': [('font-size', '16px'), ('color', 'blue')]},
        {'selector': 'th', 'props': [('background-color', 'lightgray'), ('border', '2px solid black'), ('font-weight', 'bold')]},
        {'selector': 'td', 'props': [('border', '1px solid black')]}
    ]
    display(player_stats.style.set_caption('Player Stats Summary')
            .set_table_styles(styles))
    
