//
//  Messprogramm.cpp
//  
//
//  Created by Adrian Wald on 17.08.25.
//

// Arduino Code zur Messung am Pin A0 und serieller Ausgabe

void setup() {
  // Starte die serielle Kommunikation mit dem PC
  // 9600 Baud ist ein gängiger Standardwert
  Serial.begin(9600);
}

void loop() {
  // Lies den analogen Wert am Pin A0.
  // Der Wert liegt zwischen 0 (für 0V) und 1023 (für 5V).
  int sensorWert = analogRead(A0);

  // Sende den gelesenen Wert über die serielle Schnittstelle an den PC.
  // println fügt einen Zeilenumbruch hinzu, damit jede Messung in einer neuen Zeile steht.
  Serial.println(sensorWert);

  // Warte 20 Millisekunden bis zur nächsten Messung.
  // Das ergibt eine Abtastrate von ca. 1000ms / 20ms = 50 Hz.
  delay(20);
}
