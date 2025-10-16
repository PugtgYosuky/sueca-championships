import streamlit as st
import pandas as pd
import os
from utils import load_teams, load_games, save_games
import time

# File paths


# Streamlit App
st.title("Informação de Jogos")

# Load teams and games
teams_df = load_teams()
games_df = load_games()

# Check if there are teams available
if teams_df.empty:
    st.warning("Sem equipas disponiveis. Por favor adicionar equipas primeiro.")
else:
    # Add a New Game
    st.subheader("Adicionar jogo")
    list_games = [('Equipa', 'Equipa', '')] + [(team1, team2, round) for team1, team2, round in zip(games_df['Equipa 1'], games_df['Equipa 2'], games_df['Ronda'])]
    team1, team2, round = st.selectbox('Equipas', list_games, format_func=lambda x: f'[Ronda {x[2]}] {x[0]} vs {x[1]}', index=0)
    selected_game = games_df.loc[(games_df["Equipa 1"] == team1) & (games_df["Equipa 2"] == team2)]
    
    if selected_game.empty == False:
        with st.form("add_game_form"):
            team1_score = st.number_input(f'Pontuação da equipa {team1}', value = selected_game['Pontos E1'].values[0], step=1)
            team2_score = st.number_input(f'Pontuação da equipa {team2}', value = selected_game['Pontos E2'].values[0], step=1)
            
            if st.form_submit_button("Adicionar jogo"):
                # change games results
                games_df.loc[(games_df['Equipa 1'] == team1) & (games_df['Equipa 2'] == team2), 'Pontos E1'] = team1_score
                games_df.loc[(games_df['Equipa 1'] == team1) & (games_df['Equipa 2'] == team2), 'Pontos E2'] = team2_score
                games_df.loc[(games_df['Equipa 1'] == team1) & (games_df['Equipa 2'] == team2), 'Jogado'] = True
                save_games(games_df)
                st.success("Jogo adicionado com sucesso!")
                time.sleep(1)
                st.rerun()