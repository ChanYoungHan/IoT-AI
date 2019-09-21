# IoT-AI
The codes from AI-IoT Education and project program linked to the IoT Companies.

2019.08 The codes from AI-IoT Education and preject program linked to the IoT Companies.

2019.08 산업진흥원에서 진행된 프로젝트기반 AI_IoT 취업연계 교육에서 만든 어플과 코드들입니다. 각 프로젝트는 사용한 언어 및 주제에 대해 제한되어있으며 final project에서는 교육프로그램에서 배운 모든 내용이 활용되었습니다. 



Crawling - made by phython jsoup lib, it contains simple data processing and the temperature about han-peninsula is visualized.
크롤링 - 파이선의 jsoup 라이브러리르 이용하여, 한반도 주변의 온도 데이터를 처리하고 시각화 하여, 그 변화를 본 프로젝트입니다. 그 중 한가지는 음원사이트로부터 가수들의 데이터를 모아 리스트를 매기는 기본적 예제도 포함합니다.

HomeIoT - Using Arduino and Blynk Web server service, Security IoT products are made.
아두이노를 사용하여 Blynk 웹서버 서비스를 사용하여 보안 IoT 시스템을 구축한 예제입니다.

둘중 하나는 두개의 초음파센서가 물체의 이동방향을 추적하여, 공간에 들어왔는지 나갔는지를 판단합니다. 오류를 제어하기 위해 추가적인 조건문이 사용되며, 사용환경에 따라 설정하도록 했습니다.
판단내용 및 기준은 와이파이 모듈, 블루투스 모듈을 통해 어플과 커뮤니케이션하여 설정 및 모니터링 할 수 있습니다.
지정 값 이상의 침입자가 발생하면 경고음과 함께 미리 설정된 사용자에게 푸쉬알람이 발생합니다. 이를 통해 위험 상황을 타인에게 알릴 수 있습니다

나머지 하나는 RFID, 초음파센서, keypad, 7segment 등 아두이노 기초 컴포넌트를 이용하여, 보안 시스템을 구축하였습니다. 여러개의 아두이노가 1-wire 방식으로 간단한 통신을 합니다. 최종적인 결과의 모니터링은 blynk 웹서버 서비스로 이루어지게 구성되었습니다. 


FinalProject - Using the Physics of Sensor, AI, Data Processing, Android Studio that is leraned at the program, IoT Golf application is made.
가속도 센서 mpu9250을 대신하여, 휴대폰의 가속도 센서를 이용하여 물리모델을 구축하고, 모바일 딥러닝이 동시에 탑재되었습니다. 스포츠 골프의 3D 스윙 데이터, 가속도와 힘 데이터를 얻음과 동시에 시퀀스 데이터의 조합을 AI가 판단하여 간단한 이진분류를 진행할 수 있습니다. 
