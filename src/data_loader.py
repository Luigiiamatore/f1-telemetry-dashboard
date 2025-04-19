import fastf1
import streamlit as st

@st.cache_data
def get_grand_prix_list(year):
    schedule = fastf1.get_event_schedule(year)
    return schedule['EventName'].tolist()

@st.cache_data(show_spinner="Caricamento sessione...")
def carica_sessione(year, gp, session_type):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    return session

def get_fastest_lap_telemetry(driver, session):
    lap = session.laps.pick_drivers(driver).pick_fastest()
    telemetry = lap.get_car_data().add_distance()
    return telemetry