Ziel des Projektes ist der bau einer realen Sensorschaltung, die Erfassung der Daten mit einem Arduino, die Validierung des elektrische Signal mit dem Analog Discovery 3 und Analyse der erfassten Daten mit einem Python-Skript

Benötigt:
- Potentiometer (Bspw. 50K \Ohm)
- Arduino
- male-female Jumper


## 1. Sensoraufbau: 
- Einer der äußeren Pins des Potis mit Power GND des Arduinos verbinden
- Anderer äußerer Pin mit Power 5V verbinden
- Mittlerer mit A0 verbinden

## 2. Arduino Programm:
 Messprogramm.cpp
