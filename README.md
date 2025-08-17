Ziel des Projektes ist der bau einer realen Sensorschaltung, die Erfassung der Daten mit einem Arduino, die Validierung des elektrische Signal mit dem Analog Discovery 3 und Analyse der erfassten Daten mit einem Python-Skript

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
 - Arduino IDE herunterladen und installieren (z.B mit brew)
 - Arduino mit IDE verbinden
 - Messprogramm auf Arduino hochladen
 - Serieller Monitor Baudrate auf 9600 baud stellen
 
 ## (Optional) 3. Signal Validierung mit Analog Discovery:
 - Waveforms herunterladen
 - Analog Discovery mit Computer verbinden
 - Messspitze an mittleren Anschluss des Potentiometers
 - GND der Messspitze an GND des Arduino
 
 ## 4. Arduino Daten erfassen:
 - In der Arduino IDE den Port des Arduino kopieren und in Datenmessung.py einfügen
