---
title: marvel_website
author:
  name: dongjun-Yi
  link: https://github.com/dongjun-Yi/marvel_website.git
categories: [Project]
tags: [html, css, javascript, api]
render_with_liquid: false
---

api 호출을 이용한 마블 사이트

[Github 바로가기!](https://github.com/dongjun-Yi/marvel_website.git)

### 주요 사용 기술
* html
* css
* javascript
* bootstrap
* postman

이번에 html, css ,js를 공부하면서 한번 웹사이트를 만들어보고 싶어 마침 api중에 marvel 정보를 주는 api가 있어서 
마블 정보를 주는 사이트를 한번 만들어 보았다!

내가만든 마블 웹사이트  ↓ ↓ ↓

[https://dj-marvel-site.netlify.app](https://dj-marvel-site.netlify.app/)



웹사이트는 모바일 버전에서도 볼 수 있게 반응형 웹사이트로 만들었고 나름 만족스러운? 홈페이지가 나온것 같다

#### 메인 화면 모습
![메인화면](https://user-images.githubusercontent.com/90665186/152365716-36089046-b502-4760-82f2-5e963ea1dacb.jpg)

카테고리는 캐릭터, 시리즈, 스토리, 만화 그리고 사건으로 구성되고
각 카테고리를 누르면 topic에 맞게 api를 호출한다.

#### 카테고리별 화면
![캐릭터](https://user-images.githubusercontent.com/90665186/152366006-99c58bce-e2b9-4976-822c-7c86a454dd90.jpg)
![event](https://user-images.githubusercontent.com/90665186/152366246-ee61643e-8d45-4972-8a6f-e50a105ffaad.jpg)

그런데 api를 호하려고 코드 쓰는데 'fetch has been blocked by cors policy'라고 오류가 계속 떠서 멘붕..
인터넷에 처보니 CORS(Cross-Origin Resource Sharing) 이라고 하는데 이것은 추가 http헤더를 사용하며, 
한 출처에서 실행 중인 웹 어플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제 라고 한다
결국 api를 사용하는 웹어플리케이션은 자신의 출처와 동일한 리소스만 불러올 수 있는것인데 이 해결방법을 구글링 해보니
프록시서버라는 중계서버로 우회해서 api를 호출하면 해결이 된다고 한다.
근데 프록시 서버로 통해 api 호출해도 계속 똑같은 오류,,

며칠동안 고민하고 검색해도 안되다가 console.log 찍어보면서 어디서부터 안됐는지 체크하고 devtools로도 계속 확인했다.
결국 차근차근 생각해보니까 js에서는 단일 스레드라 이 부분을 비동기식으로 처리하기 위해 async으로 url을 불러오고
그다음 순서대로 진행이 되어야 되어서 그 다음에 getNews()에도 await을 붙여 url이 불러올때 까지 기달리고 url을 불러오는 작업이
끝나면 getNews()도 실행이 되어 오류 해결..!

#### 모바일 화면
![모바일 화면](https://user-images.githubusercontent.com/90665186/152367879-cdf1f4eb-c87c-4224-8841-cb18f1c960e7.jpg)
![모바일 화면 카테고리](https://user-images.githubusercontent.com/90665186/152367888-e7e13662-a1f6-41cf-bc67-2ac28b4e127d.jpg)

검색기능도 구현했고, 모바일 버전에서는 메뉴바도 생기게 구현
그리고 마지막 page navigation도 구현하여 웹페이지 완성!

완벽하진 않지만 그래도 끝까지 완성해서 뿌듯하고 api 불러오는거랑 웹페이지 꾸미고 bootstrap도 이용하면서 
웹페이지를 채우는 재미 있었다.! 



