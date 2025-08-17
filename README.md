## Ziel des Projektes ist der bau einer realen Sensorschaltung, die Erfassung der Daten mit einem Arduino, die Validierung des elektrische Signal mit dem Analog Discovery 3 und zuletzt die Analyse der erfassten Daten mit einem Python-Skript.

Benötigt:
- Potentiometer (Bspw. 50K \Ohm)
- Arduino
- 3 x male-female Jumper
Optional:
- Analog Discovery 3
- Messspitze
- 1 x male-male Jumper


## 1. Sensoraufbau: 
- Einer der äußeren Pins des Potis mit Power GND des Arduinos verbinden
- Anderer äußerer Pin mit Power 5V verbinden
- Mittlerer mit A0 verbinden

## 2. Arduino Programm:
 - Messprogramm.cpp herunterladen
 - Arduino IDE herunterladen und installieren (z.B mit ```brew install arduino-ide```)
 - Arduino mit IDE verbinden
 - Messprogramm auf Arduino hochladen
 - Serieller Monitor Baudrate auf 9600 baud stellen
 
 ## (Optional) 3. Signal Validierung mit Analog Discovery:
 - Waveforms herunterladen
 - Analog Discovery mit Computer verbinden
 - Messspitze an mittleren Anschluss des Potentiometers
 - GND der Messspitze an GND des Arduino

   <img width="1470" height="867" alt="Bildschirmfoto 2025-08-17 um 20 45 16" src="https://github.com/user-attachments/assets/cd3c930c-f147-4766-8408-c561886891cc" />

 
 ## 4. Arduino Daten erfassen:
 - In der Arduino IDE den Port des Arduino kopieren und in Datenmessung.py einfügen
 - Terminal öffnen
   ```
   python -m venv venv
   source venv/bin/activate
   pip install pandas numpy matplotlib scipy
   python Datenmessung.py
   ```
   und währenddessen den Poti drehen.

 ## 5. CSV zu Diagramm:
 - ".csv" aus Schritt 4 als Pfad kopieren und in "Datenanalyse.py" einfügen.
 - Im Terminal
```
   python Datenanalyse.py
```
 - Plot öffnet sich - Vergleich: 
 <img width="1200" height="600" alt="Analyse der realen Sensordaten vom Arduino" src="https://github.com/user-attachments/assets/b5c5e7d6-16b2-42cc-8978-9ed3054f19af" />
