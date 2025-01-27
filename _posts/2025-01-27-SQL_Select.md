---
title: "SQL SELECT 데이터 검색"
author:
  name: dongjun-Yi
categories: [database]
tags: [sql, database]
render_with_liquid: false
---
- Select
    - `select`는 테이블에서 열을 지정하여 선택한다.
- where
    - `where`는 테이블에서 행을 지정하여 선택한다.
    - `where`는 조건식을 지정해 조건식은 참 또는 거짓의 진리값을 반환하는 식으로 조건식에서 만족한 행만 결과값으로 반환한다.
    
    ```sql
    select * from sample21 where no=2; // where 조건식 사용
    ```
    
    > select와 from 구의 내부 처리 순서
    `where`구에서 행 선택, `select`구에서 열 선택은 데이터베이스 서버 내부에서
    `where` → `select`구 순서로 처리된다.
    > 

- like
    - `where` 식에 =을 사용하면 셀의 데이터 값이 완전일치하는지를 비교하고 `like`를 사용하면 특정문자나 문자열이 포함되어있는지를 검색 가능하다.
    
    ```sql
     // where 조건식에 like술어를 사용하여 text열이 sql을 포함하는 행을 검색
    select * from sample25 where text like '%sql%';
    ```
    
- order by
    - 검색 결과의 행 순서를 바꿀 수 있다.
    - `order by` 구로 정렬하고 싶은 열을 지정한다. 이 열은 기준이되며 이 값을 기준으로 행 순서가 결정된다.
    - 내림차순(DESC), 오름차순(ASC, default) 2가지가 존재한다.
    
    ```sql
    select * from sample31 order by age;
    ```
    
    > order by 실행순서
    where → select→ order by
    > 
- limit
    - 반환되는 데이터의 개수를 제한할 수 있다.
    - `limit`은 `where`, `order by`, `limit`순으로 실행된다.

## 집계와 서브쿼리

---

SQL은 데이터 집합을 다루는 언어다. 여기서 집합의 개수나 합계와 같은 값을 알고 싶으면 집계함수를 사용하면된다.

```sql
count(집합), sum(집합), avg(집합), max(집합), min(집합)
```

집계함수는 인수로 집합을 지정한다. 집계함수의 특징은 복수의 값(집합)에서 하나의 값을 반환한다. 즉, `select`구에서 집계함수를 쓰면 하나의 행만 추출된다.

- group by
    - `group by`를 통해 집계함수로 넘겨줄 집합을 그룹으로 나눈다.
    - `group by`로 열을 지정하여 그룹화하면 같은 행이 하나의 그룹으로 묶이게 된다.
    
    ```sql
    // group by 구에 name열을 지정해 그룹화
    select name from sample51 group by name;
    ```
    
- having
    - 집계함수의 조건식을 지정하려면 `having`을 사용해야 하며 `where` 구에 사용하면 에러가 난다. 이유는 `where`구가 `group by`보다 먼저 처리되기 때문에 집계함수 조건은 where에서 사용 불가능하다.
    
    > 내부 처리 순서
    `where` → `group by`→ `having` → `select` → `order by` → `limit`
    > 
    - `group by`에 지정한 열 이외의 열은 집계함수를 사용하지 않은 채 `select` 구에 기술할 수 없다.
    
    ```sql
    select no, name, quantity from sample51 group by name;
    ```
    
    이유는 `group by`는 반환되는 결과가 그룹 당 하나의 행이 반환되는 데, 만약 지정되지 않은 열로 추출하면 그룹에 여러 값 중 어느 값을 선택해야되는지를 모르기 때문에 에러가 발생한다. 
    
- 서브 쿼리
    - 서브쿼리는 `select` 명령에 의한 질의문으로 SQL문안에 지정하는 하부 `select` 명령으로 지정한다.
    
    ```sql
    select from sample54 where a = (select MIN(a) from sample54);
    ```
    
- 스칼라 값
    - 스칼라 값이란 하나의 값을 반환하는 뜻으로 서브 쿼리에서 단 하나의 값을 반환한다면 스칼라 서브쿼리라고 부른다.
    - `where` 구에서 스칼라 값을 반환하는 서브 쿼리는 = 연산자로 비교할 수 있다.
    
    ```sql
    select from sample54 where a = (select MIN(a) from sample54);
    ```
    
    위와 같이 서브쿼리에 스칼라 값을 반환하도록 하여 비교 연산자를 통해 서브 쿼리로 사용하기 간편하다.
    
- 상관 서브쿼리
    - 상관 서브 쿼리란 메인 쿼리문과 서브 쿼리가 특정 관계를 맺는 것을 상관 서브쿼리라고 부른다.
    
    ```sql
    // 부모 테이블의 행을 셀값을 이용해 서브쿼리에서 비교연산자를 사용하기 때문에 이는 상관서브쿼리다.
    update sample551 set a='있음' where
    exists (select * from sample 552 where no2=no);
    ```
    

<aside>
📖 references  SQL 첫걸음 - 한빛미디어

</aside>