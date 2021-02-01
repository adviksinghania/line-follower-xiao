int led = 13;  // LED pin
int right1 = 9;  // Right motor pin 1
int right2 = 8;  // Right motor pin 2
int right_en = 7;  // EN pin on right
int left1 = 4;  // Left motor pin 1
int left2 = 5;  // Left motor pin 2
int left_en = 6;  // EN pin on left
int ir_left = A3;  // Left IR Sensor pin
int ir_right = A10;  // Right IR Sensor pin

// Function for initializing/stopping the robot
void initialize() {
  digitalWrite(left1, LOW);
  digitalWrite(left2, LOW);
  digitalWrite(left_en, HIGH);
  digitalWrite(right1, LOW);
  digitalWrite(right2, LOW);
  digitalWrite(right_en, HIGH);
}

// Turning right
void right() {
  digitalWrite(left1, LOW);
  digitalWrite(left2, HIGH);
  digitalWrite(right1, HIGH);
  digitalWrite(right2, LOW);
  Serial.println("Turning right");
}

// Turning left
void left() {
  digitalWrite(left1, HIGH);
  digitalWrite(left2, LOW);
  digitalWrite(right1, LOW);
  digitalWrite(right2, HIGH);
  Serial.println("Turning left");
}

// Moving forward
void forward() {
  digitalWrite(left1, LOW);
  digitalWrite(left2, HIGH);
  digitalWrite(right1, LOW);
  digitalWrite(right2, HIGH);
  Serial.println("Moving forward");
}

void setup() {  // Setup function
  Serial.begin(9600);
  pinMode(led, OUTPUT);

  pinMode(right1, OUTPUT);
  pinMode(right2, OUTPUT);
  pinMode(right_en, OUTPUT);

  pinMode(left1, OUTPUT);
  pinMode(left2, OUTPUT);
  pinMode(left_en, OUTPUT);

  pinMode(ir_left, INPUT);
  pinMode(ir_right, INPUT);

  initialize();
  delay(100);
  Serial.println("Ready");
}

void loop() { // Main loop function
  int readleft = analogRead(ir_left);  // values now in the range of 0 to 6
  int readright = analogRead(ir_right);
  //  Serial.print("Left: ");  // for debugging
  //  Serial.print(readleft);
  //  Serial.print('\t');
  //  Serial.print("Right: ");
  //  Serial.println(readright);
  if (readleft < 512 && readright < 512)
    forward();
  else if (readleft > 512 && readright < 512)
    left();
  else if (readleft < 512 && readright > 512)
    right();
  else
    initialize();
  delay(100);
}
