---
title: "[JPA] 영속성 컨텍스트"
author:
  name: dongjun-Yi
categories: [JPA]
tags: [java, ORM, JPA]
render_with_liquid: false
---
## 엔티티 매니저 팩토리와 엔티티 매니저
---

![Untitled.png](/assets/images/PersistenceContext/Untitled.png)

**엔티 매니저 팩토리**는 이름 그대로 **엔티티 매니저를 만드는 공장**이고, **엔티티 매니저**는 엔티티를 저장하고, 수정하고, 삭제하고, 조회하는 등 엔티티와 관련된 모든일을 처리하는 **엔티티를 관리하는 관리자**이다.

## 영속성 컨텍스트란?

---

영속성 컨텍스트(Persistence Context)는 논리적인 개념으로 **엔티티를 영구 저장하는 환경이다.**

```java
EntityManger.persist(entity);
```

`persist()`는 엔티티 객체를 DB에 저장하는게 아니라 **영속성 컨텍스트**라는 곳에 저장한다. 즉, **엔티티 메니저를 통해 영속성 컨텍스트에 접근한다!**

![Untitled.png](/assets/images/PersistenceContext/1.png)

엔티티 메니저를 생성하면 영속성 컨텍스트와 1:1로 존재하게 된다.

## 엔티티의 생명주기

---

- **비영속(new/transient)** : 영속성 컨텍스트와 전혀 관계가 없는 새로운 상태

![Untitled.png](/assets/images/PersistenceContext/2.png)
```java
//객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member1");
member.setUserName("회원1");
```

- **영속(managed)** : 영속성 컨텍스트에 관리되는 상태

![Untitled.png](/assets/images/PersistenceContext/3.png)

```java
//객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member1");
member.setUserName("회원1");

EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
EntityManager em = new emf.createEntityManager();
em.getTransaction().begin();

//객체를 저장한 상태(영속)
em.persist(member);
```

- **준영속(detached)** : 영속성 컨텍스트에 저장되었다가 분리된 상태

```java
Member member = em.find(Member.class, 150L);
member.setName("AAA");
em.detach(member);
```

- **삭제(removed)** : 삭제된 상태

```java
Member member = em.find(Member.class, 150L);
member.setName("AAA");
em.remove(member);
```

## 영속성 컨텍스트의 이점

---

영속성 컨텍스트는 자바 어플리케이션과 DB중간에 있는 매개체로 다음과 같은 이점들이 있다.

### 1. 1차 캐시

---

![Untitled.png](/assets/images/PersistenceContext/4.png)

영속성 컨텍스트는 내부에 1차 캐시가 있다. 이해를 위해 아래의 코드를 보자

```java
//객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member1");
member.setUserName("회원1");

//엔티티를 영속
em.persist(member);
```

Member객체 생성 후 `em.persist(member)`를 실행하면 Member 데이터가 영속성 컨텍스트 내부에 1차캐시에 저장된다. 엔티티를 생성할 때 키로 매핑한 @ID와 엔티티 인스턴스로 key-value형태로 저장된다.
이 상태에서 만약 회원객체를 조회하면 어떤 일이 일어날까?

```java
Member member = new Member();
member.setId("member1");
member.setUserName("회원1");
//영속
em.persist(member);

Member findMember = em.find(Member.class, );
```

`em.find()`로 조회하면 JPA는 영속성 컨텍스트에서 1차 캐시에 member객체가 있는지 확인한다. 1차 캐시에 만약 member엔티티가 존재하면 1차캐시에서 값을 조회해온다. 

![Untitled.png](/assets/images/PersistenceContext/5.png)

근데 만약 아래의 코드로 member2를 조회해오면 

```java
Member findMember2 = em.find(Member.class, "member2");
```

![Untitled.png](/assets/images/PersistenceContext/6.png)

member2는 1차 캐시에 존재하지 않기 때문에 DB에서 member2를 조회한 후 1차  캐시에 저장한다. 그 후 member2를 반환한다.

> **위의 예처럼 1차캐시를 둠으로써 필요한 데이터를 조회했을 때 데이터가 1차 캐시에 존재하면 DB에 안거치고 데이터를 반환할 수 있다!**
> 

### 2. 영속 엔티티의 동일성 보장

---

```java
Member a = em.find(Member.class, "member1");
Member b = em.find(Member.class, "member1");
System.out.println(a == b); //동일성 비교 true
```

위의 코드를 실행하면 결과는 true가 반환된다. 마치 **자바 컬렉션**에서 꺼내서 똑같은 레퍼런스가 있는 객체를 꺼내면 ==비교했을때 true가 나오는것처럼 영속 엔티티도 1차 캐시에 존재했기 때문에 **동일성을 보장**해준다.

### 3. 쓰기 지연(transactional write-behind)

---

![Untitled.png](/assets/images/PersistenceContext/7.png)

영속성 컨텍스트안에는 1차캐시외에 **쓰기지연 SQL 저장소**라는곳이 있다. 위의 그림처럼 em.persist(memberA)로 영속성 컨텍스트에 넣으면 memberA가 1차캐시에 보관된다. 그러면서 동시에 JPA는 memberA엔티티를 분석해서 INSERT쿼리를 생성한다. 그 후 쓰기지연 SQL저장소에 쌓아둔다.

![Untitled.png](/assets/images/PersistenceContext/8.png)

