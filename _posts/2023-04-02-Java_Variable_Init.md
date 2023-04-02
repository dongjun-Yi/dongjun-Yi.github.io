---
title: "[자바의 정석] 변수의 초기화"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 변수의 초기화

---

멤버변수 초기화를 하지 않고도 자동적으로 변수의 자료형에 맞는 기본값으로 초기화가 이루어지므로 초기화 하지 않고 사용해도 되지만, 지역변수는 사용하기 전에 반드시 초기화해야 한다.

멤버변수의 초기화 방법에는 다음과 같이 3가지가 있다.

- 명시적 초기화(explict initialization)
- 생성자(Constructor)
- 초기화 블럭(initialization block)

## 명시적 초기화

---

변수의 선언과 동시에 초기화 하는 방법

```java
class Car{
		int door = 4; //기본형 변수의 초기화 
		Engine e = new Engine(); //참조형 변수의 초기화
}
```

## 초기화 블럭

---

초기화 블럭에는 클래스와 인스턴스 초기화 블럭 두 가지 종류가 있다. 클래스 초기화 블럭은 클래스변수의 초기화에 사용되고, 인스턴스 초기화 블럭은 인스턴스변수의 초기화에 사용된다.

```java
class BlockTest {

	static { // 클래스 초기화 블럭
		System.out.println("static { }");
	}

	{ //인스턴스 초기화 블럭
		System.out.println("{ }");
	}

	public BlockTest() {     
		System.out.println("ťýźşŔÚ");
	}

	public static void main(String args[]) {
		System.out.println("BlockTest bt = new BlockTest(); ");
		BlockTest bt = new BlockTest();

		System.out.println("BlockTest bt2 = new BlockTest(); ");
		BlockTest bt2 = new BlockTest();
	}
}
```

클래스 초기화 블럭은 앞에 static을 붙이고, 인스턴스 블럭은 {}만 만들어주면 된다.
클래스 초기화 블럭은 처음 메모리에 로딩될 때 한번만 수행되지만, 인스턴스 초기화 블럭은 인스턴스가 생성될 때 마다 수행된다.

## 멤버변수의 초기화 시기와 순서

---

- 클래스변수의 초기화 순서 : 기본값 → 명시적 초기화 → 클래스 초기화 블럭
- 인스턴스변수의 초기화 순서 : 기본값 → 명시적 초기화 → 인스턴스 초기화 블럭 → 생성자

```java
class InitTest {
		static int cv=1;
		int iv=1;

		static { cv=2;}
		{ iv= 2;}

		InitTest() {
				iv=3;
		}
}
```

1. cv가 메모리에 생성되고, cv에는 int형의 기본값인 0이 cv에 저장된다.
2. 그 다음에는 명시적 초기화(int cv=1)에 의해 cv에 1이 저장된다.
3. 마지막으로 클래스 초기화 블럭(cv=2)이 수행되어 cv에는 2가 저장된다.
4. InitTest클래스의 인스턴스가 생성되면서 iv가 메모리에 존재하게 된다.
iv 역시 int형 변수이므로 기본값 0이 저장된다.
5. 명시적 초기화에 의해서 iv에 1이 저장되고 인스턴스 초기화 블럭이 수행되어 iv에 2가 저장된다.
6. 마지막으로 생성자가 수행되어 iv에는 3이 저장된다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>