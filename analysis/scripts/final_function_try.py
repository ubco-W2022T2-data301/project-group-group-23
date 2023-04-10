import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def player_per_game_processed(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and modify scope)
    df = (
        pd.read_csv('../data/raw/Player Per Game.csv')
        .drop(['birth_year', 'lg', 'ft_per_game', 'fta_per_game', 'ft_percent', 'stl_per_game', 'tov_per_game', 'pf_per_game'], axis=1)
        .dropna(subset=['fg_percent', 'x3p_percent', 'e_fg_percent'])
        .rename(columns={
            'seas_id': 'season_id',
            'player': 'player_name',
            'pos': 'position',
            'age': 'player_age',
            'experience': 'years_of_experience',
            'tm': 'team',
            'g': 'games_played',
            'gs': 'games_started',
            'mp_per_game': 'minutes_played_per_game',
            'fg_per_game': 'field_goals_per_game',
            'fga_per_game': 'field_goal_attempts_per_game',
            'fg_percent': 'field_goal_percentage',
            'x3p_per_game': 'three_pointers_per_game',
            'x3pa_per_game': 'three_point_attempts_per_game',
            'x3p_percent': 'three_point_percentage',
            'x2p_per_game': 'two_pointers_per_game',
            'x2pa_per_game': 'two_point_attempts_per_game',
            'x2p_percent': 'two_point_percentage',
            'e_fg_percent': 'effective_field_goal_percentage',
            'orb_per_game': 'offensive_rebounds_per_game',
            'drb_per_game': 'defensive_rebounds_per_game',
            'trb_per_game': 'total_rebounds_per_game',
            'ast_per_game': 'assists_per_game',
            'blk_per_game': 'blocks_per_game',
            'pts_per_game': 'points_per_game'
        })
    )
    # Method Chain 2 (Create new columns, drop others, and do processing)
    df1 = (
        df
        .loc[lambda x: x['season'] >= 1980]
        .loc[lambda df: (df['two_point_percentage'] != 0) & (df['two_point_percentage'] != 1)]
        .loc[lambda df: df['years_of_experience'] > 2]
    )
    
    # Return the last dataframe
    
    return df1

def load_and_process_per_game(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)
    df2 = (
        pd.read_csv('../data/raw/Player Per Game.csv')
        .drop(['birth_year', 'lg', 'ft_per_game', 'fta_per_game', 'ft_percent', 'stl_per_game', 'tov_per_game', 'pf_per_game'], axis=1)
        .dropna(subset=['fg_percent', 'x3p_percent', 'e_fg_percent'])
        .rename(columns={
            'seas_id': 'season_id',
            'player': 'player_name',
            'pos': 'position',
            'age': 'player_age',
            'experience': 'years_of_experience',
            'tm': 'team',
            'g': 'games_played',
            'gs': 'games_started',
            'mp_per_game': 'minutes_played_per_game',
            'fg_per_game': 'field_goals',
            'fga_per_game': 'field_goal_attempts_per_game',
            'fg_percent': 'field_goal_percentage',
            'x3p_per_game': 'three_pointers_per_game',
            'x3pa_per_game': 'three_point_attempts_per_game',
            'x3p_percent': 'three_point_percentage',
            'x2p_per_game': 'two_pointers_per_game',
            'x2pa_per_game': 'two_point_attempts_per_game',
            'x2p_percent': 'two_point_percentage',
            'e_fg_percent': 'effective_field_goal_percentage',
            'orb_per_game': 'offensive_rebounds_per_game',
            'drb_per_game': 'defensive_rebounds_per_game',
            'trb_per_game': 'total_rebounds_per_game',
            'ast_per_game': 'assists_per_game',
            'blk_per_game': 'blocks_per_game',
            'pts_per_game': 'points_per_game'
        })
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)
    df3 = (
        df2
        .loc[lambda x: x['season'] >= 1980]
        .assign(players=['Michael Jordan', 'DeMar DeRozan', 'Stephen Curry'])
        .merge(pd.read_csv("../data/processed/merged_cleaned.csv", index_col=[0])
               .loc[lambda df: df['player_name'].isin(['Michael Jordan', 'DeMar DeRozan', 'Stephen Curry'])]
               .loc[:, ['player_name', 'season', 'two_pointers']]
              )
    )
    
    # Return the last dataframe
    
    return df3