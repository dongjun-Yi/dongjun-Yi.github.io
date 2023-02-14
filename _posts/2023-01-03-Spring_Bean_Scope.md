---
title: "[Spring] 빈 스코프"
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## **빈 스코프란?**

---

빈이 존재할 수 있는 범위를 뜻한다.

**스프링은 다음과 같은 다양한 스코프를 지원한다.**

- **싱글톤**: 기본 스코프, 스프링 컨테이너의 시작과 종료까지 유지되는 가장 넓은 범위의 스코프이다.
- **프로토타입**: 스프링 컨테이너는 프로토타입 빈의 생성과 의존관계 주입까지만 관여하고 더는 관리하지 않는
매우 짧은 범위의 스코프이다.
- **웹 관련 스코프**
    - **request**: 웹 요청이 들어오고 나갈때 까지 유지되는 스코프이다.
    - **session**: 웹 세션이 생성되고 종료될 때 까지 유지되는 스코프이다.
    - **application**: 웹의 서블릿 컨텍스트와 같은 범위로 유지되는 스코프이다.
    

## **프로토타입 스코프**

---

싱글톤 스코프의 빈을 조회하면 스프링 컨테이너는 항상 같은 인스턴스의 스프링 빈을 반환한다. 

반면에 프로토타입 스코프를 스프링 컨테이너에 조회하면 스프링 컨테이너는 **항상 새로운 인스턴스**를 생성해서 반환한다.

**싱글톤 빈 요청**

![Untitled.png](/assets/images/Spring_Bean_Scope/Untitled.png)

1. 싱글톤 스코프의 빈을 스프링 컨테이너에 요청한다.

2. 스프링 컨테이너는 본인이 관리하는 스프링 빈을 반환한다.

3. 이후에 스프링 컨테이너에 같은 요청이 와도 같은 객체 인스턴스의 스프링 빈을 반환한다.

**프로토타입 빈 요청1**

![Untitled1.png](/assets/images/Spring_Bean_Scope/Untitled 1.png)

1. 프로토타입 스코프의 빈을 스프링 컨테이너에 요청한다.

2. 스프링 컨테이너는 이 시점에 프로토타입 빈을 생성하고, 필요한 의존관계를 주입한다.

프로토타입 빈 요청2

![Untitled2.png](/assets/images/Spring_Bean_Scope/Untitled 2.png)

3. 스프링 컨테이너는 생성한 프로토타입 빈을 클라이언트에 반환한다.

4. 이후에 스프링 컨테이너에 같은 요청이 오면 항상 새로운 프로토타입 빈을 생성해서 반환한다.

> **스프링 컨테이너는 프로토타입 빈을 생성하고, 의존관계 주입, 초기화까지만 처리한다.** 클라이언트에 빈을 반환하고, 이후 스프링 컨테이너는 생성된 프로토타입 빈을 관리하지 않는다. 프로토타입 빈을 관리할 책임은 프로토타입 빈을 받은 클라이언트에 있다. 그래서 `@PreDestroy` 같은 종료 메서드가 호출되지 않는다.
> 

```java
public class PrototypeTest {
    @Test
    public void prototypeBeanFind() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(PrototypeBean.class);
        System.out.println("PrototypeTest.prototypeBeanFind1");
        PrototypeBean bean1 = ac.getBean(PrototypeBean.class);
        System.out.println("PrototypeTest.prototypeBeanFind2");
        PrototypeBean bean2 = ac.getBean(PrototypeBean.class);

        System.out.println("bean1 = " + bean1);
        System.out.println("bean2 = " + bean2);

        Assertions.assertThat(bean1).isNotSameAs(bean2);
        ac.close();
    }

    @Scope("prototype")
    static class PrototypeBean {
        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init");
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }
    }
}
```

- 스프링 컨테이너에 요청할 때 마다 새로 생성된다.
- 스프링 컨테이너는 프로토타입 빈의 생성과 의존관계 주입 그리고 초기화까지만 관여한다.
- 종료 메서드가 호출되지 않는다. 그래서 프로토타입 빈은 프로토타입 빈을 조회한 클라이언트가 관리해야 한다. 종료 메서드에 대한 호출도
- 클라이언트가 직접 해야한다.

## **프로토타입 스코프 - 싱글톤 빈과 함께 사용시 문제점**

---

clientBean이라는 싱글톤 빈이 의존관계 주입을 통해서 프로토타입 빈을 주입받아서 사용하는 예를 보자.

**싱글톤에서 프로토타입 빈 사용1**

![Untitled3.png](/assets/images/Spring_Bean_Scope/Untitled 3.png)

