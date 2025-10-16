import streamlit as st
import pandas as pd
from utils import load_teams, get_championship, load_games, delete_games
import random
import numpy as np
from itertools import combinations

NUMBER_TEAMS_IN_GAME = 2

st.title("Gerar jogos do campeonato")
teams = load_teams()
num_teams = len(teams)

col1, col2 = st.columns([7, 3])
if col2.button("Apagar jogos existentes", ):
    delete_games()
    st.rerun()

if num_teams % NUMBER_TEAMS_IN_GAME != 0:
    st.error(f"O número de equipas deve ser um múltiplo de {NUMBER_TEAMS_IN_GAME}")

num_rounds = st.number_input("Número de rondas", min_value=1, step=1, value=1)

if st.button("Gerar jogos"):
    # check if games already exist
    games = load_games()
    if (games['Pontos E1'] > 0).any() or (games['Pontos E2']>0).any():
        st.warning("Já existem jogos adicionados. Por favor, apague os jogos existentes antes de gerar novos jogos.")
    else:
        num_games_per_round = num_teams // NUMBER_TEAMS_IN_GAME
        games = get_championship(list(teams['Nome Equipa']), len(teams) // 2, num_rounds, teams_per_game=NUMBER_TEAMS_IN_GAME)

    print_games = games[['Ronda', 'Equipa 1', 'Equipa 2']]
    # write dataframe using the entire length of the screen
    st.write(print_games)

