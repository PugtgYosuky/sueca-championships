import pandas as pd
import os
import random
from itertools import combinations
import streamlit as st
import time
import numpy as np
TEAMS_CSV = 'data/teams.csv'
GAMES_CSV = 'data/games.csv'
GAMES_ORDER_CSV = 'data/games_order.csv'
POINTS_CSV = 'data/points.csv'

def load_teams():
    if os.path.exists(TEAMS_CSV):
        return pd.read_csv(TEAMS_CSV)
    else:
        return pd.DataFrame(columns=['team_id', 'Nome Equipa', 'Elemento A', 'Elemento B'])
    
def load_games():
    if os.path.exists(GAMES_CSV):
        return pd.read_csv(GAMES_CSV)
    else:
        # Create the CSV if it doesn't exist
        df = pd.DataFrame(columns=['Jogo', 'Ronda', 'Equipa 1', 'Equipa 2', 'Pontos E1', 'Pontos E2'])
        df.to_csv(GAMES_CSV, index=False)
        return df
    
def save_games(df):
    df.to_csv(GAMES_CSV, index=False)

def save_teams(df):
    df.to_csv(TEAMS_CSV, index=False)

def get_championship(teams, teams_per_round, num_rounds, teams_per_game):
    # generate championship
    schedule = None
    while schedule is None:
        try:
            schedule = generate_championship_schedule(teams, teams_per_round, num_rounds, teams_per_game)
        except ValueError:
            pass

    games = []
    for round, round_matches in enumerate(schedule):
        for match in round_matches:
            team1, team2 = match
            games.append({
                'Ronda': round+1,
                'Equipa 1': team1,
                'Equipa 2': team2,
                'Pontos E1': 0,
                'Pontos E2': 0,
                'Jogado' : False
            })
    df = pd.DataFrame(games)
    save_games(df)
    aux = df[['Ronda', 'Equipa 1', 'Equipa 2']].copy()
    aux.to_csv(GAMES_ORDER_CSV, index=False)
    return df

def generate_championship_schedule(teams, games_per_round, num_rounds, teams_per_game):
    # generate games for a match
    # Generate all possible matches
    all_matches = list(combinations(teams, teams_per_game))
    
    # Shuffle matches for randomness
    random.shuffle(all_matches)
    
    rounds = []
    used_matches = set()
    
    for _ in range(num_rounds):
        round_matches = []
        teams_played = set()
        
        for match in all_matches:
            team1, team2 = match
            
            # Check if teams have not played this round and match is not repeated
            if team1 not in teams_played and team2 not in teams_played and match not in used_matches:
                round_matches.append(match)
                teams_played.update([team1, team2])
                used_matches.add(match)
            
            # Stop once we have enough games for the round
            if len(round_matches) == games_per_round:
                break
        
        if len(round_matches) != games_per_round:
            raise ValueError("Unable to generate a valid schedule with the given constraints.")
        
        rounds.append(round_matches)
    
    return rounds


def show_games(games_df):
    games_df = games_df.copy()
    # games_df.columns = ['Ronda', 'Equipa 1', 'Equipa 2', 'Resultado Equipa 1', 'Resultado Equipa 2']
    st.write(games_df)

def delete_teams():
    os.remove(TEAMS_CSV)
    st.success('Todas as equipas foram eliminadas!')
    time.sleep(1)
    st.rerun()

def delete_games():
    os.remove(GAMES_CSV)
    os.remove(GAMES_ORDER_CSV)
    st.success('Todos os jogos foram eliminados!')
    time.sleep(1)

def save_points(df):
    df.to_csv(POINTS_CSV, index=True)

def calculate_league_points():
    games = load_games()
    teams = load_teams()
    points = {}
    # create team tuple
    for team in teams['Nome Equipa']:
        points[team] = {
            'Num. Jogos' : 0,
            'Pontos' : 0,
            'Num. Vitórias' : 0,
            'Num. Derrotas' : 0,
            'Num. Marcados' : 0,
            'Num. Sofridos' : 0,
            'Diferença' : 0
        }

    for game in games.iterrows():
        # get the teams and scores by their feature name
        team1 = game[1]['Equipa 1']
        team2 = game[1]['Equipa 2']
        team1_score = game[1]['Pontos E1']
        team2_score = game[1]['Pontos E2']


        if not game[1]['Jogado']:
            continue

        points[team1]['Num. Jogos'] += 1
        points[team2]['Num. Jogos'] += 1
        points[team1]['Num. Marcados'] += team1_score
        points[team2]['Num. Marcados'] += team2_score
        points[team1]['Num. Sofridos'] += team2_score
        points[team2]['Num. Sofridos'] += team1_score

        if team1_score > team2_score:
            points[team1]['Pontos'] += 2
            points[team1]['Num. Vitórias'] += 1
            points[team2]['Num. Derrotas'] += 1

        elif team2_score > team1_score:
            points[team2]['Pontos'] += 2
            points[team2]['Num. Vitórias'] += 1
            points[team1]['Num. Derrotas'] += 1

        else:
            points[team1]['Pontos'] += 1
            points[team2]['Pontos'] += 1
            
        points[team1]['Diferença'] = points[team1]['Num. Marcados'] - points[team1]['Num. Sofridos']
        points[team2]['Diferença'] = points[team2]['Num. Marcados'] - points[team2]['Num. Sofridos']


    points_df = pd.DataFrame(points).T
    try:
        points_df = points_df.reset_index(names='Equipa')
        points_df = points_df.sort_values(by=['Pontos', 'Diferença', 'Num. Marcados'], ascending=False)
        points_df.index = range(1, len(points_df) + 1)
        points_df.index.name = 'Posição'
        save_points(points_df)
    except:
        pass

    return points_df
        
