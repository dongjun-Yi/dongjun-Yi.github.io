---
title: Spring-핵심 원리 기본편 2. 스프링 컨테이너와 빈
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## 스프링 컨테이너 생성

---

```java
ApplicationContext applicationContext = new 
													AnnotationConfigApplicationContext(AppConfig.class);
```

ApplicationContext를 스프링 컨테이너라고 한다.

### 스프링 컨테이너 생성 과정

![Untitled.png](/assets/images/Spring_Container_Bean/Untitled.png)

new AnnotationConfigApplicationContext(AppConfig.class)을 이용해 컨테이너를 생성하고 		AppConfig.class를 활용해서 빈 저장소를 구성한다.

### 스프링 빈 등록

![Untitled1.png](/assets/images/Spring_Container_Bean/Untitled 1.png)

설정 클래스 정보를 사용해서 스프링 빈을 등록한다.

### 스프링 빈 의존관계 설정 - 준비

![Untitled2.png](/assets/images/Spring_Container_Bean/Untitled 2.png)

### 스프링 빈 의존관계 설정 - 완료

![Untitled3.png](/assets/images/Spring_Container_Bean/Untitled 3.png)

스프링 컨테이너는 빈을 등록한 후 빈끼리 의존관계를 주입해준다.

> 스프링은 빈을 생성하고, 의존관계를 주입하는 단계가 나누어져 있다. 그런데 이렇게 자바 코드로 스프링 빈을 등록하면 생성자를 호출하면서 의존관계 주입도 한번에 처리된다.
> 

## 빈 출력하기

---

**모든 빈 출력**

```java
public class ApplicationContextInfoTest {
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("모든 빈 출력하기")
    void findAllBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName : beanDefinitionNames) {
            Object bean = ac.getBean(beanDefinitionName);
            System.out.println("name = " + beanDefinitionName + " object = "+ bean);
        }
    }
}
```

`ac.getBeanDefinitionNames()`: 스프링에 등록된 모든 빈 이름을 조회

`ac.getBean()` : 빈 이름으로 빈 객체를 조회

**어플리케이션 빈 출력**

```java
public class ApplicationContextInfoTest {
    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("어플리케이션 빈 출력하기")
    void findApplicationBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName : beanDefinitionNames) {
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);
            if(beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION){
                Object bean = ac.getBean(beanDefinitionName);
                System.out.println("name = " + beanDefinitionName + " object = " + bean);
            }
        }
    }
}
```

- 스프링 내부에서 사용하는 빈은 `getRole()`로 구분할 수 있다.
    - ROLE_APPLICATION : 일반적으로 사용자가 정의한 빈
    - ROLE_INFRASTRUCTURE : 스프링이 내부에서 사용하는 빈

`ac.getBeanDefinition()`: Bean에 대한 meta data 정보들을 반환한다. 코드에서는 스프링이 내부에서 사용하는 빈을 `getRole()`로 구분하기 위해 사용함.

**스프링 빈 조회 - 기본**

```java
public class ApplicationContextBasicFindTest {

    ApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 이름으로 조회")
    void findBeanByName() {
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("이름 없이 타입으로만 조회")
    void findBeanByType() {
        MemberService bean = ac.getBean(MemberService.class);
        assertThat(bean).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("구체 타입으로 조회")
    void findBeanBySpecificType() {
        MemberServiceImpl bean = ac.getBean(MemberServiceImpl.class);
        assertThat(bean).isInstanceOf(MemberServiceImpl.class);
    }

    @Test
    @DisplayName("빈 이름으로 조회했는데 없을 경우")
    void findBeanByNameX() {
        Assertions.assertThrows(NoSuchBeanDefinitionException.class, ()
                -> ac.getBean("xxxxx", MemberService.class));
    }
}
```

`ac.getBean(빈이름, 타입)` , `ac.getBean(타입)`으로 조회

**스프링 빈 조회 - 동일한 타입이 2개 있을 때, 타입으로 조회했을 시**

