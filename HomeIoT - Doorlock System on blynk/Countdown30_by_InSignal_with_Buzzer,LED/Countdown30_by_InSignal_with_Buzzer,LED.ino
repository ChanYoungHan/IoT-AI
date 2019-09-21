
//7세그먼트
// 사용법 참고 https://github.com/DeanIsMe/SevSeg
// timer.h 사용법 참조 http://www.dreamy.pe.kr/zbxe/CodeClip/3768817
#include <SevSeg.h>
#include "Timer.h"
 
 
Timer t;
SevSeg sevseg; //init Segment-object

int buzzerPin = A0; //pin for Sound
int number=31; //Counter value 1-30
static unsigned long timer = 0;
static unsigned long fotimer = 0;

int sigin_rf_save =0;
int sigin_key_save = 0; // form key 저장

int sigout = 0;

void setup()
{
//Serial.begin(9600);
  
  byte numDigits = 4; //number of digits
  byte digitPins[] = {2, 3, 4, 5}; //digit pins
  byte segmentPins[] = {6, 7, 8, 9, 10, 11, 12, 13}; //Pins Segment
  sevseg.begin(COMMON_CATHODE, numDigits, digitPins, segmentPins);
  sevseg.setBrightness(90);

  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(sigout, OUTPUT);
 
  t.every(1000, countdown);
  
}

void loop()
{
  sigin_rf_save = analogRead(A1);
  sevseg.refreshDisplay();
  
  if(sigin_rf_save>1000){
//Serial.println("Count Down is working!");
   t.update();
   CountDown_piezo(timer);
   
  }
  if(sigin_rf_save<1000){
    setColor(0,0,0);
  }
}

void countdown(){
//Serial.println("Count Down Start!");
    // Must run repeatedly
    timer += 1000;
 
    if(number > 0){
      number--;
    }

     sevseg.setNumber(number,2 );
   }
  


  
  //if(){ //Keypad에서 비밀번호 일치시 전송 받은 값일 경우 
  //  
  //  setColor(0,0,0);
  //}
 



void CountDown_piezo (long timer){

  
   if(millis() % 2000 == 0 && timer <= 10000)
   {
      setColor(0, 255, 0);
      tone(buzzerPin, 200, 500); 
 //     Serial.println("pcik!");
   }
   
   if(millis() % 1000 == 0 && timer > 10000)
   {
      setColor(255, 255, 0);
      tone(buzzerPin, 200, 300); 
//Serial.println("pcik!");
   }
   
   if(millis() % 500 == 0 && timer > 20000)
   {
      setColor(255,0,0);
      tone(buzzerPin, 200, 200); 
//      Serial.println("pcik!");
   }
   
   if(millis() % 250 == 0 && timer > 25000 && timer < 31000)
   {    
        setColor(255,0,0); 
        tone(buzzerPin, 200, 200);
//        Serial.println("pcik!");
   }
   
   if(timer > 30000)
   {   
//        Serial.println("pcik!");  
        digitalWrite(sigout, HIGH);
       tone(buzzerPin, 500, 3000); 
      
  
       StopCountDown();

       digitalWrite(sigout, LOW);
       loop();
   }
}

void StopCountDown(){
  
  for(int color=0; color < 10; color++){  
       setColor(255, 0, 0);
       delay(500);
       setColor(0, 0, 255);
       delay(500);
       }
       setColor(0,0,0);
       delay(5100000);
}

void setColor(int red, int green, int blue)
{
  analogWrite(A3, red);
  analogWrite(A4, green);
  analogWrite(A5, blue); 
}
