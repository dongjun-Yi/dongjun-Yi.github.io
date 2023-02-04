---
title: "[자바의 정석] 오버로딩"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 오버로딩이란?

---

한 클래스 내에 같은 이름의 메서드를 여러 개 정의하는 것을 ‘메서드 오버로딩(method overloading)’ 또느 간단히 오버로딩이라고 한다.

## 오버로딩의 조건

---

같은 이름의 메서드를 정의한다고 무조건 오버로딩이 아니다. 오버로딩이 성립하기 위해서는 다음과 같은 조건을 만족해야 한다.

1. 메서드 이름이 같아야 한다.
2. 매개변수의 개수 또는 타입이 달라야 한다.

메서드의 이름이 같다 해도 매개변수가 다르면 서로 구별될 수 있기 때문에 오버로딩이 가능한 것이다.

ex1)

```java
int add(int a, int b) { return a+b;}
int add(int x, int y) { return x+y;}
```

위의 두 메서드는 매개변수의 이름만 다른 뿐 매개변수의 타입이 같기 때문에 오버로딩이 성립하지 않는다.

ex2)

```java
int add(int a, int b) { return a+b;}
long add(int a, int b) { return (long) (a+b);}
```

위의 예제는 리턴 타입만 다를 뿐 매개변수의 타입과 개수가 일치하기 때문에 오버로딩이 성립하지 않는다.

ex3)

```java
long add(int a, long b) { return a+b;}
long add(long a, int b) { return a+b;}
```

두 메서드 모두 int형과 long형 매개변수가 하나씩 선언되어 있지만, 서로 순서가 다른 경우 호출 시 매개변수의 값에 의해 호출될 메서드가 구분될 수 있으므로 중복된 메서드가 아닌 오버로딩으로 간주한다.

- 오버로딩의 장점
    - 메서드를 사용하는 쪽에서는 이름을 일일이 구분해서 기억 안해도되고 기억하기 쉽다.
    - 메서드의 이름 절약가능

> 같은 일을 하지만 매개변수를 달리해야하는 경우에, 이와 같이 이름은 같고 매개변수를 다르게 하여 오버로딩을 구현한다.
> 

## 가변인자 오버로딩

---

기존에는 메서드의 매개변수 개수가 고정적이었으나 JDK1.5부터 동적으로 지정해 줄 수 있게 되었으며, 이기능을 가변인자(variable arguments)라고 한다.
가변인자는 “타입..변수명”과 같은 형식으로 선언하며, PrintStream클래스의 printf()가 대표적인 예다.

```java
public PrintStream printf(String format, Object.. args) {...}
```

위와 같이 가변인자 외에도 매개변수가 더 있다면, 가변인자를 매개변수 중에서 제일 마지막에 선언해야 한다. 그렇지 않으면, 컴파일 에러가 난다. 가변인자인지 아닌지를 구별할 방법이 없기 때문에 허용하지 않는 것이다.

```java
//컴파일 에러 발생 - 가변인자는 항상 마지막 매개변수여야 한다.
public PrintStream printf(Object... args, String format) { ...}
```

ch6/VarArgsEx.java

```java
class VarArgsEx {
	public static void main(String[] args) {
		String[] strArr = { "100", "200", "300" };
		
		System.out.println(concatenate("", "100", "200", "300"));
		System.out.println(concatenate("-", strArr));
		System.out.println(concatenate(",", new String[]{"1", "2", "3"}));
		System.out.println("["+concatenate(",", new String[0])+"]");
		System.out.println("["+concatenate(",")+"]");
	}

	static String concatenate(String delim, String... args) {
		String result = "";

		for(String str : args) {
			result += str + delim;
		}
		
		return result;
	}

/*
	static String concatenate(String... args) {
		return concatenate("",args);
	}
*/
} // class
```

가변인자는 내부적으로 배열을 이용한다. 가변인자가 선언된 메서드를 호출할 때마다 배열이 새로 생긴다.

만약 주석처리된 concatenate을 주석을 풀게 되면 컴파일 에러가 발생한다.
가변인자를 선언한 메서드를 오버로딩하면, 메서드를 호출했을 때 이와 같이 구별되지 못하는 경우가 발생하기 쉽기 때문에 주의해야 한다.

> 가능하면 가벼인자를 사용한 메서드는 오버로딩하지 않는 것이 좋다.
> 

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>