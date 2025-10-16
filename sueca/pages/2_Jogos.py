import streamlit as st
import pandas as pd
import os
from utils import load_games, show_games

st.title("Jogos")
# show games
games_df = load_games()
if games_df.empty:
    st.warning("Sem jogos disponiveis. Por favor adicionar jogos primeiro.")
else:

    round_number = st.selectbox("Ronda", ['Todas'] + list(games_df['Ronda'].unique()))
    if round_number == 'Todas':
        show_games(games_df)
    else:
        show_games(games_df.loc[games_df['Ronda'] == round_number])