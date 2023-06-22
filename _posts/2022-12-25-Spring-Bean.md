---
title: "[Spring] 빈과 의존관계"
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## Bean이란?

---

*the objects that form the backbone of your application and that are managed by the Spring IoC container are called beans. A bean is an object that is instantiated, assembled, and otherwise managed by a Spring IoC container.*

Spring 공식문서에 bean의 정의를 보면 spring 컨테이너에 의해 제어받는 어플리케이션의 구조인 객체를 뜻한다고 나와있다. 근데 여기서 IoC란 뭘까?

## IoC(Inversion of Control)란?

---

→Inversion of Control(IoC) is **a process in which an object defines its dependencies without creating them.**

IoC란 객체가 의존성을 생성하지 않고 정의하는 프로세스를 뜻한다. 이와 같은 기법을 DI(Dependency injection)이라고 하며 객체의 생성이나 값을 대입하는 경우 외부에서 주입하는 경우를 말한다.

## 컴포넌트 스캔과 자동 의존관계 설정

회원 컨트롤러에 회원 서비스와 회원 리포지토리를 사용할 수 있게 의존관계를 설정하는 코드를 보면

```java
@Controller
public class MemberController {
    private final MemberService memberService;

    @AutoWired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
```

생성자에 `@AutoWired`가 있으면 스프링이 연관관계가 맺어진 객체를 찾아서 스프링 컨테이너 안에 넣어준다. 이렇게 객체 의존관계를 외부에서 넣어주는 것을 DI(Dependency Inversion), 의존성 주입이라고 한다.

하지만 memberService가 스프링 빈으로 등록되지 않아 오류가 발생한다.

![Untitled.png](/assets/images/Spring_Bean/Untitled.png)

### 스프링 빈을 등록하는 2가지 방법

1. 컴포넌트 스캔과 자동 의존관계 설정
2. 자바 코드로 직접 스프링 빈 등록하기

### 컴포넌트 스캔 원리

`@Component` 어노테이션이 있으면 스프링 빈으로 자동 등록된다. 이 때문에 `@Controller`도 컨트롤러가 자동 등록된 이유도 컴포넌트 스캔 때문이다.

`@Controller, @Service, @Repository` 모두 `@Component`를 포함하므로 자동으로 스프링 빈에 등록된다.

```java
@Service
public class MemberService {
     private final MemberRepository memberRepository;

     @Autowired
     public MemberService(MemberRepository memberRepository) {
          this.memberRepository = memberRepository;
     }
}
```

생성자에 `@Autowired`를 사용하면 객체 생성 시점에 스프링 컨테이너에서 해당 스프링 빈을 찾아서 주입한다.

![Untitled1.png](/assets/images/Spring_Bean/1.png)

어노테이션을 사용한 결과 memberService와 memberRepository가 스프링 컨테이너에 스프링 빈으로 등록된 것을 볼 수 있다.

- 스프링은 스프링 컨테이너에 스프링 빈을 등록할 때, 기본으로 싱글톤으로 등록한다(유일하게 하나만 등록해서 공유한다) 따라서 같은 스프링 빈이면 모두 같은 인스턴스다. 설정으로 싱글톤이 아니게 설정할 수 있지만, 특별한 경우를 제외하면 대부분 싱글톤을 사용한다.

## 자바 코드로 직접 스프링 빈 등록하기

기존 자동 의존관계설정 방식에서 사용한 어노테이션을 Controller만 제외하여 다 제거 후 자바 코드로 빈을 등록하면 다음과 같이 작성한다.

```java
@Configuration
public class SpringConfig {

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }

    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
}
```

`@Configuration` 어노테이션과 `@Bean` 어노테이션을 사용하여 작성자가 직접 스프링 컨테이너에 빈을 등록할 수 있다.

<aside>
📖 references 스프링 입문 -코드로 배우는 스프링 부트, 웹 MVC, DB접근 기술 by 김영한

</aside>
