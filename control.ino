// This is to be uploaded on the Arduino to control the system actuators
#include <Servo.h>

// Define pins for input devices
const int MOTION_SENSOR_PIN = 2;  // Motion sensor connected to digital pin 2

// Define pins for output devices
const int DC_MOTOR_1_PIN = 3;     // DC Motor 1 connected to digital pin 3
const int DC_MOTOR_2_PIN = 4;     // DC Motor 2 connected to digital pin 4
const int SERVO_MOTOR_PIN = 5;    // Servo Motor connected to digital pin 5

// Define pins for LEDs
const int LED_1_PIN = 6;          // LED 1 connected to digital pin 6
const int LED_2_PIN = 7;          // LED 2 connected to digital pin 7
const int LED_3_PIN = 8;          // LED 3 connected to digital pin 8
const int LED_4_PIN = 9;          // LED 4 connected to digital pin 9

// Include necessary libraries


// Create servo object
Servo myServo;



void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // Initialize input pins
  pinMode(MOTION_SENSOR_PIN, INPUT);

  // Initialize output pins
  pinMode(DC_MOTOR_1_PIN, OUTPUT);
  pinMode(DC_MOTOR_2_PIN, OUTPUT);
  pinMode(SERVO_MOTOR_PIN, OUTPUT);
  
  // Initialize LED pins
  pinMode(LED_1_PIN, OUTPUT);
  pinMode(LED_2_PIN, OUTPUT);
  pinMode(LED_3_PIN, OUTPUT);
  pinMode(LED_4_PIN, OUTPUT);

  // Attach the servo to its pin
  myServo.attach(SERVO_MOTOR_PIN);

  // Print setup complete message
  Serial.println("Setup complete. Pins initialized.");
  
}

void loop() {
  // Main code to run repeatedly
  // Example: Control actuators based on input or sensors

}

// Add additional functions as needed