- clientBean 은 싱글톤이므로, 보통 스프링 컨테이너 생성 시점에 함께 생성되고, 의존관계 주입도
발생한다.
- clientBean 은 의존관계 자동 주입을 사용한다. 주입 시점에 스프링 컨테이너에 프로토타입 빈을
요청한다.
- 스프링 컨테이너는 프로토타입 빈을 생성해서 clientBean 에 반환한다. 프로토타입 빈의 count 필드
값은 0이다.
- 이제 clientBean 은 프로토타입 빈을 내부 필드에 보관한다. (정확히는 참조값을 보관한다.)

**싱글톤에서 프로토타입 빈 사용2**

![Untitled4.png](/assets/images/Spring_Bean_Scope/Untitled 4.png)

- 클라이언트 A는 clientBean 을 스프링 컨테이너에 요청해서 받는다.싱글톤이므로 항상 같은
clientBean 이 반환된다.
- 클라이언트 A는 clientBean.logic() 을 호출한다.
- clientBean 은 prototypeBean의 addCount() 를 호출해서 프로토타입 빈의 count를 증가한다.
count값이 1이 된다.

**싱글토에서 프로토타입 빈 사용3**

![Untitled5.png](/assets/images/Spring_Bean_Scope/Untitled 5.png)

- 클라이언트 B는 clientBean 을 스프링 컨테이너에 요청해서 받는다.싱글톤이므로 항상 같은 clientBean 이 반환된다.
- **여기서 중요한 점이 있는데, clientBean이 내부에 가지고 있는 프로토타입 빈은 이미 과거에 주입이 끝난
빈이다. 주입 시점에 스프링 컨테이너에 요청해서 프로토타입 빈이 새로 생성이 된 것이지, 사용 할 때마다
새로 생성되는 것이 아니다!**
- 클라이언트 B는 clientBean.logic() 을 호출한다.
- clientBean 은 prototypeBean의 addCount() 를 호출해서 프로토타입 빈의 count를 증가한다.
원래 count 값이 1이었으므로 2가 된다.

Test

```java
public class SingletonWithPrototypeTest1 {

    @Test
    void prototypeFind() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(PrototypeBean.class);
        PrototypeBean bean1 = ac.getBean(PrototypeBean.class);
        bean1.addCount();
        Assertions.assertThat(bean1.count).isEqualTo(1);

        PrototypeBean bean2 = ac.getBean(PrototypeBean.class);
        bean2.addCount();
        Assertions.assertThat(bean2.count).isEqualTo(1);
    }

    @Test
    void singletonClientUsePrototype() {
        AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(ClientBean.class, PrototypeBean.class);
        ClientBean bean1 = ac.getBean(ClientBean.class);
        int logic1 = bean1.logic();
        Assertions.assertThat(logic1).isEqualTo(1);

        ClientBean bean2 = ac.getBean(ClientBean.class);
        int logic2 = bean2.logic();
        Assertions.assertThat(logic2).isEqualTo(1);

    }

    @Scope("singleton")
    static class ClientBean {
        private final PrototypeBean prototypeBean; //생성 시점에 주입 beacause 생성주입이기 때문에

        @Autowired
        ClientBean(PrototypeBean prototypeBean) {
            this.prototypeBean = prototypeBean;
        }

        public int logic() {
            //PrototypeBean prototypeBean = prototypeBeanProvider.getObject();
            PrototypeBean prototypeBean = prototypeBeanProvider.get();
            prototypeBean.addCount();
            int count = prototypeBean.getCount();
            return count;
        }
    }

    @Scope("prototype")
    static class PrototypeBean {
        private int count = 0;

        public void addCount() {
            count++;
        }

        public int getCount() {
            return count;
        }

        @PostConstruct
        public void init() {
            System.out.println("PrototypeBean.init" + this);
        }

        @PreDestroy
        public void destroy() {
            System.out.println("PrototypeBean.destroy");
        }
    }
}
```

**스프링은 일반적으로 싱글톤 빈을 사용하므로, 싱글톤 빈이 프로토타입 빈을 사용하게 된다. 그런데 싱글톤 빈은 생성 시점에만 의존관계 주입을 받기 때문에, 프로토타입 빈이 새로 생성되기는 하지만, 싱글톤 빈과 함께 계속 유지되는 것이 문제다.**

## **프로토타입 스코프 - 싱글톤 빈과 함께 사용시 Provider로 문제 해결**

---

**ObjectFactory, ObjectProvider**

지정한 빈을 컨테이너에서 대신 찾아주는 DL 서비스를 제공하는 것이 바로 `ObjectProvider` 이다. 참고로 과거에는 `ObjectFactory`가 있었는데, 여기에 편의 기능을 추가해서 `ObjectProvider`가 만들어졌다.

