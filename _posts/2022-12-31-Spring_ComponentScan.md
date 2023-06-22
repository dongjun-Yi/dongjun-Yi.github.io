---
title: "[Spring] 컴포넌트 스캔"
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## **컴포넌트 스캔과 의존관계 자동 주입 시작하기**

---

- 스프링 빈을 `@Bean`을 사용하여 스프링 컨테이너에 등록했지만, 만약 등록해야 할 빈이 수백개가 넘는다면 설정 정보도 커지고, 누락하는 문제도 발생할 수 있다.
- 이 때문에 스프링은 자**동으로 스프링 빈을 등록하는 컴포넌트 스캔**이라는 기능을 제공한다.
- 또 의존관계도 자동으로 주입하는 `@Autowired` 라는 기능도 제공한다.

**AutoAppConfig**

```java
@Configuration
@ComponentScan(
        excludeFilters = @ComponentScan.Filter(type = FilterType.ANNOTATION, classes = Configuration.class)
)
public class AutoAppConfig {
}
```

- 컴포넌트 스캔을 사용하려면 먼저 `@ComponentScan` 을 설정 정보에 붙여주면 된다.
- 기존의 AppConfig와는 다르게 `@Bean`으로 등록한 클래스가 하나도 없다!

<aside>
👉 컴포넌트 스캔을 사용하면 `@Configuration` 이 붙은 설정 정보도 자동으로 등록되기 때문에, AppConfig, TestConfig 등 앞서 만들어두었던 설정 정보도 함께 등록되고, 실행되어 버린다. 그래서 excludeFilters 를 이용해서 설정정보는 컴포넌트 스캔 대상에서 제외했다.

</aside>

컴포넌트 스캔은 이름 그대로 `@Component` 어노테이션이 붙은 클래스를 스캔해서 스프링 빈으로 등록한다.

```java
@Component
public class MemoryMemberRepository implements MemberRepository {}
@Component
public class RateDiscountPolicy implements DiscountPolicy {}
@Component
public class MemberServiceImpl implements MemberService {
      private final MemberRepository memberRepository;
      @Autowired
      public MemberServiceImpl(MemberRepository memberRepository) {
          this.memberRepository = memberRepository;
      }
}
```

**AutoAppConfig Test**

```java
public class AutoAppConfigTest {
    @Test
    void basicScan() {
        ApplicationContext ac = new AnnotationConfigApplicationContext(AutoAppConfig.class);
        MemberService bean = ac.getBean(MemberService.class);
        assertThat(bean).isInstanceOf(MemberService.class);
    }
}
```

## 컴포넌트 스캔과 자동 주입 동작원리

---

1. **컴포넌트 스캔**

![Untitled.png](/assets/images/Spring_ComponentScan/Untitled.png)

- `@ComponentScan` 은 `@Component` 가 붙은 모든 클래스를 스프링 빈으로 등록한다.
- 이때 스프링 빈의 기본 이름은 클래스명을 사용하되 맨 앞글자만 소문자를 사용한다.
    - **빈 이름 기본 전략:** MemberServiceImpl 클래스 memberServiceImpl
    - **빈 이름 직접 지정:** 만약 스프링 빈의 이름을 직접 지정하고 싶으
- `@Component("memberService2")` 이런식으로 이름을 부여하면 된다.

1. `**@AutoWired` 의존관계 자동 주입**

![Untitled1.png](/assets/images/Spring_ComponentScan/1.png)

- 생성자에 `@Autowired` 를 지정하면, 스프링 컨테이너가 자동으로 해당 스프링 빈을 찾아서 주입한다.
- `getBean(MemberRepository.class)`를 이용해서 한다고 생각하면 된다.

## **탐색 위치와 기본 스캔 대상**

---

**탐색할 패키지의 시작 위치 지정**

```java
@ComponentScan(
          basePackages = "hello.core",
}
```

- basePackages : 탐색할 패키지의 시작 위치를 지정한다. 이 패키지를 포함해서 하위 패키지를 모두 탐색한다.
    - basePackages = {"hello.core", "hello.service"} 이렇게 여러 시작 위치를 지정할 수도 있다.
- basePackageClasses : 지정한 클래스의 패키지를 탐색 시작 위치로 지정한다.
- 만약 지정하지 않으면 `@ComponentScan` 이 붙은 설정 정보 클래스의 패키지가 시작 위치가 된다.

**컴포넌트 스캔 기본 대상**

- 컴포넌트 스캔은 `@Component` 뿐만 아니라 다음과 내용도 추가로 대상에 포함한다.
    - `@Component` : 컴포넌트 스캔에서 사용
    - `@Controlller` : 스프링 MVC 컨트롤러에서 사용
    - `@Service` : 스프링 비즈니스 로직에서 사용
    - `@Repository` : 스프링 데이터 접근 계층에서 사용
    - `@Configuration` : 스프링 설정 정보에서 사용

**필터**

- includeFilters : 컴포넌트 스캔 대상을 추가로 지정한다.
- excludeFilters : 컴포넌트 스캔에서 제외할 대상을 지정한다.

## **중복 등록과 충돌**

---

컴포넌트 스캔에서 만약 빈의 이름이 같으면 어떻게 될까?

**case1) 자동 빈 등록 vs 자동 빈 등록**

컴포넌트 스캔에 의해 자동으로 스프링 빈이 등록되는데, 그 이름이 같은 경우 스프링은 오류를 발생시킨다.

- ConflictingBeanDefinitionException 예외 발생

**case2)**  **수동 빈 등록 vs 자동 빈 등록**

- 이 경우 수동 빈 등록이 우선권을 가진다.
- 그러나 최근 스프링 부트에서는 수동 빈 등록과 자동 빈 등록이 **충돌나면 오류가 발생하도록 기본 값을 바꾸었다.**

<aside>
📖 references 스프링 핵심원리 -기본편 by 김영한

</aside>