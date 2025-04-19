import fastf1
from fastf1.plotting import setup_mpl
import matplotlib.pyplot as plt

# === Configurazioni iniziali ===
fastf1.Cache.enable_cache('cache')   # Abilita la cache
setup_mpl(color_scheme='fastf1')     # Stile grafico ispirato alla F1

# === Parametri della session ===
year = 2023
gp = 'Monza'
session_type = 'Q'
driver_1 = 'HAM'
driver_2 = 'VER'

# === Caricamento dati ===
session = fastf1.get_session(year, gp, session_type)
session.load()

# === Estrazione giri più veloci ===
lap_1 = session.laps.pick_drivers(driver_1).pick_fastest()
lap_2 = session.laps.pick_drivers(driver_2).pick_fastest()

# === Telemetria con distanza ===
tel1 = lap_1.get_car_data().add_distance()
tel2 = lap_2.get_car_data().add_distance()

# === Plot ===
plt.figure(figsize=(10,5))   # Imposta dimensione del grafico

plt.plot(tel1['Distance'], tel1['Speed'], label=driver_1, linewidth=2)
plt.plot(tel2['Distance'], tel2['Speed'], label=driver_2, linewidth=2)

plt.title(f"Confronto velocità sul giro - {gp} {year} ({session_type})")
plt.xlabel('Distanza (m)')
plt.ylabel('Velocità (km/h)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()