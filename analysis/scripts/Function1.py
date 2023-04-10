import pandas as pd
import matplotlib.pyplot as plt

def select_player_stats(url_or_path_to_csv_file):
    # Read in the data and select only the relevant columns and players
    df = (
        pd.read_csv('../data/processed/player_per_game_cleaned.csv')
        .loc[lambda x: x['player_name'].isin(['Stephen Curry', 'Ray Allen', 'Reggie Miller'])]
        [['player_name', 'season', 'points_per_game', 'three_point_percentage', 'games_played']]
    )
    # Filter out any extreme outliers based on the points_per_game column
    # Here, we assume any score below 5 or above 40 is an outlier,
    # but any score between 30 and 40 is not an outlier
    df = df.loc[lambda x: (x['points_per_game'] >= 5) & ((x['points_per_game'] <= 40) | (x['points_per_game'] >= 30))]
    return df

