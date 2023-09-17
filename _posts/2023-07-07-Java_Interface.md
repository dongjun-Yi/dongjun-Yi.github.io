---
title: "[자바의 정석] 인터페이스"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 인터페이스란?

---

인터페이스는 일종의 추상클래스다. 

- 인터페이스는 추상클래스처럼 추상메서드를 갖지만, 추상클래스보다 추상화 정도가 높아서 **추상클래스와 달리 몸통을 갖춘 일반 메서드 또는 멤버변수를 구성원으로 가질 수 없다**.
- 추상클래스를 부분적으로만 완성된 미완성 설계도면, **인터페이스는 구현된것은 아무것도 없고 밑그림만 그려져 있는 기본설계도라 할 수 있다**.
- 오직 추상메서드와 상수만을 멤버로 가질 수 있으며, 그외에는 허용되지 않는다.

## 인터페이스의 작성

---

키워드를 class 대신 interface를 사용한다.

```java
interface PlayingCard { 
			public static final int SPADE = 4;
			final int DIAMOND = 3;
			static int HEART = 2;
			int CLOVER = 1;

			public abstract String getCardNumber();
			String getCardKind();
}
```

- 모든 멤버변수는 `public static final`이어야 하며, 이를 생략할 수 있다.
- 모든 메서드는 `public abstract`여야 하며, 이를 생략할 수 있다.(단. static 메서드와 디폴트 메서드는 예외다.(JDK1.8부터))

## 인터페이스의 상속

---

인터페이스는 인터페이스로부터만 상속받을 수 있고, 클래스와 달리 다중상속을 지원한다.

```java
interface Movable { 
		void move(int x, int y);
}

interface Attackable { 
		void attack(Unit u);
}

interface Fightable extends Movable, Attackable{}
```

## 인터페이스의 구현

---

인터페이스도 추상클래스처럼 그 자체로는 인스턴스를 생성할 수 없으며 ,추상클래스가 상속을 통해 추상메서드를 완성하는 것처럼, 인터페이스도 자신에 정의된 추상메서드의 몸통을 만들어주는 클래스를 작성해야 하는데, `implements` 키워드를 사용한다.

```java
class Fighter implements Fightable { 
			void move(int x, int y);
			void attack(Unit u);
}
```

상속과 구현을 동시에도 할 수 있다.

```java
class Fighter extends Unit implements Fightable { 
			void move(int x, int y);
			void attack(Unit u);
}
```

## 인터페이스를 이용한 다중상속

---

인터페이스는 `static` 상수만 정의할 수 있으므로, 조상클래스의 멤버변수와 충돌하는 경우는 거의 없고 충돌한다 해도 클래스 이름을 붙여서 구분이 가능하다. 그리고 추상메서드는 구현내용이 없어 조상클래스의 메서드와 선언부가 일치하는 경우는 당연히 조상클래스 쪽의 메서드를 상속받으면 되므로 문제되지 않는다.

But, 이렇게 하면 상속받는 멤버의 충돌은 피하지만, **다중상속의 장점을 잃어 연관관계를 사용하여 구현하는것이 더 바람직하다.**

## 인터페이스를 이용한 다형성

---

인터페이스 타입의 참조변수로 이를 구현한 클래스의 인스턴스를 참조할 수 있으며, 인터페이스의 타입으로의 형변환도 가능하다.

```java
interface Parseable {
	// 구문 분석작업을 수행한다.
	public abstract void parse(String fileName);
}

class ParserManager {
	// 리턴타입이 Parseable인터페이스이다.
	public static Parseable getParser(String type) {
		if(type.equals("XML")) {
			return new XMLParser();
		} else {
			Parseable p = new HTMLParser();
			return p;
			// return new HTMLParser();
		}
	}
}

class XMLParser implements Parseable {
	public void parse(String fileName) {
		/* 구문 분석작업을 수행하는 코드를 적는다. */
		System.out.println(fileName + "- XML parsing completed.");
	}
}

class HTMLParser implements Parseable {
	public void parse(String fileName) {
		/* 구문 분석작업을 수행하는 코드를 적는다. */
		System.out.println(fileName + "-HTML parsing completed.");
	}
}

class ParserTest {
	public static void main(String args[]) {
		Parseable parser = ParserManager.getParser("XML");
		parser.parse("document.xml");
		parser = ParserManager.getParser("HTML");
		parser.parse("document2.html");
	}
}
```

리턴타입이 인터페이스라는 것은 메서드가 해당 인터페이스를 구현한 클래스의 인스턴스를 반환한다는 것을 의미한다.

## 디폴트 메서드와 static 메서드

---

원래는 인터페이스에 추상메서드만 선언할 수 있는데, JDK1.8부터 디폴트 메서드와 static메서드도 추가할 수 있게 되었다.
디폴트 메서드는 추상메서드의 기본적인 구현을 제공하는 메서드로, 추상메서드가 아니기 때문에 디폴트 메서드가  새로 추가되어도 해당 인터페이스를 구현한 클래스를 변경하지 않아도 된다.

```java
interface MyInterface {
			void method();
			default void newMethod();
}
```

위와 같이 디폴트 메서드를 추가하면 기존의 MyInterface를 구현한 클래스를 변경하지 않아도 된다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>