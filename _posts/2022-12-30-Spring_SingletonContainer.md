---
title: "[Spring] 싱글톤 컨테이너"
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## **웹 애플리케이션과 싱글톤**

---

![Untitled.png](/assets/images/Spring_SingletonContainer/Untitled.png)

웹 어플리케이션 구조에서 고객은 보통 동시에 요청이 온다. 순수한  DI 컨테이너는 요청이 올때마다 객체를 새로 생성해서 반환해주게 된다.

**스프링없는 순수한 DI컨테이너 테스트**

```java
public class SingletonTest {
    @Test
    @DisplayName("스프링 없는 순수한 DI 컨테이너")
    void pureContainer() {
        AppConfig appconfig = new AppConfig();
        MemberService memberService1 = appconfig.memberService();
        MemberService memberService2 = appconfig.memberService();

        System.out.println("memberServic1 = " + memberService1);
        System.out.println("memberServic2 = " + memberService2);

        assertThat(memberService1).isNotSameAs(memberService2);
    }
}
```

- 스프링 없는 순수한 DI컨테이너는 요청이 올때마다 새로운 객체를 반환해서 만약 고객의 요청이 많을 경우 메모리낭비가 어마어마하게 많을 것이다.
- 이를 위해 해당 객체를 딱 1개만 생성하여 공유하도록 설계해야 한다.**(싱글톤 패턴)**

## 싱글톤 패턴

---

클래스의 인스턴스가 딱 1개만 생성되는 것을 보장하는 디자인 패턴

```java
public class SingletonService {
    private static final SingletonService instance = new SingletonService();

    public static SingletonService getInstance() {
        return instance;
    }

    private SingletonService() {}

    public void logic() {
        System.out.println("싱글톤 객체 로직 호출");
    }
}
```

- static 영엑에 객체 instance를 미리 하나 생성한다.
- 이 객체 인스턴스가 필요하면 오직 `getInstance()` 메서드를 통해서만 조회할 수 있다. 이 메서드를
호출하면 항상 같은 인스턴스를 반환한다.
- 딱 1개의 객체 인스턴스만 존재해야 하므로, 생성자를 private으로 막아서 혹시라도 외부에서 new 키워드로 객체 인스턴스가 생성되는 것을 막는다.

**싱글톤 패턴을 사용하는 테스트 코드**

```java
@Test
@DisplayName("싱글톤 패턴을 적용한 객체 사용")
void singletonServiceTest() {
    SingletonService instance1 = SingletonService.getInstance();
    SingletonService instance2 = SingletonService.getInstance();

    System.out.println("instance1 = " + instance1);
    System.out.println("instance2 = " + instance2);

    assertThat(instance1).isSameAs(instance2);
}
```

But, 싱글톤 패턴은 다음과 같은 문제점들이 있다.

- 싱글톤 패턴을 구현하는 코드 자체가 많이 들어간다.
- 의존관계상 클라이언트가 구체 클래스에 의존한다. DIP를 위반한다.
- 클라이언트가 구체 클래스에 의존해서 OCP 원칙을 위반할 가능성이 높다.
- 테스트하기 어렵다.
- 내부 속성을 변경하거나 초기화 하기 어렵다.
- private 생성자로 자식 클래스를 만들기 어렵다.
- 결론적으로 유연성이 떨어진다.
- 안티패턴으로 불리기도 한다.

## 싱글톤 컨테이너

---

- 스프링 컨테이너는 싱글턴 패턴을 적용하지 않아도, 객체 인스턴스를 싱글톤으로 관리한다.
- 스프링 컨테이너는 싱글톤 컨테이너 역할을 한다. 이렇게 싱글톤 객체를 생성하고 관리하는 기능을 싱글톤
레지스트리라 한다.
- 스프링 컨테이너의 이런 기능 덕분에 싱글턴 패턴의 모든 단점을 해결하면서 객체를 싱글톤으로 유지할 수
있다.
    - 싱글톤 패턴을 위한 지저분한 코드가 들어가지 않아도 된다.
    - DIP, OCP, 테스트, private 생성자로 부터 자유롭게 싱글톤을 사용할 수 있다.

**스프링 컨테이너를 사용하는 테스트 코드**

```java
@Test
@DisplayName("스프링 컨테이너와 싱글톤")
void springContainer() {
    ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    MemberService memberService1 = ac.getBean("memberService", MemberService.class);
    MemberService memberService2 = ac.getBean("memberService", MemberService.class);

    System.out.println("memberService1 = " + memberService1);
    System.out.println("memberService2 = " + memberService2);

    assertThat(memberService1).isSameAs(memberService2);
}
```

**스프링 컨테이너 적용 후** 

![Untitled1.png](/assets/images/Spring_SingletonContainer/1.png)

