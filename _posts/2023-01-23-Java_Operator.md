---
title: "[자바의 정석] 연산자"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 연산자의 종류

---

| 종류 | 연산자 | 설명 |
| --- | --- | --- |
| 산술 연산자 | + - * / & << >> | 사칙연산과 나머지 연산 |
| 비교 연산자 | > < ≤ ≥ == ≠ | 크고 작음과 같고 다름을 비교 |
| 논리 연산자 | && || ! & | ^ ~ | 그리고와 또는으로 조건을 연결 |
| 대입 연산자 | = | 우변의 값을 좌변에 저장 |
| 기타 | (type) ?: instanceof  | 형변환 연산자, 삼항 연산자, instanceof 연산자 |

## 단항 연산자

---

### 증감연산자 ++ —

- 증감 연산자는 피연산자에 저장된 값을 1증가 또는 감소 시킨다.

> 증가 연산자(++) 피연산자의 값을 1 증가시킨다.
감소 연산자(—) 피연산자의 값을 1 감소시킨다.
> 

피연산자의 왼쪽에 위치하면 전위형(prefix), 오른쪽에 위치하면 후위형(postfix)라고 한다.

| 타입 | 설명 | 사용예 |
| --- | --- | --- |
| 전위형 | 값이 참조되기 전에 증가시킨다. | j= ++i; |
| 후위형 | 값이 참조된 후에 증가시킨다. | j= i++; |

전위/후위 연산자의 예제

```java
class OperatorEx1 {
	public static void main(String args[]) {
		int i=5;
		i++;		      // i=i+1;과 같은 의미이다. ++i;로 바꿔 써도 결과는 같다. 
		System.out.println(i);

		i=5;		      //	결과를 비교하기 위해 i값을 다시 5로 변경.
		++i;
		System.out.println(i);
	}
}
```

- 식을 계산하기 위해서는 식에 포함된 변수의 값을 읽어 와야 하는데, 전위형은 변수의 값을 먼저 증가시킨 후에 변수의 값을 읽어오는 반면, 후위형은 변수의 값을 먼저 읽어온 후 증가시킨다.

증감 연산자를 사용하면 코드가 간결해지지만 지나치면 코드가 복잡해져 이해하기가 어렵다.

<aside>
👉 증감연산자는 식에 두 번 이상 포함된 변수에 증감연산자를 사용하는 것은 피해야 한다.

</aside>

### 부호 연산자

- 부호 연산자 ‘-’는 피연삱의 부호를 반대로 변경한 결과를 반환한다.

## 비교 연산자

---

두 피연산자를 비교하는데 사용되는 연산자며, 연산결과는 오직 `true`와 `false`를 반환한다.

### 등가비교 연산자

- 두 피연산의 값이 같은지 또는 다른지를 비교하는 연산자(==, ≠)
- 기본형의 경우 **변수에 저장되어 있는 값**이 같은지를 알 수 있고, 참조형의 경우 **객체의 주소값**을 저장하기 때문에 두 개의 피연산자가 같은 객체를 가리키고 있는지를 알 수 있다.
- 기본형과 참조형은 서로 형변환이 불가능하므로 등가비교로 기본형과 참조형은 비교할 수 없다.

**등가비교 예제**

```java
class OperatorEx22 {
	public static void main(String args[]) { 
		float  f  = 0.1f;
		double d  = 0.1;
		double d2 = (double)f;

		System.out.printf("10.0==10.0f  %b\n", 10.0==10.0f);
		System.out.printf("0.1==0.1f    %b\n",  0.1==0.1f);
		System.out.printf("f =%19.17f\n", f);
		System.out.printf("d =%19.17f\n", d);
		System.out.printf("d2=%19.17f\n", d2);
		System.out.printf("d==f   %b\n", d==f);
		System.out.printf("d==d2  %b\n", d==d2);
		System.out.printf("d2==f  %b\n", d2==f);
		System.out.printf("(float)d==f  %b\n", (float)d==f);
	}
}
```

```java
//실행결과
10.0==10.0f  true
0.1==0.1f    false
f =0.10000000149011612
d =0.10000000000000000
d2=0.10000000149011612
d==f   false
d==d2  false
d2==f  true
(float)d==f  true
```

실행결과에서 d==f에서 false가 나온것을 볼 수 있다. 10.0 == 10.0f는 true로 나왔지만, 0.1 == 0.1f는 false가 나왔다. 이 이유는 정수형과 달리 실수향은 근사값으로 저장되기 때문에 오차가 발생했기 때문이다.

**0.1f는 저장할때 2진수로 변환하는 과정에서 오차가 발생한다**. 따라서 dobule형과 float형을 비교할때 false가 나온다.

따라서 float형과 double형을 비교할때는 double형을 float형으로 형변환 후 비교해야 한다.

### 문자열의 비교

---

두 문자열을 비교할 때는 비교 연산자==대신 `equals()`라는 메서드를 사용해야 한다. 비교 연산자는 두 문자열이 완전히 같은 것인지 비교할 뿐이므로, 문자열의 내용이 같은지 비교하기 위해서는 `equals()`를 사용하는 것이다.

문자열 비교 예제

```java
class OperatorEx23 {
	public static void main(String[] args) {
		String str1 = "abc";
		String str2 = new String("abc");

		System.out.printf("\"abc\"==\"abc\" ? %b%n", "abc"=="abc");
		System.out.printf(" str1==\"abc\" ? %b%n",    str1=="abc");
		System.out.printf(" str2==\"abc\" ? %b%n",    str2=="abc");
		System.out.printf("str1.equals(\"abc\") ? %b%n", str1.equals("abc"));
		System.out.printf("str2.equals(\"abc\") ? %b%n", str2.equals("abc"));
		System.out.printf("str2.equals(\"ABC\") ? %b%n", str2.equals("ABC"));
		System.out.printf("str2.equalsIgnoreCase(\"ABC\") ? %b%n", str2.equalsIgnoreCase("ABC"));
	}
}
```

```java
//실행결과
"abc"=="abc" ? true
 str1=="abc" ? true
 str2=="abc" ? false
str1.equals("abc") ? true
str2.equals("abc") ? true
str2.equals("ABC") ? false
str2.equalsIgnoreCase("ABC") ? true
```

str2와 “abc”의 내용이 같은데도 “==”로 비교하면, false를 결과로 얻는다. 내용은 같지만 서로 다른 객체라서 false를 반환한다. 그러나 `equals()`는 객체가 달라도 내용이 같으면 true를 반환한다. 그래서 문자열을 비교할 때는 항상 `equals()`를 사용해야 한다.

- `equalsIgnore()`는 대소문자를 구분하리 않고 구별할 때 사용한다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>