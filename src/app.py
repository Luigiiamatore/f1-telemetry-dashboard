import streamlit as st
import matplotlib.pyplot as plt
from fastf1.plotting import setup_mpl

from data_loader import carica_sessione, get_fastest_lap_telemetry
from plot import plot_speed_comparison

setup_mpl(color_scheme='fastf1')
st.set_page_config(page_title="F1 Telemetry Dashboard", layout="wide")
st.title("\U0001F3C1 F1 Telemetry Dashboard")

# === Sidebar per selezione ===
with st.sidebar:
    st.header("Parametri")
    year = st.sidebar.selectbox("Selezione l'anno", list(range(2018, 2024))[::-1])
    gp = st.sidebar.selectbox("Gran Premio", ["Monza", "Spa", "Silverstone", "Bahrain"])
    session_type = st.sidebar.selectbox("Sessione", ["FP1", "FP2", "FP3", "Q", "R"])

    # === Caricamento sessione ===
    session = carica_sessione(year, gp, session_type)
    piloti_disponibili = session.laps['Driver'].unique().tolist()
    driver_1 = st.sidebar.selectbox("Primo pilota", piloti_disponibili, index = 0)
    driver_2 = st.sidebar.selectbox("Secondo pilota", piloti_disponibili, index = 1)

    genera = st.button("Genera grafico")

# === Generazione grafico ===
if genera:
    tel1 = get_fastest_lap_telemetry(driver_1, session)
    tel2 = get_fastest_lap_telemetry(driver_2, session)

    fig = plot_speed_comparison(tel1, tel2, driver_1, driver_2, gp, year, session_type)
    st.pyplot(fig)

    st.markdown(f"**{driver_1} vs {driver_2}** - {gp} {year} ({session_type})")