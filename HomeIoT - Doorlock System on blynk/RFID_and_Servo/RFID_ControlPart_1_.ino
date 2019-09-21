#include <MFRC522.h>
#include <MFRC522Extended.h>
#include <require_cpp11.h>

#include <Servo.h>
#include <SPI.h>
#include <MFRC522.h>
#define RST_PIN   9     // reset핀 설정 (태깅)
#define SS_PIN    10    // 데이터를 주고받는 역할의 핀( SS = Slave Selector ) (태깅)

int Piezo = 7; //피에조 스피커의 변수 선언
int fail_num = 0 ; //실패 횟수

int echoPin = 2; //초음파 센서의 핀번호 설정
int trigPin = 4; //초음파 센서의 핀번호 설정
int door = 15;

int outsig = 3; // 출력 신호 핀번호 설정

int insig_pass =0;


Servo servo;

MFRC522 mfrc(SS_PIN, RST_PIN);           // 이 코드에서 MFR522를 이용하기 위해 mfrc객체를 생성해 줍니다.

int motor = 6;                            // 모터를 6번핀에 연결합니다.

void setup() {
  Serial.begin(9600);                     // 시리얼 통신, 속도는 9600
  SPI.begin();                             // SPI 초기화(SPI : 하나의 마스터와 다수의 SLAVE(종속적인 역활)간의 통신 방식)
  mfrc.PCD_Init();
  
  pinMode(trigPin, OUTPUT); // trig를 출력모드로 설정
  pinMode(echoPin, INPUT); //echo를 입력모드로 설정
  pinMode(outsig, OUTPUT);
  servo.attach(motor);    //6번 핀 사용 서보모터
  servo.write(0);         //서보모터의 각을 0도로 초기화
  pinMode(Piezo, OUTPUT);
  pinMode(A5, INPUT);
}

void loop() {
  float duration, distance; //초음파센서의 값
  int a [5] ;
   //문과 사람의 거리

  
  //************초음파센서*****************
  digitalWrite(trigPin, HIGH);// 초음파를 보낸다. 다 보내면 echo가 HIGH 상태로 대기하게 된다.
  delay(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); // echoPin 이 HIGH를 유지한 시간을 저장 한다.
  distance = ((float)(340 * duration) / 10000) / 2;  // HIGH 였을 때 시간(초음파가 보냈다가 다시 들어온 시간)을 가지고 거리를 계산 한다.
  //Serial.print((int)distance);
  //Serial.println("cm");// 수정한 값을 출력


  
  if((int)distance < door){
    Serial.println("GoodBye!");        // 시리얼 모니터에 출력
    servo.write(90);
    delay(3000);
  }
 

  
  //*******RFID - RC522 태깅방식***********************
  if ( ! mfrc.PICC_IsNewCardPresent() || ! mfrc.PICC_ReadCardSerial() ) {    //  태그 접촉이 되지 않았을때 또는 아이디가 읽혀지지 않았을때
    delay(500);       
    return servo.write(0);                                  // return
  }
    
  if(mfrc.uid.uidByte[0] == 239 && mfrc.uid.uidByte[1] == 244 
       && mfrc.uid.uidByte[2] == 243 && mfrc.uid.uidByte[3] == 89) {    // 2번 태그 ID가 맞을경우

    Serial.println("어서오세요");        // 시리얼 모니터에 출력
    tone(Piezo,523,100);
    servo.write(90);  //90도 만큼 열린다.

    
    for(int i=0; i<40; i++){
    digitalWrite(outsig, HIGH); 
     insig_pass = analogRead(A5);
     Serial.println("Conutdown is working");
     Serial.println(insig_pass);
    if(insig_pass > 800){
      Serial.println("STOP!!");
      digitalWrite(outsig, LOW);
      break;
      }
      delay(1000);
    }
    fail_num = 0;
   digitalWrite(outsig, LOW);
  }
  else {                                   // 다른 태그 ID일 경우
    fail_num ++;
    Serial.print("누구냐 신고한다?");        // 시리얼 모니터에 출력 
    Serial.println(fail_num);
    delay(500);
    servo.write(0);

    if(fail_num == 3 ){
    Piezo_Siren(); // fail_num의 숫자가 3이 되었을때 피에조 사용자 함수
    }
  }
  

}
void Piezo_Siren(){
  int i = 0; //For문을 돌리는 변수
  for (int i =200; i<=800; i++){
    tone(Piezo,i);
    delay(5);
  }
  delay(4000);
  for(int i = 800; i>=200;i--){
    tone(Piezo,i);
    delay(10);
  }
fail_num = 0 ;
}
