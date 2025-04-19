import matplotlib.pyplot as plt

def plot_speed_comparison(tel1, tel2, driver_1, driver_2, gp, year, session_type, tema="Scuro"):
    if tema == "Scuro":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")

    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(tel1["Distance"], tel1["Speed"], label=driver_1, linewidth=2)
    ax.plot(tel2["Distance"], tel2["Speed"], label=driver_2, linewidth=2)
    
    ax.set_xlabel('Distanza (m)')
    ax.set_ylabel('Velocità (km/h)')
    ax.set_title(f"{driver_1} vs {driver_2} - {gp} {year} ({session_type})")
    ax.legend()
    ax.grid(True)

    return fig