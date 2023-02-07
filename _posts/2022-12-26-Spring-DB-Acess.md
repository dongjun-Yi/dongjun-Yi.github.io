---
title: "[Spring] 데이터베이스 접근방식"
author:
  name: dongjun-Yi
categories: [Spring]
tags: [java, Spring]
render_with_liquid: false
---
## 순수 JDBC

---

과거에 사용하던 방식이어서 사용하는 방식만 살펴보자

save 메소드에서 사용된 jdbc 로직

```java
public class JDBCMemberRepository implements MemberRepository {

    private final DataSource dataSource;

    public JDBCMemberRepository(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public Member save(Member member) {
        String sql = "insert into member(name) values(?)";
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            conn = getConnection();
            pstmt = conn.prepareStatement(sql,
                    Statement.RETURN_GENERATED_KEYS);
            pstmt.setString(1, member.getName());
            pstmt.executeUpdate();
            rs = pstmt.getGeneratedKeys();
            if (rs.next()) {
                member.setId(rs.getLong(1));
            } else {
                throw new SQLException("id 조회 실패");
            }
            return member;
        } catch (Exception e) {
            throw new IllegalStateException(e);
        } finally {
            close(conn, pstmt, rs);
        }

    }
}
```

## 스프링 통합 테스트

---

스프링 컨테이너와 DB까지 연결한 통합 테스트

```java
@SpringBootTest
@Transactional
class MemberServiceIntegrationTest {
    @Autowired
    MemberService memberService;
    @Autowired
    MemberRepository repository;

    @Test
    void 회원가입() {
        //given
        Member member = new Member();
        member.setName("spring");

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
```

@SpringBootTest는 스프링 컨테이너와 테스트를 함께 실행한다.

@Transactional은 테스트 시작 전에 **트랜잭션을 시작하고 테스트 완료 후 항상 롤백**을 해준다. 이렇게 하면 DB에 데이터가 남지 않기 때문에 다음 테스트에 영향을 주지 않는다.

## 스프링 Jdbc Template

---

기존 순수 jdbc에서 템플릿 메소드 패턴을 적용하여 중복된 코드를 줄여 순수 jdbc보다 단순한 형태로 코드를 구성할 수 있다.

```java
public class JDBCTemplateMemberRepository implements MemberRepository {

    private final JdbcTemplate jdbcTemplate;

    public JDBCTemplateMemberRepository(DataSource dataSource) {
        jdbcTemplate = new JdbcTemplate(dataSource);
    }

    @Override
    public List<Member> findAll() {
        return jdbcTemplate.query("select * from member", memberRowMapper());
    }
		private RowMapper<Member> memberRowMapper() {
        return (rs, rowNum) -> {
            Member member = new Member();
            member.setId(rs.getLong("id"));
            member.setName(rs.getString("name"));
            return member;
				}; 
		}
}
```

findAll메소드만 살펴보면 jdbcTemplate 객체를 이용하여 sql문을 작성하면 데이터베이스에서 데이터를 가져올 수 있는 것을 볼 수 있다.

## JPA(Java Persistence Api)

---

JPA는 반복적인 코드를 줄일 수 있고 기본적인 sql도 JPA가 직접 만들어서 실행해준다.

Member 클래스를 @Entity 어노테이션으로 매핑해주고 회원 레포지토리를 JPA를 이용하여 구성하면 다음과 같이 구성된다.

```java
public class JpaMemberRepository implements MemberRepository {

    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        Member member = em.find(Member.class, id);
        return Optional.ofNullable(member);
    }

    @Override
    public Optional<Member> findByName(String name) {
        List<Member> result = em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList();
        return result.stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }
}
```

코드가 전에 사용한 Jdbc보다 확연하게 줄어든 것을 볼 수 있다. 

이 후 서비스 계층에 트랜잭션을 추가해줘야 한다.

```java
@Transactional
public class MemberService {}
```

**JPA를 통한 모든 데이터 변경은 트랜잭션 안에서 실행해야 한다.**

## 스프링 데이터 JPA

---

레포지토리에 구현 클래스 없이 인터페이스만으로 개발을 할 수 있다.

```java
public interface SpringDataJpaMemberRepository extends JpaRepository<Member, Long>, MemberRepository {
    @Override
    Optional<Member> findByName(String name);
}
```

<aside>
📖 references 스프링 입문 -코드로 배우는 스프링 부트, 웹 MVC, DB접근 기술 by 김영한

</aside>