#include <IRremote.h>

#define PWM_D1 5
#define IN1_D1 2
#define IN2_D1 3

#define PWM_D2 6
#define IN1_D2 8
#define IN2_D2 9


IRrecv rc(11);
decode_results results;


int speed = 100;

void setup(){
  Serial.begin(9600);
  rc.enableIRIn();
  
  pinMode(PWM_D1,OUTPUT);
  pinMode(PWM_D2,OUTPUT);
  
  pinMode(IN1_D1,OUTPUT);
  pinMode(IN2_D1,OUTPUT);
  
  pinMode(IN1_D2,OUTPUT);
  pinMode(IN2_D2,OUTPUT);
}

void loop(){
  if (rc.decode(&results)){
 
       
    	switch(results.value){
          case 0xFD00FF://power
          break;
          case 0xFD807F://vol+ button
          	Serial.println("forward");
            analogWrite(PWM_D1, speed);
            analogWrite(PWM_D2, speed);
            digitalWrite(IN1_D1, HIGH);
            digitalWrite(IN2_D1, LOW);
            digitalWrite(IN1_D2, HIGH);
            digitalWrite(IN2_D2, LOW);
          break;
          case 0xFD40BF://func/stop button
          break;
          case 0xFD20DF://|<< button
          	Serial.println("turnLeft");
            analogWrite(PWM_D1, 0);
            analogWrite(PWM_D2, speed);
            digitalWrite(IN1_D1, HIGH);
            digitalWrite(IN2_D1, LOW);
            digitalWrite(IN1_D2, HIGH);
            digitalWrite(IN2_D2, LOW);
          break;
          case 0xFDA05F://>|| button
          	  Serial.println("stop");
              digitalWrite(IN1_D1, LOW);
              digitalWrite(IN2_D1, LOW);
              digitalWrite(IN1_D2, LOW);
              digitalWrite(IN2_D2, LOW);
          break ;  
          case 0xFD609F://>>|
             Serial.println("turnRight");
             analogWrite(PWM_D1, speed);
             analogWrite(PWM_D2, 0);
             digitalWrite(IN1_D1, HIGH);
             digitalWrite(IN2_D1, LOW);
             digitalWrite(IN1_D2, HIGH);
             digitalWrite(IN2_D2, LOW);
          break ;               
          case 0xFD10EF://down arrow
          	Serial.println("speedDown");
            speed-=10;
            if(speed<0) speed =0;
            analogWrite(PWM_D1, speed);
            analogWrite(PWM_D2, speed);
          break ;  
          case 0xFD906F://vol-
          	Serial.println("backward");
            analogWrite(PWM_D1, speed);
            analogWrite(PWM_D2, speed);
            digitalWrite(IN1_D1, LOW);
            digitalWrite(IN2_D1, HIGH);
            digitalWrite(IN1_D2, LOW);
            digitalWrite(IN2_D2, HIGH);
          break ;  
          case 0xFD50AF://up arrow
          	Serial.println("speedUp");
            speed+=10;
  			if(speed>255) speed =255;
  			analogWrite(PWM_D1, speed);
  			analogWrite(PWM_D2, speed);
          break ;  
           
          
        }
       rc.resume(); 
  }
}