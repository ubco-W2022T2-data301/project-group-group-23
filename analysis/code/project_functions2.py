import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process_team_totals(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)
    df1 = (
        pd.read_csv('../data/raw/Team Totals.csv')
        .drop(['lg', 'playoffs', 'mp', 'ft', 'fta', 'ft_percent', 'stl', 'tov', 'pf'], axis=1)
        .dropna(subset=['abbreviation'])
        .rename(columns={
            'seas': 'season', 
            'lg': 'league', 
            'team': 'team', 
            'abbreviation': 'team_abbreviation',
            'g': 'games_played',
            'fg': 'field_goals',
            'fga': 'field_goal_attempts',
            'fg_percent': 'field_goal_percentage',
            'x3p': 'three_pointers',
            'x3pa': 'three_point_attempts',
            'x3p_percent': 'three_point_percentage',
            'x2p': 'two_pointers',
            'x2pa': 'two_point_attempts',
            'x2p_percent': 'two_point_percentage',
            'orb': 'offensive_rebounds',
            'drb': 'defensive_rebounds',
            'trb': 'total_rebounds',
            'ast': 'assists',
            'blk': 'blocks',
            'pts': 'points'
        })
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)
    df2 = (
        df1
        .loc[lambda x: x['season'] >= 1980]
        .assign(three_point_attempts_per_game=lambda x: x['three_point_attempts'] / x['games_played'],
            three_point_made_per_game=lambda x: x['three_point_percentage'] * x['three_point_attempts_per_game'])
    )
    
    # Return the last dataframe
    
    return df2

def load_and_process_per_game(url_or_path_to_csv_file):
    # Method Chain 1 (Load data and deal with missing data)
    df3 = (
        pd.read_csv('../data/raw/Player Per Game.csv')
        .drop(['birth_year', 'lg', 'ft_per_game', 'fta_per_game', 'ft_percent', 'stl_per_game', 'tov_per_game', 'pf_per_game'], axis=1)
        .dropna(subset=['fg_percent', 'x3p_percent', 'x2p_percent', 'e_fg_percent'])
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
    df4 = (
        df3
        .loc[lambda x: x['season'] >= 1980]
        .assign(
            three_pointers_to_attempts_ratio=lambda x: x['three_point_attempts_per_game'] / x['games_played'],
            adjusted_three_point_percentage=lambda x: x['three_point_percentage'] * 1.5
        )
    )
    
    # Return the last dataframe
    
    return df4