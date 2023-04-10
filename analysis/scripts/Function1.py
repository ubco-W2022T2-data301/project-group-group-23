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

def clean_advanced_stats(url_or_path_to_csv_file):
    # Load the data and select columns
    advanced_stats = (pd.read_csv(url_or_path_to_csv_file)
                      [['player_name', 'season', 'position', 'minutes_played', 'true_shooting_percentage', 'offensive_win_shares',  'box_plus_minus']]
                      .loc[lambda x: x['minutes_played'] >= 500])

    # Calculate the upper and lower bounds for filtering outliers
    q1 = advanced_stats[['true_shooting_percentage', 'offensive_win_shares', 'box_plus_minus']].quantile(0.25)
    q3 = advanced_stats[['true_shooting_percentage', 'offensive_win_shares', 'box_plus_minus']].quantile(0.75)
    iqr = q3 - q1
    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr

    # Filter the dataframe to remove outliers
    advanced_stats = (advanced_stats
                      .loc[(lambda x: x['true_shooting_percentage'].between(lower_bound['true_shooting_percentage'], upper_bound['true_shooting_percentage'])) &
                           (lambda x: x['offensive_win_shares'].between(lower_bound['offensive_win_shares'], upper_bound['offensive_win_shares'])) &
                           (lambda x: x['box_plus_minus'].between(lower_bound['box_plus_minus'], upper_bound['box_plus_minus']))])

    # Replace a value within the dataframe
    advanced_stats = (advanced_stats
                      .replace({'position': {'Isaiah Thomas': 'PG'}}))

    return advanced_stats
