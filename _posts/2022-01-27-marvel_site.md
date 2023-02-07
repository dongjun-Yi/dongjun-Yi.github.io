---
title: "[프로젝트] marvel_website"
author:
  name: dongjun-Yi
  link: https://github.com/dongjun-Yi/marvel_website.git
categories: [Project]
tags: [html, css, javascript, api]
render_with_liquid: false
---

api 호출을 이용한 반응형 웹페이지 마블 사이트

### 주요 사용 기술

* HTML
* CSS
* javascript

이번에 html, css ,js를 공부하면서 한번 웹사이트를 만들어보고 싶어 마침 api중에 marvel 정보를 주는 api가 있어서 
마블 정보를 주는 사이트를 한번 만들어 보았다.

내가만든 마블 웹사이트  ↓ ↓ ↓

[https://dj-marvel-site.netlify.app](https://dj-marvel-site.netlify.app/)



웹사이트는 모바일 버전에서도 볼 수 있게 반응형 웹사이트로 만들었고 공부한 내용들을 전체적으로 사용할 수 있었다.

#### 소스코드 ↓ ↓ ↓
[Github 바로가기!](https://github.com/dongjun-Yi/marvel_website.git)

#### 메인 화면 모습
![메인화면](https://user-images.githubusercontent.com/90665186/152365716-36089046-b502-4760-82f2-5e963ea1dacb.jpg)

카테고리는 캐릭터, 시리즈, 스토리, 만화 그리고 사건으로 구성되고
각 카테고리를 누르면 topic에 맞게 api를 호출한다.

#### 카테고리별 화면
![캐릭터](https://user-images.githubusercontent.com/90665186/152366006-99c58bce-e2b9-4976-822c-7c86a454dd90.jpg)
![event](https://user-images.githubusercontent.com/90665186/152366246-ee61643e-8d45-4972-8a6f-e50a105ffaad.jpg)

그런데 getdata()함수에서 api를 하려고 url을 이용해 fetch를 하는데 'fetch has been blocked by cors policy'라는 오류 발생..

인터넷에 처보니 CORS(Cross-Origin Resource Sharing) 이라고 하는데 이것은 추가 http헤더를 사용하며, 
한 출처에서 실행 중인 웹 어플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제 라고 한다.
결국 api를 사용하는 웹어플리케이션은 자신의 출처와 동일한 리소스만 불러올 수 있는것인데 이 해결방법을 구글링 해보니
프록시서버라는 중계서버로 우회해서 api를 호출하면 해결이 된다고 한다.
api호출 url앞에 'https://cors-anywhere.herokuapp.com/' 를 추가해서 fetch하면 잘 동작한다. 백엔드 쪽에서 CORS오류를 해결할 수 있지만
프론트 쪽에서는 딱히 방법이 없어 프록시서버로 우회해서 접속하였다.


#### 모바일 화면
![모바일 화면](https://user-images.githubusercontent.com/90665186/152367879-cdf1f4eb-c87c-4224-8841-cb18f1c960e7.jpg)
![모바일 화면 카테고리](https://user-images.githubusercontent.com/90665186/152367888-e7e13662-a1f6-41cf-bc67-2ac28b4e127d.jpg)

검색기능도 구현했고, 모바일 버전에서는 메뉴바도 생기게 구현
그리고 마지막 page navigation도 구현하여 웹페이지 완성

javascript를 공부할겸 처음 만든 웹페이지. javascript로 api 불러오는거를 통해 웹페이지를 조금더 동적으로 만들수 있었고 만드는 과정에서 REST api에 관하여 백엔드와 프론트간에 통신에 있어 주고 받는 데이터 형식에 대해 많은 공부를 하였다. 또한 bootstrap을 이용하면서 웹페이지를 꾸몄고 html과 css를 써가면서 사용자UI에 신경을 많이 썼지만 전체적인 css나 웹페이지에 보여지는 컴포넌트들이 좀 심심한느낌도 있어 화면구성에 어려움을 느꼈다. 또한 화면을 구성할때 사용자에게 이해도와 흥미를 높이기 위해 UI를 구성하는 연습과 생각이 필요하고 느꼈다.



