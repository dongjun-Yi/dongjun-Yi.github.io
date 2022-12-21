---
title: Spring 프로젝트 환경설정
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, design pattern]
render_with_liquid: false
---
[https://start.spring.io](https://start.spring.io/) 에서 스프링 부트의 환경 설정이 가능하며, 버전선택, 패키지 이름, 라이브러리 추가 등 스프링 부트에 필요한 설정들을 추가할 수 있다.

dependencies 추가 내용 : Spring Web, Thymeleaf(html을 만들어주는 template 엔진)

### **환경설정**

---

- build.gradle
    - repositories{ mavenCentral()} : mavenCentral()이라는 곳에서 라이브러리 다운하라는 명령어
    - dependencies {implementaion ~} : 프로젝트 생성할 때 추가했던 라이브러리들

### **라이브러리**

---

dependencies : 라이브러리와의 의존관계

- spring-boot-starter-web
    - spring-boot-starter-tomcat: 톰캣 (웹서버)
    - spring-webmvc: 스프링 웹 MVC
- spring-boot-starter-thymeleaf: 타임리프 템플릿 엔진(View)
- spring-boot-starter(공통): 스프링 부트 + 스프링 코어 + 로깅
    - spring-boot
        - spring-core
    - spring-boot-starter-logging
        - logback, slf4j

### **Spring 동작 환경**

![Untitled.png](/assets/images/SpringProjectSetting/Untitled.png)

1. 웹 브라우저가 8080포트에 접속하면 톰켓서버를 거쳐 스프링 컨테이너에게 /hello에 관한 처리를 요청한다.
2. helloController는 model에 data : hello!를 삽입하고 “hello”를 return하면 viewResolver가 templates 밑에 hello.html를 찾는다.
3. ViewResolver는 hello.html을 찾아서 Thymeleaf가 템플릿을 처리하여 웹 브라우저에게 응답한다.
- 스프링 부트 템플릿엔진 기본 viewName 매핑
- **resources:templates/ +{ViewName}+ .html**

- **웹 템플릿 엔진은 view code(html)와 data logic code(db connection)를 분리해주는 기능을 한다.**