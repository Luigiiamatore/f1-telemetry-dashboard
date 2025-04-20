# 🏎️ F1 Telemetry Dashboard

Un'app interattiva per confrontare la telemetria di due piloti di Formula 1 sul giro più veloce, basata sui dati ufficiali forniti da [FastF1](https://theoehrly.github.io/Fast-F1/).

## 📸 Anteprima

![Screenshot Dashboard](images/screenshot-dashboard.png)

## ⚙️ Funzionalità

- ✅ Selezione anno, circuito e sessione (prove libere, qualifiche, gara)
- ✅ Scelta dinamica dei piloti disponibili
- ✅ Grafici interattivi sincronizzati:
  - Velocità
  - Throttle (acceleratore)
  - Brake (frenata)
- ✅ Griglia sull’asse X per migliorare la leggibilità
- ✅ Tema chiaro/scuro selezionabile
- ✅ Layout responsive e leggibile anche su schermi più piccoli

## 🚀 Come eseguirlo localmente

### 1. Clona il progetto

```bash
git clone https://github.com/tuo-username/f1-telemetry-dashboard.git
cd f1-telemetry-dashboard
```

### 2. Installa le dipendenze

Si consiglia l'uso di un virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Avvia l'app

```bash
streamlit run ./src/app.py
```

## ☁️ Deploy online

Presto disponibile su [Streamlit Cloud](https://streamlit.io/cloud) — sarà sufficiente un link pubblico per provarlo!

## 🧠 Basato su

- [FastF1](https://theoehrly.github.io/Fast-F1/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
