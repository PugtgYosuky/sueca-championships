import streamlit as st
import pandas as pd
import os
from utils import save_teams, load_teams, delete_teams

# File path for the CSV
CSV_FILE = 'data/teams.csv'

# Streamlit interface
st.title('Equipas')

# Load teams
teams_df = load_teams()

# Show current teams
st.subheader('Equipas em jogo')
if not teams_df.empty:
    st.dataframe(teams_df)
else:
    st.write('Sem equipas.')

# Add a new team
st.subheader('Adicionar Equipa')
with st.form('Adicionar Equipa'):
    team_name = st.text_input('Nome da Equipa')
    element_a = st.text_input('Element A')
    element_b = st.text_input('Element B')
    submitted = st.form_submit_button('Adicionar')

    if submitted:
        if team_name and element_a and element_b:
            new_team_id = len(teams_df) + 1 if not teams_df.empty else 1
            new_team = {
                'team_id': [new_team_id],
                'Nome Equipa': team_name,
                'Elemento A': element_a,
                'Elemento B': element_b,
            }
            teams_df = pd.concat([teams_df, pd.DataFrame(new_team)], ignore_index=True)
            save_teams(teams_df)
            st.success(f'Equipa "{team_name}" adicionada!')
            st.rerun()  # Refresh the page to show updated data
        else:
            st.error('Faltam campos obrigatorios')

# Edit or delete existing teams
st.subheader('Editar ou eliminar equipa')
if not teams_df.empty:
    selected_team = st.selectbox('Selecionar equipa', teams_df['Nome Equipa'])
    if selected_team:
        team_row = teams_df[teams_df['Nome Equipa'] == selected_team].iloc[0]
        with st.form('Editar Equipa'):
            team_name_edit = st.text_input('Nome da equipa', value=team_row['Nome Equipa'])
            element_a_edit = st.text_input('Elemento A', value=team_row['Elemento A'])
            element_b_edit = st.text_input('Elemento B', value=team_row['Elemento B'])
            edited = st.form_submit_button('Guardar alterações')

            if edited:
                teams_df.loc[teams_df['Nome Equipa'] == selected_team, 'Nome Equipa'] = team_name_edit
                teams_df.loc[teams_df['Nome Equipa'] == selected_team, 'Elemento A'] = element_a_edit
                teams_df.loc[teams_df['Nome Equipa'] == selected_team, 'Elemento B'] = element_b_edit
                save_teams(teams_df)
                st.success('Equipa atualizada!')
                st.rerun()

        # Delete team
        if st.button('Eliminar equipa'):
            teams_df = teams_df[teams_df['Nome Equipa'] != selected_team]
            save_teams(teams_df)
            st.success('Equipa eliminada!')
            st.rerun()
else:
    st.write('Sem equipas.')

if st.button('Apagar todas as equipas'):
    delete_teams()
