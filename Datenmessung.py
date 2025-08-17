#
#  Datenmessung.py
#
#
#  Created by Adrian Wald on 17.08.25.
#

import serial
import time
import csv

# Finde den richtigen Port im Arduino IDE (unter Werkzeuge -> Port)
# Beispiele: 'COM3' (Windows), '/dev/ttyUSB0' oder '/dev/tty.usbmodem...' (Mac/Linux)
ARDUINO_PORT = '/dev/cu.usbmodem11301' # ANPASSEN!
BAUD_RATE = 9600
CSV_FILE = 'sensor_data_real.csv'
SAMPLES_TO_CAPTURE = 500 # Wie viele Messwerte wir aufnehmen wollen

print(f"Verbinde mit Arduino an Port {ARDUINO_PORT}...")
ser = serial.Serial(ARDUINO_PORT, BAUD_RATE)
time.sleep(2) # Kurze Pause, damit die Verbindung stabil ist

print(f"Starte Aufzeichnung von {SAMPLES_TO_CAPTURE} Messwerten...")

with open(CSV_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Messwert']) # Header für die CSV-Datei

    for i in range(SAMPLES_TO_CAPTURE):
        try:
            line = ser.readline().decode('utf-8').strip()
            if line: # Sicherstellen, dass die Zeile nicht leer ist
                print(f"Messwert {i+1}/{SAMPLES_TO_CAPTURE}: {line}")
                writer.writerow([line])
        except KeyboardInterrupt:
            print("Aufzeichnung durch Benutzer abgebrochen.")
            break

ser.close()
print(f"Aufzeichnung beendet. Daten in {CSV_FILE} gespeichert.")
