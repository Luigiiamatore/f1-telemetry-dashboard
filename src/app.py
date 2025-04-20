import streamlit as st
from fastf1.plotting import setup_mpl

from data_loader import get_grand_prix_list, carica_sessione, get_fastest_lap_telemetry
from plot import plot_telemetry_dashboard

setup_mpl(color_scheme='fastf1')

st.set_page_config(
    page_title="F1 Telemetry Dashboard", 
    page_icon="🏎️",
    layout="wide"
)
st.title("🏁 F1 Telemetry Dashboard")

# === Sidebar per selezione ===
with st.sidebar:
    st.header("Parametri")
    year = st.selectbox("Selezione l'anno", list(range(2018, 2024))[::-1])
    gp_list = get_grand_prix_list(year)
    gp = st.selectbox("Gran Premio", gp_list)
    session_type = st.selectbox("Sessione", ["FP1", "FP2", "FP3", "Q", "R"])

    round_number = gp_list.index(gp) + 1
    session = carica_sessione(year, round_number, session_type)

    piloti_disponibili = session.laps['Driver'].unique().tolist()
    driver_1 = st.selectbox("Primo pilota", piloti_disponibili, index=0)
    driver_2 = st.selectbox("Secondo pilota", piloti_disponibili, index=1)

    if st.button("Genera grafico"):
        st.session_state['genera'] = True

# === Generazione grafico ===
if st.session_state.get('genera', True):
    tel1 = get_fastest_lap_telemetry(driver_1, session)
    tel2 = get_fastest_lap_telemetry(driver_2, session)

    fig = plot_telemetry_dashboard(tel1, tel2, driver_1, driver_2, gp, year, session_type)

    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.plotly_chart(fig, use_container_width=True)