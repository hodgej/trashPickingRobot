#include <Servo.h>


Servo myservo;

int incomingByte;

void setup() 
{ 
  Serial.begin(9600);
  myservo.attach(6);
  myservo.write(30);  // set servo to mid-point
  pinMode(6, OUTPUT);
} 

void loop() {

  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
  //myservo.write(gotVal);  // set servo to mid-point

  if(incomingByte=="h"){
    myservo.write(120);  // set servo to mid-point
  }
}
