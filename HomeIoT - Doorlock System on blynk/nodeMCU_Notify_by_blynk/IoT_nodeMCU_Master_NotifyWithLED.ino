

//nodeMCU PinNum가 아두이노랑 다릅니다.
#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>


char auth[] = "BgBiHm10oDAsTKavCIDFvnz3MzZ8vGwO";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "Bizschool4_2.4G";
char pass[] = "12345678";

int alarmPin = 4;
int led = 13;
int sig_in = 4;
int sig_save = 0;

SimpleTimer timer;


void setup() {
  // put your setup code here, to run once:
pinMode(led, OUTPUT);
pinMode(sig_in, INPUT);
Serial.begin(9600);
Blynk.begin(auth, ssid, pass);
}

void loop() {
  // put your main code here, to run repeatedly:
Blynk.run();

// 아두이노 신호를 받아 sig_save에 저장
sig_save = digitalRead(sig_in);
Serial.print("IN signal :");
Serial.println(sig_save);
delay(300);

// 아두이노 신호가 '1'일 때, light on
if(sig_save==HIGH){
  digitalWrite(led,HIGH);
Serial.println("light ON");
Blynk.notify("The Door is open!! Please Check the room!");
delay(5000);
}

// 아두이노 신호가 '0'일 떄, light off
if(sig_save==LOW){
  digitalWrite(led,LOW);
Serial.println("light OFF");
delay(300);
}
}
