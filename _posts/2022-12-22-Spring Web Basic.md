---
title: Spring-입문 2. 웹 개발 기초
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
Spring 웹 어플리케이션에서 브라우저에게 응답하는 방식은 다음과 같이 크게 3가지로 나눌 수 있다.

- Static Content
- MVC
- API

## Static Content

---

![Untitled.png](/assets/images/Spring_Web_Basic/Untitled.png)
1. 웹 브라우저가 /hello-static.html url을 요청하면 톰켓 내장서버는 스프링 컨테이너에 hello-static에 관련된 컨트롤러를 찾아달라고 한다.
2. 만약 관련된 컨트롤러가 없으면 톰켓 내장서버는 resources: statc/hello-static.html을 찾고 이를 웹 브라우저에게 응답해준다.

## **MVC**

---

![Untitled1.png](/assets/images/Spring_Web_Basic/Untitled 1.png)

1. 웹 브라우저는 /hello-mvc를 요청하고 내장 톰켓 서버는 스프링 컨터이너에 helloController에게 넘겨서 /hello-mvc에 매핑되어있는 메소드를 호출하고 “hello-template”을 return한다.
2. viewResolver는 return한 “hello-template”을 templates밑에 찾고 템플릿 엔진에게 넘긴다.
3. 템플릿 엔진은 변환한 html을 웹 브라우저에게 응답한다.

## API

---

![Untitled2.png](/assets/images/Spring_Web_Basic/Untitled 2.png)

1. 웹 브라우저가 /hello-api를 요청하면 내장 톰켓 서버는 스프링에 helloController에게 넘겨서 helloController는 /hello-api와 매핑되어있는 메소드가 있다면 해당 메소드를 호출한다.
2. 만약 해당 메소드에 `@ReponseBody` 라고 어노테이션이 있다면 viewResolver 대신 HttpMessageConverter에게 return 값을 반환한다.
3. HttpMessageConverter는 만약 반환값이 문자열이라면 StringConverter가 동작되고, 만약 반환값이 객체라면 JsonConverter가 동작된다.
4. hello라는 객체가 반환되었으므로 JsonConverter가 동작되어 웹 브라우제에게 Json형태로 데이터가 응답된다.
- 기본 문자처리: StringHttpMessageConverter
- 기본 객체처리: MappingJackson2HttpMessageConverter

<aside>
📖 references 스프링 입문 -코드로 배우는 스프링 부트, 웹 MVC, DB접근 기술 by 김영한

</aside>