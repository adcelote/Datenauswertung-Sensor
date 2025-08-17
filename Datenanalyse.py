import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# NEU: Dateiname auf die neue CSV-Datei geändert
CSV_FILE = '/Path/to/sensordaten_beispiel.csv'

# Lade die realen Messdaten
df = pd.read_csv(CSV_FILE)

# --- ANPASSUNGEN FÜR REALE DATEN ---

# 1. NEU: Daten von 0-1023 in eine echte Spannung (0-5V) umrechnen
# Das macht die Y-Achse im Diagramm physikalisch interpretierbar.
adc_werte = df['Messwert']
spannung = adc_werte * (5.0 / 1023.0)
df['Spannung'] = spannung # Füge die berechnete Spannung als neue Spalte hinzu

# 2. NEU: Zeitachse selbst erstellen
# Wir wissen aus dem Arduino-Code, dass wir ca. alle 20ms (0.02s) einen Wert messen (50 Hz).
anzahl_messwerte = len(df)
abtastrate = 50  # 50 Hz
zeit = np.arange(0, anzahl_messwerte / abtastrate, 1 / abtastrate)
df['Zeit'] = zeit # Füge die Zeit als neue Spalte hinzu


# --- AB HIER IST DER CODE WIEDER SEHR ÄHNLICH ---

# Statistische Analyse der Spannungswerte
mittelwert = df['Spannung'].mean()
maximalwert = df['Spannung'].max()
minimalwert = df['Spannung'].min()

print("--- Statistische Analyse der realen Messdaten ---")
print(f"Mittelwert der Spannung: {mittelwert:.2f} V")
print(f"Maximalwert der Spannung: {maximalwert:.2f} V")
print(f"Minimalwert der Spannung: {minimalwert:.2f} V")
print("-------------------------------------------------")


# Digitalen Filter entwerfen und anwenden (Parameter bleiben gleich)
fs = abtastrate  # 50 Hz
fc = 2  # 2 Hz Grenzfrequenz
b, a = signal.butter(4, fc / (fs / 2), 'low')
gefilterte_spannung = signal.filtfilt(b, a, df['Spannung'])
df['Gefilterte Spannung'] = gefilterte_spannung


# --- FINALES DIAGRAMM ERSTELLEN ---

plt.figure(figsize=(12, 6))

# NEU: Spaltennamen im Plot-Befehl sind jetzt alle im DataFrame vorhanden
plt.plot(df['Zeit'], df['Spannung'], label='Originalsignal (real)', alpha=0.6)
plt.plot(df['Zeit'], df['Gefilterte Spannung'], label='Gefiltertes Signal', linewidth=2, color='red')

# Diagramm beschriften
plt.title('Analyse der realen Sensordaten vom Arduino')
plt.xlabel('Zeit [s]')
plt.ylabel('Spannung [V]')
plt.legend()
plt.grid(True)
plt.ylim(0, 5.5) # Setze das Limit der Y-Achse auf 0-5.5V für eine bessere Darstellung

# Diagramm speichern und anzeigen
plt.savefig('ergebnis_plot_real.png')
plt.show()