```java
@Autowired
private ObjectProvider<PrototypeBean> prototypeBeanProvider;
public int logic() {
    PrototypeBean prototypeBean = prototypeBeanProvider.getObject();
    prototypeBean.addCount();
    int count = prototypeBean.getCount();
    return count;
}
```

- 실행해보면 prototypeBeanProvider.getObject() 을 통해서 항상 새로운 프로토타입 빈이 생성되는
것을 확인할 수 있다.
- ObjectProvider 의 getObject() 를 호출하면 내부에서는 스프링 컨테이너를 통해 해당 빈을 찾아서
반환한다. (**DL**)
- 스프링이 제공하는 기능을 사용하지만, 기능이 단순하므로 단위테스트를 만들거나 mock 코드를 만들기는
훨씬 쉬워진다.
- ObjectProvider 는 지금 딱 필요한 DL 정도의 기능만 제공한다.

<aside>
👉 `ObjectProvider , JSR330 Provider` 등은 프로토타입 뿐만 아니라 DL이 필요한 경우는 언제든지 사용할 수 있다.

</aside>

## **웹 스코프**

---

웹 스코프는 웹 환경에서만 동작하는 스코프이다. 웹 스코프는 프로토타입과 다르게 **스프링이 해당 스코프의 종료시점까지 관리한다. 따라서 종료 메서드가 호출된다.**

### 웹스코프 종류

- **request :** HTTP 요청 하나가 들어오고 나갈 때 까지 유지되는 스코프, 각각의 HTTP 요청마다 별도의 빈
인스턴스가 생성되고, 관리된다.
- **session :** HTTP Session과 동일한 생명주기를 가지는 스코프
- **application :** HTTP Session과 동일한 생명주기를 가지는 스코프
- **websocket :** 웹 소켓과 동일한 생명주기를 가지는 스코프

**HTTP request 요청 당 각각 할당되는 request 스코프**

![Untitled6.png](/assets/images/Spring_Bean_Scope/Untitled 6.png)

## **request 스코프 예제**

---

로그가 남도록 request 스코프를 활용해서 추가 기능을 개발하는 예를 들어 보자.

**로그를 출력하기 위한 MyLogger 클래스**

```java
@Component
@Scope(value = "request")
public class MyLogger {
    private String uuid;
    private String requestURL;

    public void setRequestURL(String requestURL) {
        this.requestURL = requestURL;
    }

    public void log(String message) {
        System.out.println("[" + uuid + "]" + "[" + requestURL + "] " + message);
    }

    @PostConstruct
    public void init() {
        uuid = UUID.randomUUID().toString();
        System.out.println("[" + uuid + "]" + "request scope bean create : " + this);
    }

    @PreDestroy
    public void close() {
        System.out.println("[" + uuid + "]" + "request scope bean close : " + this);
    }
}
```

- `@Scope(value = "request")`를 사용해서 request 스코프로 지정했다. 이제 이 빈은 HTTP 요청 당
    
    하나씩 생성되고, HTTP 요청이 끝나는 시점에 소멸된다.
    
- 이 빈이 생성되는 시점에 자동으로 `@PostConstruct` 초기화 메서드를 사용해서 uuid를 생성해서
저장해둔다. 이 빈은 HTTP 요청 당 하나씩 생성되므로, uuid를 저장해두면 다른 HTTP 요청과 구분할 수
있다.
- 이 빈이 소멸되는 시점에 `@PreDestroy` 를 사용해서 종료 메시지를 남긴다.

**LogDemoController**

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {
    private final LogDemoService logDemoService;
    private final MyLogger myLogger;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        Thread.sleep(100);
        logDemoService.logic("testId");
        return "OK";
    }
}
```

- Logger가 잘 작동하는지 확인하는 테스트용 컨트롤러다.
- 여기서 HttpServletRequest를 통해서 요청 URL을 받았다.
    - requestURL 값 http://localhost:8080/log-demo
- 이렇게 받은 requestURL 값을 myLogger에 저장해둔다. myLogger는 HTTP 요청 당 각각 구분되므로
다른 HTTP 요청 때문에 값이 섞이는 걱정은 하지 않아도 된다.

**LogDemoService**

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {
    private final MyLogger myLogger;

    public void logic(String id) {
        myLogger.log("service id=" + id);
    }
}
```

위와 같은 코드로 실행시키면 다음과 같은 오류가 발생한다.

Error creating bean with name 'myLogger': Scope 'request' is not active for the current thread; consider defining a scoped proxy for this bean if you intend to refer to it from a singleton;

