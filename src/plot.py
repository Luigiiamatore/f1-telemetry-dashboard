from plotly.subplots import make_subplots
import plotly.graph_objects as go

COLOR_1 = "#1f77b4"  # blu
COLOR_2 = "#d62728"  # rosso

def plot_parameter(tel1, tel2, parameter, driver_1, driver_2, dash=False, title=None, y_title=None, y_range=None):
    tel1 = tel1.copy()
    tel2 = tel2.copy()

    if parameter == "Brake":
        tel1[parameter] = tel1[parameter].astype(int)
        tel2[parameter] = tel2[parameter].astype(int)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=tel1["Distance"],
        y=tel1[parameter],
        name=f"{driver_1}",
        line=dict(color=COLOR_1, dash="dot" if dash else None)
    ))
    fig.add_trace(go.Scatter(
        x=tel2["Distance"],
        y=tel2[parameter],
        name=f"{driver_2}",
        line=dict(color=COLOR_2, dash="dot" if dash else None)
    ))

    fig.update_layout(
        title=title or f"{parameter} comparison",
        yaxis_title=y_title or parameter,
        height=500
    )
    if y_range:
        fig.update_yaxes(range=y_range)

    return fig

def plot_telemetry_dashboard(tel1, tel2, driver_1, driver_2, gp, year, session_type):
    tel1 = tel1.copy()
    tel2 = tel2.copy()
    tel1["Brake"] = tel1["Brake"].astype(int)
    tel2["Brake"] = tel2["Brake"].astype(int)

    parametri = [
        ("Speed", "Speed (km/h)", False, None),
        ("Throttle", "Throttle (%)", False, None),
        ("Brake", "Brake (on/off)", False, [-0.1, 1.1]),
    ]

    fig=make_subplots(
        rows=len(parametri), cols=1,
        shared_xaxes=True,
        subplot_titles=("",) * len(parametri),
        vertical_spacing=0
    )

    for i, (param, label, dash, yrange) in enumerate(parametri):
        row = i + 1
        
        showlegend = (i == 0)
        for j, trace in enumerate(plot_parameter(tel1, tel2, param, driver_1, driver_2, dash=dash).data):
            trace.showlegend = showlegend
            fig.add_trace(trace, row=row, col=1)

        
        fig.update_yaxes(title_text=label, row=row, col=1)
        fig.update_xaxes(showgrid=True, nticks=20, row=row, col=1)

        if param == "Brake":
            fig.update_yaxes(tickvals=[0, 1], row=row, col=1)
        if yrange:
            fig.update_yaxes(range=yrange, row=row, col=1)

    fig.update_layout(
        height=300 * len(parametri),
        title=f"{driver_1} vs {driver_2} - {gp} {year} ({session_type})",
        legend_title="Parameters"
    )

    fig.update_xaxes(title_text="Distance (m)", row=3, col=1)

    return fig