또한 memberB를 persist()하게 되면 1차캐시에 저장되고, JPA는 INSERT쿼리를 쓰기지연 SQL저장소에 보관하게 된다.

![Untitled.png](/assets/images/PersistenceContext/9.png)

보내그 후 transaction을 commit()하게 되면 쓰지 지연 SQL저장소에 있던 SQL문들이 DB에 보내지게 된다. 그래서 실제 데이터베이스 트랜잭션이 commit되게 된다.

이와 같은 과정을 코드로 보면 아래와 같다.

```java
public class Main {
    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Member member1 = new Member(150L, "A");
            Member member2 = new Member(160L, "B");

            em.persist(member1);
            em.persist(member2);
            System.out.println("===========");
						tx.commit(); //커밋하는 시점에 db에 쿼리가 날라감
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
```

```java
//실행결과
===========
Hibernate: 
    /* insert hellojpa.Member
        */ insert 
        into
            Member
            (username, id) 
        values
            (?, ?)
Hibernate: 
    /* insert hellojpa.Member
        */ insert 
        into
            Member
            (username, id) 
        values
            (?, ?)
```

위의 결과처럼 `persist()`후 `commit()`시점에 INSERT쿼리가 2번 나갔다는것을 확인할 수 있다. 즉, 영속성 컨텍스트를 통해 **버퍼링의 기능**을 사용할 수 있다. 데이터베이스 커밋직전에만 INSERT쿼리가 나가면 되기 때문에 **한번에 모아서 쿼리가 날라가면 버퍼링의 이점을 얻을 수 있다!**

### 3. 엔티티 수정(변경 감지)

---

```java
EntityManager em = emf.createEntityManager();
EntityTransaction transaction = em.getTransaction();
transaction.begin(); // [트랜잭션] 시작// 영속 엔티티 조회

Member memberA = em.find(Member.class, "memberA");// 영속 엔티티 데이터 수정
memberA.setUsername("hi");memberA.setAge(10);//
//em.update(member)
transaction.commit(); // [트랜잭션] 커밋
```

현재 em.persist()나 em.update()같은 JPA에게 변경되었다라는 거를 알려주지 않아도 지금 위의 코드를 실행하면 DB에 변경사항이 잘 들어간거를 확인할 수 있다. 그 이유는 다음 그림과 같다.

![Untitled.png](/assets/images/PersistenceContext/10.png)

JPA는 내부적으로 **Dirty checking**이라는 것을 한다. JPA는 데이터베이스 트랜잭션을 커밋하는 시점에 내부적으로 `flush()`가 호출된다. `flush()`가 호출되면 엔티티와 스냅샷을 비교한다. 사실 1차 캐시안에는 @ID, Entity, 스냅샷이라는것으로 보관한다. **스냅샷은 최초 시점에 영속성 컨텍스트에 읽어온 값인다**. 이렇게 해놓은 상태에서 memberA값을 변경하면 JPA가 커밋시점에 스냅샷과 비교하게 된다. 비교 한뒤 만약 memberA의 값이 바뀌었다면 UPDATE쿼리를 쓰기지연SQL저장소에 넣어두고 업데이트 쿼리를 데이터베이스에 반영하고 커밋하게 된다.

## flush

---

플러시는 **영속성 컨텍스트의 변경내용을 데이터베이스에 반영하는 작업**이다.

영속성 컨텍스트를 플러시하는 방법은 3가지가 있다.

1. em.flush() - 플러시 수동 호출
2. transaction.commit() - 플러시 자동 호출
3. JPQL 쿼리 실행 - 플러시 자동 호출

다음 코드는 플러시를 수동으로 호출한 코드이다.

```java
public class Main {
    public static void main(String[] args) {

        EntityManagerFactory emf = Persistence.createEntityManagerFactory("hello");
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try {
            Member member1 = new Member(150L, "A");

	          em.persist(member1);
						em.flush(); //플러시 강제 호출
	
            System.out.println("===========");
						tx.commit(); 
        } catch (Exception e) {
            tx.rollback();
        } finally {
            em.close();
        }
        emf.close();
    }
}
```

```java
//실행결과
Hibernate: 
    /* insert hellojpa.Member
        */ insert 
        into
            Member
            (username, id) 
        values
            (?, ?)
===========
```

위의 결과처럼 commit()전에 flush()로 INSERT쿼리가 DB에 나가는것을 확인할 수 있다.

> 플러시를 하면 1차캐시를 비우는게 아니라 영속성 컨텍스트안에 쓰기지연 SQL저장소에서 데이터들이 바뀐 것이 DB에 반영하는 작업이다!
즉, 플러시는 **영속성 컨텍스트의 변경내용을 데이터베이스에 동기화하는 작업이다!!**
> 

## 준영속 상태

---

준영속 상태란 **영속 상태의 엔티티가 영속성 컨텍스트에서 분리된 상태(detached)**를 뜻한다.

아래의 명령어로 엔티티를 준영속상태로 전환할 수 있다.

```java
em.detach(entity); //특정 엔티티만 준영속 상태로 전환

em.clear() // 영속성 컨텍스트를 완전히 초기화

em.close() //영속성 컨텍스트를 종료
```

<aside>
📖 references 
자바 ORM 표준 JPA 프로그래밍 -기본편 by 김영한

</aside>