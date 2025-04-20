# 🏎️ F1 Telemetry Dashboard

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20App-ff4b4b?logo=streamlit&logoColor=white)](https://f1-telemetry-dashboard.streamlit.app/)

Un'app interattiva per confrontare la telemetria di due piloti di Formula 1 sul giro più veloce, basata sui dati ufficiali forniti da [FastF1](https://theoehrly.github.io/Fast-F1/).

ℹ️ Questo progetto è in fase di sviluppo e nasce come esercizio personale per acquisire familiarità con analisi dati, Streamlit e visualizzazione interattiva in Python.

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
git clone https://github.com/Luigiiamatore/f1-telemetry-dashboard.git
cd f1-telemetry-dashboard
```

### 2. Installa le dipendenze

Si consiglia l'uso di un virtual environment.

```bash
pip install -r requirements.txt
```

Se stai usando `pip-tools`, puoi anche rigenerare `requirements.txt` da `requirements.in`:

```bash
pip-compile requirements.in
```

### 3. Avvia l'app

```bash
streamlit run ./src/app.py
```

## ☁️ Deploy online

L'app è disponibile anche online:
👉 [Provala su Streamlit Cloud](https://f1-telemetry-dashboard.streamlit.app/)

## 🤝 Contribuire

Hai idee, suggerimenti o vuoi aggiungere funzionalità? Sentiti libero di aprire una pull request o segnalare un issue!

## 🧠 Basato su

- [FastF1](https://theoehrly.github.io/Fast-F1/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python/)
