# 🃏 Naipes League — Sueca Championship App / App para Campeonato de Sueca

**Author:** Joana Simões  
**In:** Streamlit (Python)

---

## 🇬🇧 Description (EN)

**Naipes League** is a simple **Streamlit web app** for managing *Sueca* championships.  
It allows you to organize matches, manage teams, track results, and follow the league standings in real time.

This app is designed for *Sueca* enthusiasts who want an easy and efficient way to handle tournaments — from team creation to ranking updates.

---

### 🧭 App Pages Overview

| Page | Function |
|------|-----------|
| **Geral** | Displays the overall ranking of all teams based on their points and performance. |
| **Criar_Equipa** | Create or edit teams participating in the championship. |
| **Jogos** | View the results of all games across every round. |
| **Gerar_Jogos** | Automatically generate the list of games for the championship. Run this **once**, and only **after creating all the teams**. |
| **Adicionar_Resultados** | Add or update the results for each game after it has been played. |

---

### ⚙️ Steps to Run

1. Install dependencies from `requirements.txt`
2. Ensure there is a **`data`** folder — it should be **empty** on the first run
3. Run the app:

   ```bash
   cd sueca
   streamlit run Geral.py
   ```

---

### 🃏 Game Rules Implemented

- For each match:
  - Win → **2 points**
  - Draw → **1 point**
  - Loss → **0 points**
- Team ranking is based on:
  1. Points
  2. Goal / score difference
  3. Total goals / points scored

> ⚙️ You can modify the ranking logic in  
> **`utils.py > calculate_league_points`**

---

### 📂 Notes to Take Into Account

- The app’s interface and content are in **Portuguese**
- The **`data`** folder contains **all information** about matches and teams  
  - Initially empty  
  - Later stores the full championship state  
  - ⚠️ Be careful when editing or deleting raw files manually
- Once matches are added/edited:
  - You can’t mark them as “not played” again
  - The app doesn’t allow undoing changes
  - If it crashes, it will recover from the saved data files
- There is no “back” functionality — double-check before deleting or changing anything

---

## 🇵🇹 Descrição (PT)

**Naipes League** é uma aplicação web simples desenvolvida em **Streamlit** para gerir campeonatos de *Sueca*.  
Permite organizar jogos, acompanhar classificações e gerir equipas de forma fácil e intuitiva.

Esta app foi criada para fãs de Sueca que queiram uma forma prática e rápida de gerir torneios — desde a criação das equipas até à atualização das classificações.

---

### 🧭 Páginas da Aplicação

| Página | Função |
|--------|--------|
| **Geral** | Mostra a classificação geral das equipas com base nos pontos e desempenho. |
| **Criar_Equipa** | Permite criar e editar as equipas participantes no campeonato. |
| **Jogos** | Mostra os resultados de todos os jogos em todas as jornadas. |
| **Gerar_Jogos** | Gera automaticamente os jogos do campeonato. Executar **apenas uma vez**, e **depois de criar todas as equipas**. |
| **Adicionar_Resultados** | Permite adicionar ou atualizar os resultados de cada jogo após serem jogados. |

---

### ⚙️ Passos para Executar

1. Instalar as dependências do ficheiro `requirements.txt`
2. Garantir que existe uma pasta chamada **`data`**, inicialmente **vazia**
3. Correr a aplicação:

   ```bash
   cd sueca
   streamlit run Geral.py
   ```

---

### 🃏 Regras do Jogo Implementadas

- Em cada jogo:
  - Vitória → **2 pontos**
  - Empate → **1 ponto**
  - Derrota → **0 pontos**
- A ordenação das equipas no campeonato é feita por:
  1. Pontos
  2. Diferença de “golos” / pontos por jogo
  3. Número total de “golos” / pontos marcados

> ⚙️ É possível alterar a lógica de ordenação no ficheiro  
> **`utils.py > calculate_league_points`**

---

### 📂 A Ter em Conta

- Todo o conteúdo da aplicação está em **português**
- A pasta **`data`** guarda **toda a informação** sobre jogos e equipas  
  - Inicialmente estará vazia  
  - Depois passa a conter o estado atual do campeonato  
  - ⚠️ Tenha cuidado ao editar ou eliminar ficheiros desta pasta!
- Após adicionar ou editar jogos:
  - Não é possível definir novamente um jogo como “não jogado”
  - A aplicação **não permite desfazer ações anteriores**
  - Caso a app vá abaixo, recupera o estado guardado nos ficheiros
- A aplicação não possui navegação “para trás” — confirme sempre antes de eliminar ou modificar dados
