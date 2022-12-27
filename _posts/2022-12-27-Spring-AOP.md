---
title: Spring-입문 6. AOP
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---

## AOP(Aspect Oriented Programming)란?

---

**AOP is a programming paradigm that aims to increase modularity by allowing the separation of cross-cutting concerns.** It does this by adding additional behavior to existing code without modifying the code itself.

[https://www.baeldung.com](https://www.baeldung.com/) 에 따르면 AOP는 횡단 관심사를 분리하여 모듈성을 증가시키기 위해 맞춰진 프로그래밍 패라다임이라고 나와있다. 코드 자체를 수정하지 않고 기존 코드에 추가 동작을 추가하여 이를 수행하도록 한다고 나와 있는데, 여기서 횡단 관심사는 뭘까?

횡단 관심사의 예시로는 로깅, 인증, 트랜잭션과 같은 공통적이고 중복되는 내용들이 있다. 이는 중복코드를 발생 시키고 Method의 핵심 로직을 파악하기 어렵게 하고, 코드 가독성을 떨어뜨리며, 유지보수의 난이도를 높이는 요소들이다. 이를 해결 하기 위해 **AOP(Aspect Oriented Programming)** 이라는 개념이 탄생하였다.

예를 들어 모든 메소드에 호출 시간을 측정을 한다고 가정하자.

그러면 MemberSerivce의 코드는 다음과 같다.

```java
@Transactional
public class MemberService {
    /**
* 회원가입
*/
    public Long join(Member member) {
        long start = System.currentTimeMillis();
		try {
				validateDuplicateMember(member); //중복 회원 검증
        memberRepository.save(member);
        return member.getId();
      } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("join " + timeMs + "ms");
} }
/**
*전체 회원 조회
*/
    public List<Member> findMembers() {
        long start = System.currentTimeMillis();
        try {
            return memberRepository.findAll();
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("findMembers " + timeMs + "ms");
} }
}
```

모든 메소드에다 시간을 측정하는 로직을 다 추가해줘야 하는 번거로움이 있다. 이때 사용하는 것이 AOP이다.

AOP는 **공통 관심 사항**과 **핵심 관심 사항**을 분리해주는 기능을 가지고 있다. 여기서 **공통 관심 사항은 시간을 측정하는 기능이고, 핵심 관심 사항은 비즈니스 로직이 된다.**

공통 관심 사항(cross-cutting concern) vs 핵심 관심 사항(core concern) 분리
![Untitled.png](/assets/images/Spring_AOP/Untitled.png)

**AOP 등록**

```java
@Aspect
@Component
public class TimeTraceAop {

    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        System.out.println("start = " + joinPoint.toString());
        try {
            return joinPoint.proceed();
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("End = " + joinPoint.toString() + " " + timeMs + "ms");
        }
    }
}
```

이렇게 하여 회원가입, 회원 조회 등 핵심 관심 사항과 시간을 측정하는 공통 관심 사항을 분리했다.

시간을 측정하는 로직을 별도의 공통 로직으로 만들었다.

횡단 관심사와 핵심로직
![Untitled1.png](/assets/images/Spring_AOP/Untitled 1.png)


결국 위의 예제에서 공통 관심사인 시간을 측정하는 로직이 횡단 관심사가 되며 , 여러 모듈들이 시간 측정하는 로직을 사용할 수 있게 되는 것이다.

## AOP 동작 방식

---
**AOP 적용 전 의존관계**
![Untitled2.png](/assets/images/Spring_AOP/Untitled 2.png)


**AOP 적용 후 의존관계**
![Untitled3.png](/assets/images/Spring_AOP/Untitled 3.png)


AOP를 등록하면 스프링 컨테이너에 프록시 memberService빈이 등록되고 memberController는 프록시 memberService와 연관관계를 맺게 된다. 이후 j`oinPoint.proceed()`를 실행하면 실제 memberService가 실행되게 된다. 이렇게 하여 공통 관심 사항을 메소드마다 적용할 수 있게 되어 핵심 관심 사항을 분리할 수 있게 된다.

<aside>
📖 references 스프링 입문 -코드로 배우는 스프링 부트, 웹 MVC, DB접근 기술 by 김영한

[https://jaehun2841.github.io/2018/07/20/2018-07-20-spring-aop2/#AOP의-등장배경]

</aside>