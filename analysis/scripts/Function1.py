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
            .set_precision(2)
            .set_table_styles(styles))
    
    
def display_averages_stats(df):
    # Group the dataframe by player_name and calculate the mean
    averages = df.groupby('player_name').mean()

    # Select only the columns we're interested in
    averages = averages[['points_per_game', 'three_point_percentage']]

    # Rename the columns to indicate that they represent averages
    averages = averages.rename(columns={
        'points_per_game': 'Avg Points Per Game',
        'three_point_percentage': 'Avg Three-Point Percentage'
    })

    # Format the table for better readability
    averages_formatted = averages.style.format({
        'Avg Points Per Game': '{:.1f}',
        'Avg Three-Point Percentage': '{:.3f}'
    }).set_caption("AVERAGES BY PLAYER")