- 타입으로 조회시 같은 타입의 스프링 빈이 둘 이상이면 오류가 발생한다. 이때는 빈 이름을 지정하자.

```java
public class ApplicationContextSameBeanFindTest {

    ApplicationContext ac = new AnnotationConfigApplicationContext(SameBeanConfig.class);

    @Test
    @DisplayName("타입으로 조회시 같은 타입이 둘 이상 있으면, 중복 오류가 발생한다.")
    void findBeanByTypeDuplicate() {
        assertThrows(NoUniqueBeanDefinitionException.class,
                () -> ac.getBean(MemberRepository.class));
    }

    @Test
    @DisplayName("타입으로 조회시 같은 타입이 둘 이상 있으면, 빈 이름을 지정하면 된다.")
    void findBeanByName() {
        MemberRepository memberRepository = ac.getBean("memberRepository1", MemberRepository.class);
        assertThat(memberRepository).isInstanceOf(MemberRepository.class);
    }

    @Test
    @DisplayName("특정 타입을 모두 조회하기")
    void findAllBeanByType() {
        Map<String, MemberRepository> beansOfType = ac.getBeansOfType(MemberRepository.class);
        for (String key : beansOfType.keySet()) {
            System.out.println("key = " + key + " value = " + beansOfType.get(key));
            System.out.println("beansOfType = " + beansOfType);

            assertThat(beansOfType.size()).isEqualTo(2);
        }
    }

    @Configuration
    static class SameBeanConfig {
        @Bean
        public MemberRepository memberRepository1() {
            return new MemoryMemberRepository();
        }

        @Bean
        public MemberRepository memberRepository2() {
            return new MemoryMemberRepository();
        }
    }
}
```

`ac.getBeansOfType(타입)`을 사용하면 타입에 해당하는 모든 빈을 조회할 수 있다.

## **스프링 빈 조회 - 상속 관계**

---

![Untitled4.png](/assets/images/Spring_Container_Bean/Untitled 4.png)

- 부모 타입으로 빈을 조회하면 자식 타입도 모두 조회된다.
- 자바 객체의 부모인 Object타입으로 조회하면 모든 스프링 빈이 조회된다.

```java
public class ApplicationContextExtendsFindTest {
    ApplicationContext ac = new AnnotationConfigApplicationContext(TestConfig.class);

    @Test
    @DisplayName("부모 타입으로 조회시, 자식이 둘 이상 있으면, 중복 오류가 발생한다")
    void findBeanByParentTypeDuplicate() {
        assertThrows(NoUniqueBeanDefinitionException.class,
                () -> ac.getBean(DiscountPolicy.class));
    }

    @Test
    @DisplayName("부모 타입으로 조회시, 자식이 둘 이상 있으면, 빈 이름을 지정하면 된다")
    void findBeanByParentTypeBeanName() {
        DiscountPolicy rateDiscountPolicy = ac.getBean("rateDiscountPolicy", DiscountPolicy.class);
        assertThat(rateDiscountPolicy).isInstanceOf(DiscountPolicy.class);
    }

    @Test
    @DisplayName("특정 하위 타입으로 조회")
    void findBeanBySubType() {
        RateDiscountPolicy bean = ac.getBean(RateDiscountPolicy.class);
        assertThat(bean).isInstanceOf(RateDiscountPolicy.class);
    }

    @Test
    @DisplayName("부모 타입으로 모두 조회하기")
    void findAllBeanByParentType() {
        Map<String, DiscountPolicy> beansOfType = ac.getBeansOfType(DiscountPolicy.class);
        assertThat(beansOfType.size()).isEqualTo(2);
        for (String key : beansOfType.keySet()) {
            System.out.println("key = " + key + " value = " + beansOfType.get(key));
        }
    }

    @Test
    @DisplayName("부모 타입으로 모두 조회하기 - Object")
    void findAllBeanByObject() {
        Map<String, Object> beansOfType = ac.getBeansOfType(Object.class);
        for (String key : beansOfType.keySet()) {
            System.out.println("key = " + key + " value = " + beansOfType.get(key));
        }
    }

    @Configuration
    static class TestConfig {
        @Bean
        public DiscountPolicy fixDiscountPolicy() {
            return new FixDiscountPolicy();
        }

        @Bean
        public DiscountPolicy rateDiscountPolicy() {
            return new RateDiscountPolicy();
        }
    }
}
```

