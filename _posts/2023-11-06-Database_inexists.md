---
title: "[데이터베이스] in과 exists 연산자 차이"
author:
  name: dongjun-Yi
categories: [database]
tags: [database]
render_with_liquid: false
---
## 중첩질의

---

`in`과 `exists`연산자는 중첩질의 중 하나인데, **중첩질의**란 SQL문을 다른 SQL문 안에 중첩하여 사용하는 질의를 의미한다. 이때 내부에 포함된 SQL문을 **부 질의**(sub query) 또는 **내부 질의**(inner query)라 하며 부 질의를 갖는 SQL문을 **외부 질의**(outer query)라고 한다.

```
스키마
course(course_id, title, credit)
class(class_id, course_id, year, semester, division, prof_id, classroom, enroll)
```

예를 들어 스키마 구조는 위와 같고, ‘301호’ 강의실에서 개설된 강좌의 과목명을 출력하는 SQL문은 다음과 같이 작성할 수 있다.

```sql
select title
from course
where course_id in
    (select distinct course_id from class where classromm = '301호')
```

위의 SQL문에서 부 질의 키워드 `in` 뒤에 나오는 SQL문으로서 class 테이블에서 강의실이 ‘301호’인 교과목 번호를 검색한다. 키워드 `in`은 부 질의의 검색 결과에 포함되는 경우를 나타낸다. 따라서 외부 질의에서는 course 테이블에서 **course_id 필드의 값이 부 질의의 검색 결과에 포함되는 경우**에만 과목명을 출력하게 된다.

또한 위의 예제를 `exists`를 이용해 SQL문을 작성해도 **같은 결과**를 얻을 수 있다.

```sql
select title
from course
where exists
    (select * 
    from class 
    where classromm = '301호' and course.course_id = class.course_id)
```

`exists`는 최소한 하나 이상의 레코가 존재하면 참이 되고 그렇지 않으면 거짓이 된다. 따라서 부질의 검색 결과에 최소한 하나 이상의 레코드가 존재하는지의 여부를 표현할 수 있다.

그렇다면 `in`과 `exists` 모두 중첩 질의이고 둘의 차이점은 무엇일까?

## `in`과 `exists`

---

`in`연산은 부질의의 SQL문을 실행하면 `select`연산으로 만족하는 모든 행을 추출한 뒤 외부 질의를 하게되지만, `exists`연산은 부 질의의 SQL문을 실행하면 하나라도 만족하는 행이 있다면 SQL엔진은 더 이상 탐색하지 않고 **참 혹은 거짓을 반환하여 외부 질의**를 하게 된다. 위의 예를 가지고 살펴보자

```sql
-- in 연산
select title
from course
where course_id in
    (select distinct course_id from class where classromm = '301호')
```

먼저 `in`연산을 사용한 SQL에서 부 질의의 실행결과는 아래와 같을 것이다.

| course_id |
| --- |
| C101 |
| C103 |
| C301 |

이후 course 테이블에서 부질의 연산의 결과인 course_id를 검색하여 title을 반환하면 아래와 같다.

| title |
| --- |
| 전산개론 |
| 데이터베이스 |
| 운영체제 |

반면, `exists`연산을 다시 보면

```sql
//exists
select title
from course
where exists
    (select * 
    from class 
    where classromm = '301호' and course.course_id = class.course_id)
```

`exists`는 `in` 구문과 다르게 **외부 쿼리에 먼저 접근하여 행 하나를 가져오고** `exists`**의 서브쿼리를 실행시켜 결과가 존재하는지를 판단**합니다.

서브쿼리의 결과가 true 인지 false 인지 체크하기 때문에 `exists`에서는 결과가 존재할 경우(= true) 메인 쿼리의 결과를 출력하고 `not exists`에서는 서브쿼리 내의 결과가 존재하지 않을 경우(= false) 메인 쿼리의 결과를 출력하게 된다.

> `in`은 서브 쿼리 → 외부 쿼리 순으로 실행
`exists`는 외부 쿼리 → 서브 쿼리 순으로 실행
> 

<aside>
💡 `in` 연산자는 **서브쿼리를 모두 검색**하고, `exists` **연산자는 찾을 때까지 검색**한다. 
따라서 서브쿼리의 데이터가 작을 경우 `in` 구문과 `exists` 의 성능은 크게 차이가 없지만, 서브쿼리에 **조회되는 데이터가 많아질수록** `exists`연산자가 `in`에 비해 성능이 더 좋다.

</aside>
<br><br>
<aside>
📖 references 
데이터베이스의 이해 [이한미디어]<br>
[https://wildeveloperetrain.tistory.com/223](https://wildeveloperetrain.tistory.com/223)<br>
[https://stackoverflow.com/questions/24929/difference-between-exists-and-in-in-sql](https://stackoverflow.com/questions/24929/difference-between-exists-and-in-in-sql)

</aside>