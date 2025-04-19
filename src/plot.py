import plotly.graph_objects as go

def plot_speed_comparison(tel1, tel2, driver_1, driver_2, gp, year, session_type, tema="Scuro"):
    theme = "plotly_dark" if tema == "Scuro" else "plotly_white"

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tel1['Distance'], y=tel1['Speed'],
        mode='lines',
        name=driver_1
    ))

    fig.add_trace(go.Scatter(
        x=tel2['Distance'], y=tel2['Speed'],
        mode='lines',
        name=driver_2
    ))

    fig.update_layout(
        template=theme,
        title=f"{driver_1} vs {driver_2} - {gp} {year} ({session_type})",
        xaxis_title="Distanza (m)",
        yaxis_title="Velocità (km/h)",
        height=500
    )

    return fig