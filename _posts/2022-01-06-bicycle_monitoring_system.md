---
title: bicycle_monitoring_system
author:
  name: dongjun-Yi
  link: https://github.com/dongjun-Yi/Bicycle-Monitoring-System
categories: [Project]
tags: [python, raspberrypi, javascript]
render_with_liquid: false
---

 라즈베리파이를 이용하여 사용자의 자전거가 도난당하지 않게끔 자전거를 실시간으로 모니터링 한다.
 
 [Github 바로가기!](https://github.com/dongjun-Yi/Bicycle-Monitoring-System)
 
### 주요 사용 기술
 * flask (python famework)
 * Mosquitto(MQTT)
 * OpenCV
 * javascript

### 작품개요


사용자의 자전거가 도난 당하지 않게 자전거를 모니터링 하는 장치이다. 자전거 앞에 초음파센서가 달린 라즈베리파이를 두어 
자전거가 있는 곳까지의 거리 값을 측정한다. 만약 초음파 센서의 거리 값이 계속 증가하여 기존 거리 값보다 높아졌다면 자전거가
없어졌다는 걸로 간주하여 그 순간 라즈베리파이에 연결된 카메라로 자전거 주변을 촬영해서 웹페이지에 전송한다. 그러면 사용자는 자전거가 
도난 당했다는 알림과 함께 웹페이지에서 자전거 주변의 촬영된 사진을 확인 할 수 있다. 또한, 훔쳐간 범인의 얼굴을 쉽게 확인할 수 있도록 
얼굴인식기능을 이용하여 카메라에 범인의 얼굴이 찍히면 쉽게 범인의 얼굴을 알 수 있게 사진을 찍는다. 그리고 거리가 멀어졌을 때 자전거가 
도난당한 것을 알리기 위해 led로 점등하고, 언제 도난 당했는지 사진이 찍힌 날짜와 시간을 웹페이지에 표시하고, 사용자는 언제 자전거가 
없어졌는지 알 수 있게 자전거를 실시간으로 모니터링하여 내 자전거를 안전하게 관리한다.



### 시스템 구조



![미니프로젝트 구조도](https://user-images.githubusercontent.com/90665186/147327608-b4c52f74-0e8d-449c-8449-294948fab39d.png)




### 사용한 부품

- 라즈베리파이 1대
- 카메라 1대
- Led 1개
- 초음파센서 1대

##### 사용한 회로도 번호 
- GPIO 핀
- LED = 6번
- Trig = 20번
- Echo= 16번

### 회로도
![회로도 사진](https://user-images.githubusercontent.com/90665186/149314325-486cf509-c073-4d3e-84b3-91baa6a432b5.jpg)



### 소프트웨어

총 7개로 설계 (파이썬 코드 4개)
* Circuit.py (초음파센서를 제어하는 파이썬코드)

* Camera.py (카메라를 제어하는 파이썬코드)

* Mqtt.py (mosquitto를 통해 웹브라우저와 통신하는 파이썬코드)

* App.py (웹 브라우저로부터 접속과 요청을 받아 처리하는 플라스크 앱)

* Mqtt.html (사용자에게 라즈베리파이에서 측정한 센서값들을 보여주기 위한 html 코드)

* Mqttio.js (측정된 값을 웹페이지에서 실시간으로 확인하기 위한 javascrpit)

* Face.js (카메라로 찍은 사진을 얼굴인식을 하기 위한 javascript)




#### 1. Circuit.py


```python
import time
import RPi.GPIO as GPIO

# 초음파 센서를 대한 전역 변수 선언 및 초기화
trig = 20
echo = 16
GPIO.setmode(GPIO.BCM)#BCM모드로 설정
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT) #초음파센서 20번을 출력선으로 지정
GPIO.setup(echo, GPIO.IN) #초음파센서 16번을 입력선으로 지정
GPIO.output(trig, False)
led = 6 # LED를 사용할 핀번호 GPIO6 의미
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정

def measureDistance():
        global trig, echo
        time.sleep(0.5)
        GPIO.output(trig, True) # 신호 1 발생
        time.sleep(0.00001) # 짧은 시간을 나타내기 위함
        GPIO.output(trig, False) # 신호 0 발생

        while(GPIO.input(echo) == 0):
                pulse_start = time.time() # 신호 1을 받았던 시간
        while(GPIO.input(echo) == 1):
                pulse_end = time.time() # 신호 0을 받았던 시간

        pulse_duration = pulse_end - pulse_start
        return 340*100/2*pulse_duration

if(__name__ == "__main__"):
        while(True):
                print("물체와의거리는 %f" %measureDistance())
def controlLED(led = 6, onOff =0 ): # led 번호의 핀에 onOff(0/1) 값 출력
GPIO.output(led, onOff)
```



초음파센서로 자전거와의 거리를 측정하는 measureDistance 함수와 LED 불빛이 켜지고 꺼질수 있는 함수를 포함하는 코드




#### 2. Camera.py



```python
import os; import io; import time
import picamera
import cv2; import numpy as np
fileName = ""
stream = io.BytesIO()
camera =picamera.PiCamera()
camera.start_preview()
camera.resolution = (320, 240)
time.sleep(1)

def takePicture() :
        global fileName, stream, camera

        stream.seek(0)  #파일포인터를 처음으로 옮김
        stream.truncate() #파일을 비우는 작업
        camera.capture(stream, format='jpeg', use_video_port=True) #사진을 찍음(화질은 선명하게 설정하고 확장자는 jpeg로 stream에 저장)
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8) #바이너리 파일인 stream을 읽어서 data변수에 저장
        image = cv2.imdecode(data, 1) #얼굴인식을 위해 Binary 형태인 data를 읽은 다음 컬러이미지로 decode하기
        haar = cv2.CascadeClassifier('./haarCascades/haar-cascade-files-master/haarcascade_frontalface_default.xml') #객체 감지를 위한 CascadeClassifier 클래스를 이용
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #이미지를 회색으로 처리
        faces = haar.detectMultiScale(image_gray,1.1,3) #입력 이미지에서 다양한 크기의 개체(얼굴)를 감지하고 감지된 얼굴(객체)은 사각형목록으로 반환
        for x, y, w, h in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) #이미지에 (x+y)와 (x+w, y+h)를 꼭짓점으로 하는사각형 그리기

        takeTime = time.time() #시간을 부동소수점으로 표현
        fileName = "./static/%d.jpg" %(takeTime*10)
        cv2.imwrite(fileName, image) #얼굴인식된 이미지 저장
        return fileName

if __name__ == '__main__' :
        while(True):
                name = takePicture()
                print("fname= %s" % name)
```



파이카메라로 카메라를 제어하고 OpenCV를 이용해 얼굴인식이 가능하도록 만든 python 




#### 3. Mqtt.py



```python
# publisher

import time
import paho.mqtt.client as mqtt
import circuit # 초음파 센서 입력 모듈 임포트
import mycamera


broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()

client.connect(broker_ip, 1883)
client.loop_start()

while(True):
        d= circuit.measureDistance()
        t=time.localtime()
        print("측정거리는 %.2fcm 입니다"%d)
        if(d>30):
                img=mycamera.takePicture() #자전거와 초음파센서까지의 거리가 30cm이상이면 사진을 찍음
                client.publish("image", img, qos=0) #broker에게 image라는 토픽으로 publish
                circuit.controlLED(onOff=1) #자전거와 초음파센서까지의 거리가 30cm이상이면 LED ON
        else:
                circuit.controlLED(onOff=0) #거리가 다시 30cm이하면 LED끄기

client.loop_stop()
client.disconnect()

```



지속적으로 자전거와의 거리를 측정하고 만약에 거리가 30cm가 넘으면 사진을 찍어 broker에게 image를 publish한다.
또한 거리가 30cm가 넘으면 되면 LED 불빛이 점등되고, 다시 30cm이하가 되면 LED 불빛을 끄게 만든다.




#### 4. app.py



```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
        return render_template("mqtt.html")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)
```



파이썬 프레임워크인 flask를 이용하여 웹브라우저의 요청에 응답하는 코드




#### 5. mqtt.html



```
<!doctype html>
<html>
<head>
        <meta charset="utf-8">
    <title>Mini_Project</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.2/mqttws31.min.js" type="text/javascript"></script>
    <script src="/static/mqttio.js" type="text/javascript"></script>
    <script src="/static/face.js" type="text/javascript"></script>
    <script>
           window.addEventListener("load", function () {
                // http://224..129:8080/에서 224...의 IP만 끊어내는 코드
                var url = new String(document.location);
                ip = (url.split("//"))[1]; // ip = "224...:8080/"
                ip = (ip.split(":"))[0]; // ip = "224..."
                document.getElementById("broker").value = ip
           });
      </script>
    <style>
        canvas {background-color:lightblue}
    </style>
</head>
<body>
        <div style ="text-align:center">
        <h1>자전거 도난 방지 시스템</h1>
        </div>
        <hr>
        <div style ="text-align:center">
                <form id="connection-form">
                        <b>관리자  IP:</b>
                        <input id="broker" type="text" name="broker" value=""><br>
                        <input type="button" onclick="startConnect()" value="관리시작">
                        <input type="button" onclick="startDisconnect()" value="관리종료">
                </form>
        </div>
         <hr>
        <div style="text-align:center">
         <form id="subscribe-form">
                <p id="sub"></p>
         </form>
         <canvas id="myCanvas" width="320" height="240"></canvas><br>
                <input type="button" onclick="unsubscribe('image')" value="확인">
        </div>
        <hr>
        <p><strong><font size="4">●이력관리●</font></strong></p>
         <div id="messages"></div>
</body>
</html>
```



사용자가 실시간으로 자전거를 모니터링 할 수 있게 html로 만든 웹페이지




#### 6. mqttio.js



```python
var port = 9001 // mosquitto의 디폴트 웹 포트
var client = null; // null이면 연결되지 않았음
var time=null; //날짜를 저장하기 위한 변수
var first=null; //처음 찍힌 날짜를 저장하기 위한 변수
var month=null; //처음 찍힌 날짜중 월을 저장하기 위한 변수
var tmonth=null; // 몇월달인지를 저장하기 위한 변수

function startConnect() { // 접속을 시도하는 함수
    clientID = "clientID-" + parseInt(Math.random() * 100); // 랜덤한 사용자 ID 생성

    // 사용자가 입력한 브로커의 IP 주소와 포트 번호 알아내기
    broker = document.getElementById("broker").value; // 브로커의 IP 주소

    // id가 message인 DIV 객체에 브로커의 IP와 포트 번호 출력
    // MQTT 메시지 전송 기능을 모두 가징 Paho client 객체 생성
    client = new Paho.MQTT.Client(broker, Number(port), clientID);

    // client 객체에 콜백 함수 등록
    client.onConnectionLost = onConnectionLost; // 접속이 끊어졌을 때 실행되는 함수 등록
    client.onMessageArrived = onMessageArrived; // 메시지가 도착하였을 때 실행되는 함수 등록

    // 브로커에 접속. 매개변수는 객체 {onSuccess : onConnect}로서, 객체의 프로퍼틴느 onSuccess이고 그 값이 onConnect.
    // 접속에 성공하면 onConnect 함수를 실행하라는 지시
    client.connect({
        onSuccess: onConnect,
    });
}

var isConnected = false;

// 브로커로의 접속이 성공할 때 호출되는 함수
function onConnect() {
    isConnected = true;

    document.getElementById("messages").innerHTML += '<span><strong>*자전거 모니터링을 시작합니다.</strong></span><br/>';
    topic = "image"

    // 토픽으로 subscribe 하고 있음을 id가 message인 DIV에 출력
    document.getElementById("messages").innerHTML += '<span><strong>*자전거가 없어지면 사진과 아래 이력들을 확인하세요.</strong></span><br/>';
    document.getElementById("sub").innerHTML = '<span><strong>자전거가 안전하게 보관중</strong></span><br/>';

    client.subscribe(topic, qos = 0); // 브로커에 subscribe

}

function unsubscribe(topic) {
    if(client == null || isConnected != true) return;

    // 토픽으로 subscribe 하고 있음을 id가 message인 DIV에 출력

    document.getElementById("sub").innerHTML += '<span><strong>'+first.getFullYear()+'/'+first.getMonth()+'/'+month+'/'+first.getHours()+'시'+first.getMinutes()+'분'+first.getSeconds()+'초에 없어졌습니다.'+'</strong></span><br/>';
    document.getElementById("sub").innerHTML += '<span><strong>찍은 사진들은 static폴더에 저장되었으니  확인해주십시오.'+ '</strong></span><br/>';

    client.unsubscribe(topic, null); // 브로커에 subscribe
}

// 접속이 끊어졌을 때 호출되는 함수
function onConnectionLost(responseObject) { // 매개변수인 responseObject는 응답 패킷의 정보를 담은 개체
    document.getElementById("messages").innerHTML += '<span> 접속을 끊고</span><br/>';
    if (responseObject.errorCode !== 0) {
        document.getElementById("messages").innerHTML += '<span>오류 : ' + + responseObject.errorMessage + '</span><br/>';
    }
}
// 메시지가 도착할 때 호출되는 함수
function onMessageArrived(msg) { // 매개변수 msg는 도착한 MQTT 메시지를 담고 있는 객체
    console.log("onMessageArrived: " + msg.payloadString);

    // 토픽 image가 도착하면 payload에 담긴 파일 이름의 이미지 그리기
    if(msg.destinationName == "image") {
            drawImage(msg.payloadString); // 메시지에 담긴 파일 이름으로 drawImage() 호출. drawImage()는 웹 페이지에 있음
    }
    if(time==null){ //처음 사진이 찍힌 날짜 저장하기 위한 조건문
        first=new Date();
        time=new Date();
        month=first.getMonth()+1;
        tmonth=time.getMonth()+1;
    }
    else{ //처음 찍힌것이 아니라면 관리이력에 표시하기 위한 시간저장
        time=new Date();
        tmonth=time.getMonth()+1;
    }
    document.getElementById("sub").innerHTML = '<span><strong> ' + '자전거가 없어짐!!' + '</strong></span><br/>';


    // 도착한 메시지 출력
    document.getElementById("messages").innerHTML += '<span>'+'자전거없어짐!!'  + '  | ' + '사진을 확인하세요!'+' | '+' 시각 : '+time.getFullYear()+'/'+tmonth+'/'+time.getDate()+'/'+time.getHours()+'시'+time.getMinutes()+'분'+time.getSeconds()+'초' +'</span><br/>';
}

// disconnection 버튼이 선택되었을 때 호출되는 함수
function startDisconnect() {
    client.disconnect(); // 브로커에 접속 해제
    document.getElementById("messages").innerHTML += '<span>모니터링을 종료합니다 </span><br/>';
}

```



mqtt broker와 연결하는 함수, broker에게 topic이라는 주제로 subscribe 하는 함수, 자전거가 도난당했을때의 주변 촬영사진을 받아 웹페이지에 나타내는 함수로 구성했다.




#### 7. face.js



```python
// 전역 변수 선언
var canvas;
var context;
var img;

// load 이벤트 리스너 등록. 웹페이지가 로딩된 후 실행
window.addEventListener("load", function() {
        canvas = document.getElementById("myCanvas");
        context = canvas.getContext("2d");

        img = new Image();
        img.onload = function () {
                context.drawImage(img, 0, 0); // (0,0) 위치에 img의 크기로 그리기
        }
});

// drawImage()는 "image' 토픽이 도착하였을 때 onMessageArrived()에 의해 호출된다.
function drawImage(imgUrl) { // imgUrl은 이미지의 url
        img.src = imgUrl; // img.onload에 등록된 코드에 의해 그려짐
}

var isImageSubscribed = false;
function recognize() {
        if(!isImageSubscribed) {
                subscribe("image"); // 토픽 image 등록
        }
}

```



사진을 받아 웹페이지에 얼굴이 찍힌 사진들은 얼굴에 사각형모양을 그려서 웹페이지에 나타냈다.

## 실행 과정


#### 초기화면
![초기화면](https://user-images.githubusercontent.com/90665186/148380068-cd21ea73-a154-465c-adf1-f8cf049dff57.png)


호스트 ip주로 접속한 웹페이지 모습이다.


#### 관리시작 버튼을 누른 화면 & 자전거와의 거리측정
![관리시작화면](https://user-images.githubusercontent.com/90665186/148381864-73d8e8a9-fd10-4c28-9a70-7dad9b249a43.png)


관리시작을 누르면 이력관리 밑에 안내설명이 나오고 mqtt.py를 실행한 모습이다.


#### 만약 자전거가 도난 당했을 경우 웹페이지
![자전거 도난 당했을시1](https://user-images.githubusercontent.com/90665186/148382030-f899b4e1-a3ae-4677-b41f-a36b314e1fb5.png)
![자전거 도난 당했을시2](https://user-images.githubusercontent.com/90665186/148382117-cd9fbc85-cd40-4c56-b28b-a80c5e58ffbd.png)
![자전거 도난 당했을시3](https://user-images.githubusercontent.com/90665186/148382175-9c48bf2a-a141-4059-b440-c06c6735e158.png)


자전거가 도난 당했을 경우 초음파센서의 거리측정 값이 증가되면서 30cm이상 될 경우 사진을 찍어 웹페이지에 지속적으로 나타나는 화면이다.


#### 이력관리 화면
![이력관리 화면](https://user-images.githubusercontent.com/90665186/148382262-7dee99ce-9003-4882-b284-1462cb2b24b4.png)



도난 당했을시 웹페이지에서 사진을 받으면서 이력관리에 언제 없어졌는지 시간도 함께 표시되어 기록한다.


#### 얼굴이 찍혔을 경우의 사진이 전송된 웹페이지
![얼굴인식기능](https://user-images.githubusercontent.com/90665186/148382343-5939edb3-d7c9-491b-a9fd-5955f87d12cc.png)


만약 범인의 얼굴이 찍혔을 경우 사진에 얼굴인식기능을 할 수 있게 구현하여 사용자가 범인의 얼굴을 더 명확하게 볼 수 있게끔 소스코드를 작성했다.


#### 확인 버튼을 누른 화면
![확인버튼을 누른 화면](https://user-images.githubusercontent.com/90665186/148382453-89aa7b6e-54a9-46d0-8fdb-c2011f630519.png)


사용자가 자전거가 도난당한 것을 인지하고 확인버튼을 누르면 언제 없어졌는지 그리고 
static폴더에 찍힌 사진들이 저장됐다는 메시지와 함께 자전거 주변의 사진전송을 멈출 수 있다.


#### static 폴더에 저장된 사진들
![static1](https://user-images.githubusercontent.com/90665186/148382539-ceffe159-914c-4ff0-8067-4bbab7676bb8.png)
![static2](https://user-images.githubusercontent.com/90665186/148382551-bb4f4baa-0149-438e-a0b8-4a90ea6f1a74.png)
![static3](https://user-images.githubusercontent.com/90665186/148382558-e3cd5823-6ba0-4f73-989c-687ae06de878.png)

증거로 남기기 위해 사진을 static폴더에 저장하여 보관할 수 있다.


### 느낀점


컴퓨터공학을 전공하고 나서 처음으로 만든 프로젝트이다. 비록 간단한 프로젝트지만 이 프로젝트를 하면서 
주제선정부터 코드작성, 발표준비까지 정말 많은 시간을 들이면서 준비 했었다. 특히 나는 만드는 과정 중에 어떻게 하면 이 작품을 사용하는 사용자가
더 유용하게 쓰일 수 있을지에 대해 고민하면서 제작을 했었다. 이 작품을 만들고 나름 자신감도
얻었고 다 만들었을 때의 뿌듯함도 느꼈다. 그치만 결국 프로그램을 완성해도 사용자에게 정보를 시각적으로 잘 전달할려면 웹페이지를 잘 꾸며서 보여줘야 된다고 생각했고, 
웹페이지를 제작하는데 어려움을 느꼈다. html&css&javascript를 공부해서 보완해야겠다.