> 스프링 애플리케이션을 실행하는 시점에 싱글톤 빈은 생성해서 주입이 가능하지만, request 스코프 빈은 아직 생성되지 않는다. 이 빈은 실제 고객의 요청이 와야 생성할 수 있다!
> 

## **스코프와 Provider**

---

첫번째 해결방안은 앞서 배운 Provider를 사용하는 것이다.

**LogDemoController**

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {
    private final LogDemoService logDemoService;
    private final ObjectProvider<MyLogger> myLoggerProvider;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request){
        String requestURL = request.getRequestURL().toString();
        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        Thread.sleep(100);
        logDemoService.logic("testId");
        return "OK";
    }
}
```

**LogDemoService**

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {
    private final ObjectProvider<MyLogger> myLoggerProvider;
  
    public void logic(String id) {
        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.log("service id=" + id);
    }
}
```

- `ObjectProvider`을 이용해서 `ObjectProvider.getObject()`를 호출하는 시점까지 request scope **빈의 생성을 지연**할 수 있다.
- `ObjectProvider.getObject()`를 호출하시는 시점에는 HTTP 요청이 진행중이므로 request scope 빈의 생성이 정상 처리된다.
- `ObjectProvider.getObject()`를 LogDemoController , LogDemoService 에서 각각 한번씩 따로 호출해도 같은 HTTP 요청이면 같은 스프링 빈이 반환된다

## 스코프와 프록시

---

MyLogger 클래스에 `proxyMode = ScopedProxyMode.TARGET_CLASS` 를 추가해주자. 

```java
@Component
  @Scope(value = "request", proxyMode = ScopedProxyMode.TARGET_CLASS)
  public class MyLogger {
  }
```

이렇게 하면 MyLogger의 가짜 프록시 클래스를 만들어두고 HTTP request와 상관 없이 가짜 프록시 클래스를 다른 빈에 미리 주입해 둘 수 있다.

이후 나머지 코드들을 Provider 사용 전으로 돌려놓으면 된다.

**LogDemoController**

```java
@Controller
@RequiredArgsConstructor
public class LogDemoController {
    private final LogDemoService logDemoService;
    private final MyLogger myLogger;

    @RequestMapping("log-demo")
    @ResponseBody
    public String logDemo(HttpServletRequest request) {
        String requestURL = request.getRequestURL().toString();
        myLogger.setRequestURL(requestURL);

        myLogger.log("controller test");
        Thread.sleep(100);
        logDemoService.logic("testId");
        return "OK";
    }
}
```

**LogDemoService**

```java
@Service
@RequiredArgsConstructor
public class LogDemoService {
    private final ObjectProvider<MyLogger> myLoggerProvider;
  
    public void logic(String id) {
        MyLogger myLogger = myLoggerProvider.getObject();
        myLogger.log("service id=" + id);
    }
}
```

실행되면 잘 동작한다.

## 웹 스코프와 프록시 동작 원리

---

`@Scope 의 proxyMode = ScopedProxyMode.TARGET_CLASS)` 를 설정하면 스프링 컨테이너는 **CGLI**라는 바이트코드를 조작하는 라이브러리를 사용해서, MyLogger를 상속받은 가짜 프록시 객체를
생성한다

- 결과를 확인해보면 우리가 등록한 순수한 MyLogger 클래스가 아니라 MyLogger$$EnhancerBySpringCGLIB 이라는 클래스로 만들어진 객체가 대신 등록된 것을 확인할 수 있다.

**프록시 동작 원리**

![Untitled7.png](/assets/images/Spring_Bean_Scope/Untitled 7.png)
**가짜 프록시 객체는 요청이 오면 그때 내부에서 진짜 빈을 요청하는 위임 로직이 들어있다.**

- 가짜 프록시 객체는 내부에 진짜 myLogger를 찾는 방법을 알고 있다.
- 클라이언트가 myLogger.logic() 을 호출하면 사실은 가짜 프록시 객체의 메서드를 호출한 것이다.
- 가짜 프록시 객체는 request 스코프의 진짜 myLogger.logic() 를 호출한다.
- 가짜 프록시 객체는 원본 클래스를 상속 받아서 만들어졌기 때문에 이 객체를 사용하는 클라이언트
입장에서는 사실 원본인지 아닌지도 모르게, 동일하게 사용할 수 있다(다형성)

<aside>
👉 Provider를 사용하든, 프록시를 사용하든 핵심 아이디어는 **진짜 객체 조회를 꼭 필요한 시점까지 지연처리 한다는 점이다.**

</aside>

<aside>
📖 references 스프링 핵심원리 -기본편 by 김영한

</aside>