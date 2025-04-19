import fastf1
import streamlit as st
import matplotlib.pyplot as plt

from fastf1.plotting import setup_mpl

fastf1.Cache.enable_cache('cache')
setup_mpl(color_scheme='fastf1')

st.title("🏁 F1 Telemetry Dashboard")

# === Sidebar per selezione ===
year = st.sidebar.selectbox("Selezione l'anno", list(range(2018, 2024))[::-1])
gp = st.sidebar.selectbox("Gran Premio", ["Monza", "Spa", "Silverstone", "Bahrain"])
session_type = st.sidebar.selectbox("Sessione", ["FP1", "FP2", "FP3", "Q", "R"])

# === Caricamento sessione ===
session = fastf1.get_session(year, gp, session_type)
session.load()

# === Selezione piloti (dinamica) ===
piloti_disponibili = session.laps['Driver'].unique().tolist()
driver_1 = st.sidebar.selectbox("Primo pilota", piloti_disponibili, index = 0)
driver_2 = st.sidebar.selectbox("Secondo pilota", piloti_disponibili, index = 1)

# === Bottone per eseguire ===
if st.sidebar.button("Genera grafico"):
    # === Estrazione giri più veloci ===
    lap_1 = session.laps.pick_drivers(driver_1).pick_fastest()
    lap_2 = session.laps.pick_drivers(driver_2).pick_fastest()

    # === Telemetria con distanza ===
    tel1 = lap_1.get_car_data().add_distance()
    tel2 = lap_2.get_car_data().add_distance()

    # === Plot ===
    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(tel1["Distance"], tel1["Speed"], label=driver_1, linewidth=2)
    ax.plot(tel2["Distance"], tel2["Speed"], label=driver_2, linewidth=2)
    
    ax.set_xlabel('Distanza (m)')
    ax.set_ylabel('Velocità (km/h)')
    ax.set_title(f"Confronto velocità sul giro - {gp} {year} ({session_type})")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
    #st.write(f"Confronto tra {driver_1} e {driver_2}")