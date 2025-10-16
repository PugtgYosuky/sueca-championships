import streamlit as st
import pandas as pd
from utils import calculate_league_points

st.markdown(
    """
    <style>
    body {
        color: #111;
        background-color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Campeonato de sueca')
st.subheader('Pontuação')
points = calculate_league_points()
if points.empty:
    st.warning('Sem Jogos')
else:
    st.write(points)