## BeanFactory와 ApplicationContext

---

![Untitled5.png](/assets/images/Spring_Container_Bean/Untitled 5.png)

- **BeanFactory**
    - 스프링 컨테이너의 최상위 인터페이스
    - 스프링 빈을 관리하고 조회하는 역할을 담당한다.
    - getBean()을 제공
- ApplicationContext
    - BeanFactory의 기능을 모두 상속받아서 제공한다.
    - ApplicationContext는 BeanFactory가 제공하는 기능 외에 부가기능까지 제공한다.
    

### ApplicationContext

![Untitled6.png](/assets/images/Spring_Container_Bean/Untitled 6.png)

- MessageSource
    - **메세지 소스를 활용한 국제화 기능**
- EnvironmentCapable
    - **환경변수**
- ApplicationEventPublisher
    - **어플리케이션 이벤트**
- ResourceLoader
    - **편리한 리소스 조회**

## 다양한 설정 형식 지원

---

![Untitled7.png](/assets/images/Spring_Container_Bean/Untitled 7.png)

스프링 컨테이너는 자바코드, XML 등 다양한 형식의 설정 정보를 받아드릴 수 있게 유연하게 설계되어 있다.

## **스프링 빈 설정 메타 정보 - BeanDefinition**

---

스프링은 BeanDefinition이라는 추상화가 있어 다양한 설정형식을 지원한다.

![Untitled8.png](/assets/images/Spring_Container_Bean/Untitled 8.png)

BeanDefinition을 빈 설정 메타 정보라 하며, 스프링 컨테이너는 이 메타 정보를 기반으로 스프링 빈을 생성한다.

**코드레벨 BeanDefinition**

![Untitled9.png](/assets/images/Spring_Container_Bean/Untitled 9.png)

AnnotationConfigApplicationContext 는 AnnotatedBeanDefinitionReader 를 사용해서
AppConfig.class 를 읽고 BeanDefinition 을 생성한다.

**BeanDefinition 정보**

- BeanClassName: 생성할 빈의 클래스 명(자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
- factoryBeanName: 팩토리 역할의 빈을 사용할 경우 이름, 예) appConfig
- factoryMethodName: 빈을 생성할 팩토리 메서드 지정, 예) memberService
- Scope: 싱글톤(기본값)
- lazyInit: 스프링 컨테이너를 생성할 때 빈을 생성하는 것이 아니라, 실제 빈을 사용할 때 까지 최대한
생성을 지연처리 하는지 여부
- InitMethodName: 빈을 생성하고, 의존관계를 적용한 뒤에 호출되는 초기화 메서드 명
- DestroyMethodName: 빈의 생명주기가 끝나서 제거하기 직전에 호출되는 메서드 명
- Constructor arguments, Properties: 의존관계 주입에서 사용한다. (자바 설정 처럼 팩토리 역할의

빈을 사용하면 없음)

```java
public class BeanDefinitionTest {

    AnnotationConfigApplicationContext ac = new AnnotationConfigApplicationContext(AppConfig.class);

    @Test
    @DisplayName("빈 설정 메타정보 확인")
    void findApplicationBean() {
        String[] beanDefinitionNames = ac.getBeanDefinitionNames();
        for (String beanDefinitionName : beanDefinitionNames) {
            BeanDefinition beanDefinition = ac.getBeanDefinition(beanDefinitionName);
            if (beanDefinition.getRole() == BeanDefinition.ROLE_APPLICATION) {
                System.out.println("beanDefinitionName = " + beanDefinitionName + " beanDefinition = " + beanDefinition);
            }
        }
    }
}
```

<aside>
📖 references 스프링 핵심원리 -기본편 by 김영한

</aside>