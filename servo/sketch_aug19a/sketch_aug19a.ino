#include <Servo.h>
Servo base;
Servo plane;

void setup(){
  Serial.begin(9600);
  plane.attach(8);
  plane.write(22);
  base.attach(4);
  base.write(75);
  Serial.println("testing...");
}

void loop(){
  if(Serial.available()){
    Serial.print("loops ");
    int i = Serial.parseInt();
    Serial.println(i);
    delay(10);
    switch (i){
      case 1:
        base.write(base.read()+1);
        break;
      case 2: 
        base.write(base.read()-1);
        break;
      case 3: 
        plane.write(plane.read()+1);
        break;
      case 4: 
        plane.write(plane.read()-1);
        break;
    }
    
    Serial.flush();
  }
}

