import streamlit as st
from fastf1.plotting import setup_mpl

from data_loader import get_grand_prix_list, carica_sessione, get_fastest_lap_telemetry
from plot import plot_speed_comparison, plot_throttle_comparison, plot_brake_comparison

setup_mpl(color_scheme='fastf1')
st.set_page_config(page_title="F1 Telemetry Dashboard", layout="wide")
st.title("\U0001F3C1 F1 Telemetry Dashboard")

# === Sidebar per selezione ===
with st.sidebar:
    st.header("Parametri")
    year = st.sidebar.selectbox("Selezione l'anno", list(range(2018, 2024))[::-1])
    gp_list = get_grand_prix_list(year)
    gp = st.sidebar.selectbox("Gran Premio", gp_list)
    session_type = st.sidebar.selectbox("Sessione", ["FP1", "FP2", "FP3", "Q", "R"])
    tema = st.radio("Tema grafico", ["Chiaro", "Scuro"], index=1)

    # === Caricamento sessione ===
    round_number = gp_list.index(gp) + 1
    session = carica_sessione(year, round_number, session_type)
    piloti_disponibili = session.laps['Driver'].unique().tolist()
    driver_1 = st.sidebar.selectbox("Primo pilota", piloti_disponibili, index = 0)
    driver_2 = st.sidebar.selectbox("Secondo pilota", piloti_disponibili, index = 1)

    if st.button("Genera grafico"):
        st.session_state['genera'] = True

# === Generazione grafico ===
if st.session_state.get('genera', True):
    tel1 = get_fastest_lap_telemetry(driver_1, session)
    tel2 = get_fastest_lap_telemetry(driver_2, session)

    fig_speed = plot_speed_comparison(tel1, tel2, driver_1, driver_2, gp, year, session_type, tema)
    fig_throttle = plot_throttle_comparison(tel1, tel2, driver_1, driver_2, tema)
    fig_brake = plot_brake_comparison(tel1, tel2, driver_1, driver_2, tema)

    col1, col2, col3 = st.columns([1, 6, 1])    # margine sinistro, centrale, destro
    with col2:
        st.markdown(f"### {driver_1} vs {driver_2} - {gp} {year} ({session_type})")
        st.plotly_chart(fig_speed, use_container_width=True)
        st.plotly_chart(fig_throttle, use_container_width=True)
        st.plotly_chart(fig_brake, use_container_width=True)