#include <NewPing.h>

#define TRIGGER_PIN 9
#define ECHO_PIN 10
#define MAX_DISTANCE 200
void setup() {
pinMode(TRIGGER_PIN, OUTPUT); // Sets the trigPin as an Output
pinMode(ECHO_PIN, INPUT); // Sets the echoPin as an Input
Serial.begin(9600); // Starts the serial communication
}
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
void loop() {
delay(100); //1 sec
int dist_inches = sonar.ping_in();
Serial.println(dist_inches);
}
