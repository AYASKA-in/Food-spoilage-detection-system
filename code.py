#include <SoftwareSerial.h>

const int smokeSensorPin = A5; 
const int tempSensorPin = A4; 
const int humSensorPin = A3; 
const int colorOutPin = 2;
const int S2 = 3; 
const int S3 = 4; 
const int S1 = 5; 
const int S0 = 6;
const int greenLED = 12; 
const int redLED = 13;

const int smokeThreshold = 400; 
const int tempThreshold = 100; 
const int humThreshold = 150;

void setup() { pinMode(smokeSensorPin, INPUT); 
pinMode(tempSensorPin, INPUT); 
pinMode(humSensorPin, INPUT); 
pinMode(colorOutPin, INPUT); 
pinMode(S2, OUTPUT); 
pinMode(S3, OUTPUT); 
pinMode(S1, OUTPUT); 
pinMode(S0, OUTPUT); 
pinMode(greenLED, OUTPUT);
pinMode(redLED, OUTPUT);

Serial.begin(9600); 
digitalWrite(S0, HIGH); 
digitalWrite(S1, LOW);
}

void loop() {
int smokeValue = analogRead(smokeSensorPin); 
int tempValue = analogRead(tempSensorPin); 
int humValue = analogRead(humSensorPin); 
float temperature = (tempValue / 1024.0) * 50.0; 
float humidity = (humValue / 1024.0) * 100;

int red = getColorReading(S2, LOW, S3, LOW);
int green = getColorReading(S2, HIGH, S3, HIGH); int blue = getColorReading(S2, LOW, S3, HIGH);

// Print values to Serial Monitor 
Serial.print("Smoke Level: "); 
Serial.println(smokeValue); 
Serial.print("Temperature: "); 
Serial.println(temperature); 
Serial.print("Humidity: "); 
Serial.println(humidity); 
Serial.print("Red: "); 
Serial.println(red); 
Serial.print("Green: "); 
Serial.println(green); 
Serial.print("Blue: "); 
Serial.println(blue);
bool isSpoiled = (smokeValue > smokeThreshold) || (temperature > tempThreshold) || (humidity > humThreshold) ||(red > 100 && green > 160 && blue > 190);

if (isSpoiled) { digitalWrite(redLED, HIGH); 
digitalWrite(greenLED, LOW);
Serial.println("Food Status: Spoiled");
} else {
digitalWrite(redLED, LOW); 
digitalWrite(greenLED, HIGH); 
Serial.println("Food Status: Fresh");
}

delay(1000);
}

int getColorReading(int s2Pin, bool s2State, int s3Pin, bool s3State) { 
  digitalWrite(s2Pin, s2State);
digitalWrite(s3Pin, s3State);
return pulseIn(colorOutPin, LOW);
}
