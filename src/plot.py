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
        title=f"Speed comparison",
        xaxis_title="Distanza (m)",
        yaxis_title="Velocità (km/h)",
        height=500
    )

    return fig

def plot_throttle_comparison(tel1, tel2, driver_1, driver_2, tema="Scuro"):
    theme = "plotly_dark" if tema == "Scuro" else "plotly_white"

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tel1['Distance'], y=tel1['Throttle'],
        mode='lines',
        name=f"{driver_1} - Throttle"
    ))
    fig.add_trace(go.Scatter(
        x=tel2['Distance'], y=tel2['Throttle'],
        mode='lines',
        name=f"{driver_2} - Throttle"
    ))

    fig.update_layout(
        template=theme,
        title="Throttle comparison",
        xaxis_title="Distanza (m)",
        yaxis_title="Throttle (%)",
        height=500
    )

    return fig

def plot_brake_comparison(tel1, tel2, driver_1, driver_2, tema="Scuro"):
    theme = "plotly_dark" if tema == "Scuro" else "plotly_white"

    tel1['Brake'] = tel1['Brake'].astype(int)
    tel2['Brake'] = tel2['Brake'].astype(int)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=tel1['Distance'], y=tel1['Brake'],
        mode='lines',
        name=f"{driver_1} - Brake",
        line=dict(dash='dot')
    ))
    fig.add_trace(go.Scatter(
        x=tel2['Distance'], y=tel2['Brake'],
        mode='lines',
        name=f"{driver_2} - Brake",
        line=dict(dash='dot')
    ))

    fig.update_layout(
        template=theme,
        title="Brake comparison",
        xaxis_title="Distanza (m)",
        yaxis_title="Brake (on/off)",
        height=300,
        yaxis=dict(range=[-0.1, 1.1])
    )
    
    return fig