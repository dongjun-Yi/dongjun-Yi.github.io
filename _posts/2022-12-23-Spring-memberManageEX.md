---
title: Spring-입문 3. 회원 관리 예제
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
### 비즈니스 요구사항

- 데이터 : 회원ID, 이름
- 기능 : 회원등록, 조회

## 일반적인 웹 어플리케이션 구조

![Untitled.png](/assets/images/Spring_MemberManage_Ex/Untitled.png)

- 컨트롤러 : 웹 MVC의 컨트롤러 역할
- 서비스 : 핵심 비즈니스 로직 구현
- 리포지토리 : 데이터베이스에 접근, 도메인 객체를 DB에 저장하고 관리
- 도메인 : 비즈니스 도메인 객체 ex)회원, 주문, 쿠폰 등 주로 데이터베이스에 저장하고 관리됨

### 회원(도메인)

```java
public class Member {
    private Long id;
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

### **회원 리포지토리 인터페이스**

```java
public interface MemberRepository {
    Member save(Member member);

    Optional<Member> findById(Long id);

    Optional<Member> findByName(String name);

    List<Member> findAll();
}
```

### **회원 리포지토리 메모리 구현체**

```java
public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L;

    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }

    public void clearStore() {
        store.clear();
    }
}
```

### 회원 서비스 개발

```java
public class MemberService {
    private final MemberRepository memberRepository = new MemoryMemberRepository();

    public Long join(Member member) {
        //같은 이름이 있는 중복 회원 X
        validateDuplicatedMember(member); //중복 회원 검증

        memberRepository.save(member);
        return member.getId();
    }

    private void validateDuplicatedMember(Member member) {
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                            throw new IllegalStateException("이미 존재하는 회원입니다.");
                        }
                );
    }

    //전체 회원 조회
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
```

### 회원 레포지토리 테스트 케이스 작성

```java
class MemoryMemberRepositoryTest {
    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach(){
        repository.clearStore();
    }

    @Test
    public void save() {
				//given
        Member member = new Member();
        member.setName("spring");
				
				//when
        repository.save(member);

				//then
        Member result = repository.findById(member.getId()).get();
        //Assertions.assertEquals(member, result);
        assertThat(member).isEqualTo(result);
    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findById(member1.getId()).get();
        assertThat(member1).isEqualTo(result);
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2);
    }
}
```

test case는 given, when, then 구조로 생각하면 쉽게 작성할 수 있다.

given에는 데이터를 넣는 과정, when은 테스트하려는 메소드를 입력하고, then에는 실제 구현해놓은 코드가 잘 동작되는지 검증하는 로직을 넣으면 된다.

`assertThat`을 이용하여 `isEqualTo()`로 작성한 로직이 맞는지 테스트가 가능하다.

- 테스트는 각각 독립적으로 실행하여 테스트 순서간에 의존성을 갖으면 안된다.
- `@AfterEach` 어노테이션은 각 테스트가 종료될 때 마다 이 기능을 실행하므로, 위의 예제에서는 메모리 DB에 저장된 데이터를 삭제한다.

### 회원 서비스 테스트

```java
class MemberServiceTest {
    MemberService memberService;
    MemoryMemberRepository repository;

    @BeforeEach
    public void beforeEach() {
        repository = new MemoryMemberRepository();
        memberService = new MemberService(repository);
    }

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    void 회원가입() {
        //given
        Member member = new Member();
        member.setName("hello");

        //when
        Long saveId = memberService.join(member);

        //then
        Member findMember = memberService.findOne(saveId).get();
        assertThat(member.getName()).isEqualTo(findMember.getName());
    }

    @Test
    public void 중복_회원_예외() {
        //given
        Member member1 = new Member();
        member1.setName("spring");
        Member member2 = new Member();
        member2.setName("spring");

        //when
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
		}
}
```

`@BeforeEach` : 각 테스트 실행 전에 호출된다. 테스트가 서로 영향이 없도록 항상 새로운 객체를 생성하고, 의존관계도 새로 맺어준다.

<aside>
📖 references 스프링 입문 -코드로 배우는 스프링 부트, 웹 MVC, DB접근 기술 by 김영한

</aside>