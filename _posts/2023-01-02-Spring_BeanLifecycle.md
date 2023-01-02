---
title: 스프링 빈 생명주기 콜백
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## **빈 생명주기 콜백**

---

스프링 빈은 간단하게 다음과 같은 라이프사이클을 가진다.

- **객체 생성 → 의존관계 주입**
- 스프링 빈은 객체를 생성하고, 의존관계 주입이 다 끝난 다음에야 필요한 데이터를 사용할 수 있는 준비가
완료된다. 따라서 초기화 작업은 의존관계 주입이 모두 완료되고 난 다음에 호출해야 한다.

> 그런데 개발자가 의존관계 주입이 모두 완료된 시점을 어떻게 알 수 있을까? **스프링은 의존관계 주입이 완료되면 스프링 빈에게 콜백 메서드를 통해서 초기화 시점을 알려주는 다양한 기능을 제공**한다. 또한 **스프링은 스프링 컨테이너가 종료되기 직전에 소멸 콜백**을 준다. 따라서 안전하게 종료 작업을 진행할 수 있다.
> 

### **스프링 빈의 이벤트 라이프사이클**

<aside>
👉 **스프링컨테이너생성 → 스프링빈생성 → 의존관계주입 → 초기화콜백 → 사용 → 소멸전콜백 → 스프링 종료**

</aside>

 **스프링은 크게 3가지 방법으로 빈 생명주기 콜백을 지원한다.**

1. 인터페이스(InitializingBean, DisposableBean)
2. 설정 정보에 초기화 메서드, 종료 메서드 지정
3. `@PostConstruct, @PreDestroy` 애노테이션 지원

### **인터페이스 InitializingBean, DisposableBean**

```java
public class NetworkClient implements InitializingBean, DisposableBean{

    private String url;

    public NetworkClient() {
        System.out.println("url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    //서비스 시작시 호출
    public void connect() {
        System.out.println("connect : " + url);
    }

    public void call(String message) {
        System.out.println("call : " + url + "message = " + message);
    }

    //서비스 종료시 호출
    public void disconnect() {
        System.out.println("close : " + url);
    }

		@Override
    public void afterPropertiesSet() throws Exception { //의존관계 주입이 끝나면 호출
        connect();
        call("초기화 연결 메세지");
    }
	
    @Override
    public void destroy() throws Exception {
        disconnect();
    }
```

- InitializingBean 은 `afterPropertiesSet()` 메서드로 초기화를 지원한다.
- DisposableBean 은 `destroy()`메서드로 소멸을 지원한다.
- 인터페이스를 사용하는 초기화, 종료 방법은 스프링 초창기에 나온 방법들이고, 지금은 다음의 더 나은 방법들이 있어서 거의 사용하지 않는다.

### **빈 등록 초기화, 소멸 메서드 지정**

설정 정보에 `@Bean(initMethod = "init", destroyMethod = "close")` 처럼 초기화, 소멸 메서드를

지정할 수 있다.

```java
public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    //서비스 시작시 호출
    public void connect() {
        System.out.println("connect : " + url);
    }

    public void call(String message) {
        System.out.println("call : " + url + "message = " + message);
    }

    //서비스 종료시 호출
    public void disconnect() {
        System.out.println("close : " + url);
    }

    public void init() { //의존관계 주입이 끝나면 호출
        connect();
        call("초기화 연결 메세지");
    }

    public void close() {
        disconnect();
    }
}
```

```java
@Configuration
static class LifeCycleConfig {
    @Bean(initMethod = "init", destroyMethod = "close")
    public NetworkClient networkClient() {
        NetworkClient networkClient = new NetworkClient();
        networkClient.setUrl("http://hello-spring.dev");
        return networkClient;
    }
}
```

- 메서드 이름을 자유롭게 줄 수 있다.
- 스프링 빈이 스프링 코드에 의존하지 않는다.
- 코드가 아니라 설정 정보를 사용하기 때문에 코드를 고칠 수 없는 외부 라이브러리에도 초기화, 종료
메서드를 적용할 수 있다.

### **애노테이션 @PostConstruct, @PreDestroy**

```java
public class NetworkClient {

    private String url;

    public NetworkClient() {
        System.out.println("url = " + url);
    }

    public void setUrl(String url) {
        this.url = url;
    }

    //서비스 시작시 호출
    public void connect() {
        System.out.println("connect : " + url);
    }

    public void call(String message) {
        System.out.println("call : " + url + "message = " + message);
    }

    //서비스 종료시 호출
    public void disconnect() {
        System.out.println("close : " + url);
    }

    @PostConstruct
    public void init() { //의존관계 주입이 끝나면 호출
        connect();
        call("초기화 연결 메세지");
    }
    @PreDestroy
    public void close() {
        disconnect();
    }
}
```

```java
@Configuration
static class LifeCycleConfig {
    @Bean
    public NetworkClient networkClient() {
        NetworkClient networkClient = new NetworkClient();
        networkClient.setUrl("http://hello-spring.dev");
        return networkClient;
    }
}
```

- 최신 스프링에서 가장 권장하는 방법이다.
- 애노테이션 하나만 붙이면 되므로 매우 편리하다.
- 패키지를 잘 보면 `javax.annotation.PostConstruct`이다. 스프링에 종속적인 기술이 아니라 JSR-250라는 자바 표준이다. 따라서 스프링이 아닌 다른 컨테이너에서도 동작한다.
- 컴포넌트 스캔과 잘 어울린다.
- 유일한 단점은 외부 라이브러리에는 적용하지 못한다는 것이다. 외부 라이브러리를 초기화, 종료 해야 하면
`@Bean`의 기능을 사용하자.

<aside>
👉 **`@PostConstruct, @PreDestroy` 애노테이션을 사용하자**

코드를 고칠 수 없는 외부 라이브러리를 초기화, 종료해야 하면 `@Bean` 의 initMethod , destroyMethod를 사용하자.

</aside>

<aside>
📖 references 스프링 핵심원리 -기본편 by 김영한

</aside>