- 스프링 컨테이너 덕분에 고객의 요청이 올 때 마다 객체를 생성하는 것이 아니라, 이미 만들어진 객체를 공유해서 효율적으로 재사용할 수 있다.

## **싱글톤 방식의 주의점**

---

- 객체 인스턴스를 하나만 생성해서 공유하는 싱글톤 방식은 여러 클라이언트가 하나의 같은 객체 인스턴스를 공유하기 때문에 싱글톤 객체는 상태를 유지(stateful)하게 설계하면 안된다.
- 무상태(stateless)로 설계해야 한다!
    - 특정 클라이언트에 의존적인 필드가 있으면 안된다.
    - 특정 클라이언트가 값을 변경할 수 있는 필드가 있으면 안된다!
    - 가급적 읽기만 가능해야 한다.
    - 필드 대신에 자바에서 공유되지 않는, 지역변수, 파라미터, ThreadLocal 등을 사용해야 한다.
- 스프링 빈의 필드에 공유 값을 설정하면 정말 큰 장애가 발생할 수 있다!!!

**상태를 유지할 경우 발생하는 문제점 예시**

```java
public class StatefulService {

    private int price;

    public void order(String name, int price){
        System.out.println("name = " + name + " price = " + price);
        this.price = price;
    }

    public int getPrice() {
        return price;
    }
}
```

**문제점 테스트**

```java
public class SingletonServiceTest {
    ApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);
    @Test
    void statefulServiceSingleton() {
        StatefulService bean1 = ac.getBean(StatefulService.class);
        StatefulService bean2 = ac.getBean(StatefulService.class);

        bean1.order("userA", 10000);
        bean2.order("userB", 20000);
        int price = bean1.getPrice();
        System.out.println("price = " + price);

        assertThat(price).isEqualTo(20000);
    }

    static class TestConfig {
        @Bean
        public StatefulService statefulService() {
            return new StatefulService();
        }
    }
}
```

- StatefulService 의 price 필드는 공유되는 필드인데, 특정 클라이언트가 값을 변경한다.
- 사용자A의 주문금액은 10000원이 되어야 하는데, 20000원이라는 결과가 나왔다.
- 진짜 공유필드는 조심해야 한다! 스프링 빈은 항상 무상태(stateless)로 설계하자.
- `int price;`를 지역변수에 두면 해결할 수 있다.

## @Configuration과 바이트코드 조작의 마법

---

스프링 컨테이너는 스프링 빈이 싱글톤이 되도록 보장해주어야 한다. 그래서 스프링은 클래스의 바이트코드를 조작하는 라이브러리를 사용한다.

```java
@Test
void configurationDeep() {
	  ApplicationContext ac = new
	          AnnotationConfigApplicationContext(AppConfig.class);
	  //AppConfig도 스프링 빈으로 등록된다.
	  AppConfig bean = ac.getBean(AppConfig.class);
	  System.out.println("bean = " + bean.getClass());
	  //출력: bean = class hello.core.AppConfig$$EnhancerBySpringCGLIB$$bd479d70
}
```

bean객체를 println으로 출력하게 되면 xxxCGLIB가 붙으면서 상당히 복잡하게 출력되는것을 볼 수 있다. 이것은 내가 만든 클래스가 아니라 **스프링이 CGLIB라는 바이트코드 조작 라이브러리를 사용해서** AppConfig 클래스를 상속받은 임의의 다른 클래스를 만들고, **그 다른 클래스를 스프링 빈으로 등록한 것이다!**

![Untitled2.png](/assets/images/Spring_SingletonContainer/2.png)

- 이렇게 바이트 코드를 조작하여 스프링 컨테이너는 싱글톤을 보장해준다.

**AppConfig@CGLIB 예상 코드**

```java
@Bean
    public MemberRepository memberRepository() {
        if (memoryMemberRepository가 이미 스프링 컨테이너에 등록되어 있으면 ?){
            return 스프링 컨테이너에서 찾아서 반환;
        } else{ //스프링 컨테이너에 없으면
            기존 로직을 호출해서 MemoryMemberRepository를 생성하고 스프링 컨테이너에 등록 return 반환
        }
    }
```

`@Bean`이 붙은 메서드마다 이미 스프링 빈이 존재하면 존재하는 빈을 반환하고, 스프링 빈이 없으면 생성해서 스프링 빈으로 등록하고 반환하는 코드가 동적으로 만들어진다.

> `@Configuration` 을 붙이면 바이트코드를 조작하는 CGLIB 기술을 사용해서 싱글톤을 보장한다. 만약 @Bean만 사용할 경우 스프링 빈으로는 등록되지만, 싱글톤을 보장해주지 않는다.
>

<aside>
📖 references 스프링 핵심원리 -기본편 by 김영한

</aside>