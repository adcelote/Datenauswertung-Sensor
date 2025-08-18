# Analyse von realen Sensordaten mit Python und Arduino

> Dieses Projekt demonstriert einen vollständigen Workflow zur Auswertung von Sensordaten. Der Prozess reicht von der Erfassung mit einem Arduino-Mikrocontroller über die Validierung mit einem Oszilloskop bis zur finalen Filterung (SciPy) und Visualisierung (Matplotlib) in Python.

## Ergebnis

<img width="1200" height="600" alt="Analyse der realen Sensordaten vom Arduino" src="https://github.com/user-attachments/assets/b5c5e7d6-16b2-42cc-8978-9ed3054f19af" />

## Über das Projekt

Ziel dieses Projektes ist der Aufbau einer realen Sensorschaltung, die Erfassung der Daten mit einem Arduino, die Validierung des elektrischen Signals mit einem Analog Discovery 3 und zuletzt die Analyse der erfassten Daten mit Python.

Das Projekt deckt folgende Schritte ab:
* **Hardware:** Aufbau einer Schaltung mit einem Potentiometer als steuerbare Spannungsquelle.
* **Firmware:** Programmierung des Arduinos (C++) zur Messung und seriellen Ausgabe der Sensordaten.
* **Validierung:** Überprüfung des analogen Signals mit einem externen Oszilloskop (Analog Discovery 3).
* **Software:** Erfassung und Speicherung der Daten mit einem Python-Skript (`pyserial`).
* **Analyse:** Filterung des Signals mit einem Butterworth-Tiefpassfilter (`scipy.signal`) und Visualisierung der Roh- und Filterdaten mit `matplotlib`.

## Verwendete Technologien
* **Hardware:** Arduino Uno, Analog Discovery 3
* **Sprachen:** Python, C++
* **Python-Bibliotheken:** Pandas, NumPy, Matplotlib, SciPy, PySerial

## Setup & Anwendung

Dieses Projekt erfordert einen Arduino und einen Computer mit Python 3.

### 1\. Vorbereitung & Installation

a. **Hardware:** Baue die Schaltung wie unten gezeigt auf und lade die Firmware (`Messprogramm`) mit der [Arduino IDE](https://www.arduino.cc/en/software) auf den Mikrocontroller.
Für die Schaltung wird verwendet:
- Potentiometer (Bspw. 50K Ohm)
- 3 x male-female Jumper

  <img width="348" height="509" alt="Schaltungsaufbau" src="https://github.com/user-attachments/assets/fbb568aa-6f3d-4a46-a3b2-f2d592049038" />


b. **Software:** Klone dieses Repository und richte die Python-Umgebung im Projektordner ein:

```bash
# Virtuelle Umgebung erstellen und aktivieren
python -m venv venv
source venv/bin/activate  # für macOS/Linux bzw. .\venv\Scripts\activate für Windows

# Benötigte Bibliotheken installieren
pip install pandas numpy matplotlib scipy pyserial
```
### 2\. Validierung der Messergebnisse
a. Stelle im Seriellen Monitor die Baudrate auf 9600 baud
b. Verbinde das Oszilloskop (z.B Analog Discovery) mit dem Ausgang des Potentiometers
c. Vergleiche die Veränderung der Messwerte des Arduinos (0-1023 = 0-5V) mit den Messwerten des Oszilloskops.
   <img width="1470" height="867" alt="Bildschirmfoto 2025-08-17 um 20 45 16" src="https://github.com/user-attachments/assets/cd3c930c-f147-4766-8408-c561886891cc" />

### 3\. Datenerfassung

a. Trage den korrekten COM-Port deines Arduinos in der Datei `Datenmessung.py` ein.
b. Starte die Messung. Drehe während der Aufzeichnung am Potentiometer, um das Signal zu verändern.

```bash
python Datenmessung.py
```

c. Das Skript erstellt eine Datei namens `sensordaten.csv`.

### 4\. Analyse & Visualisierung

Führe das Analyse-Skript aus. Es liest automatisch die `sensordaten.csv` und generiert den Ergebnis-Plot.

```bash
python Datenanalyse.py
```
 




