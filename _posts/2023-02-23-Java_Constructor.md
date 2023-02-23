---
title: "[자바의 정석] 생성자"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 생성자란?

---

생성자는 인스턴스가 생성될 때 호출되는 ‘인스턴스 초기화 메서드’이다. 인스턴스 생성 시에 실행되어야 할 작업을 위해서도 사영된다.

생성자의 조건은 다음과 같다.

1. 생성자의 이름은 클래스의 이름과 같아야 한다.
2. 생성자는 리턴 값이 없다.

```java
Card c = new Card();

1. 연산자에 의해서 메모리(heap)에 Card클래스의 인스턴스가 생성된다.
2. 생성자 Card()가 호출되어 수행된다.
3. 연산자 new의 결과로, 생성된 Card인스턴스의 주소가 반환되어 참조변수 c에 저장된다.
```

인스턴스를 생성할 때는 반드시 클래스 내에 정의된 생성자 중의 하나를 선택하여 지정해주어야 한다.

## 기본 생성자

---

컴파일 할 때, 소스파일(.java)의 클래스에 생성자가 하나도 정의되지 않은 경우 컴파일러는 자동적으로 아래와 같은 내용의 기본 생성자를 추가하여 컴파일 한다.

```java
클래스 이름(){}
Card(){}
```

ch6/ConstructorTest.java

```java
class Data1 {
	int value;
}

class Data2 {
	int value;

	Data2(int x) { 	// 매개변수가 있는 생성자.
		value = x;
	}
}

class ConstructorTest {
	public static void main(String[] args) {
		Data1 d1 = new Data1();
		Data2 d2 = new Data2();		// compile error발생
	}
}
```

위와 같이 코드를 작성하면 `d2 = new Data2()`에서 에러가 발생한다. 그 이유는 Data2에는 이미 생성자 Data2(int x)가 정의되어 있기 때문에 기본 생성자가 추가되지 않는다.
따라서 올바르게 인스턴스를 생성하려면 `d2 = new Data2(10)`과 같은 형태로 작성해야 한다.

> 기본 생성자가 컴파일러에 의해 추가되는 경우는 클래스에 정의된 생성자가 하나도 없을때 뿐이다.!
> 

## 매개변수가 있는 생성자

---

인스턴스는 각기 다른 값으로 초기화되어야하는 경우가 많기 때문에 매개변수를 사영한 초기화는 매우 유용하다.
예제를 들어 유용한지 확인해보자

```java
class Car {
	String color;		// 색상
	String gearType;	// 변속기 종류 - auto(자동), manual(수동)
	int door;			// 문의 개수

	Car() {}
	Car(String c, String g, int d) {
		color = c;
		gearType = g;
		door = d;
	}
}

class CarTest {
	public static void main(String[] args) {
		Car c1 = new Car();
		c1.color = "white";
		c1.gearType = "auto";
		c1.door = 4;

		Car c2 = new Car("white", "auto", 4);

		System.out.println("c1의 color=" + c1.color + ", gearType=" + c1.gearType+ ", door="+c1.door);
		System.out.println("c2의 color=" + c2.color + ", gearType=" + c2.gearType+ ", door="+c2.door);
	}
}
```

위의 예제에서 c1과 c2의 속성에 값을 초기화 하는거는 같지만 c1은 인스턴스를 생성한 다음 값을 초기화 했고, c2는 인스턴스를 생성하는 동시에 값을 대입했다 .c1이 가르키는 객체보다 c2가르키는 객체 의 생성 방식의 코드가 더 간결하고 직관적이다. 이처럼 클래스를 작성할 때 다양한 생성자를 제공함으로써 인스턴스 생성 후에 별도로 초기화를 하지 않아도 되도록하는게 좋다.

## 생성자에서 다른 생성자 호출하기 - this(), this

---

같은 클래스의 멤버들 간에 서로 호출할 수 있는 것처럼 생성자 간에도 서로 호출이 가능하다. 그러기 위해서는 다음과 두 조건을 만족시켜야 한다.

- 생성자의 이름으로 클래스 이름 대신 this를 사용한다.
- 한 생성자에서 다른 생성자를 호출할 때는 반드시 첫 줄에서만 호출이 가능하다.

```java
class Car {
	String color;		// 색상
	String gearType;	// 변속기 종류 - auto(자동), manual(수동)
	int door;			// 문의 개수

	Car() {
		this("white", "auto", 4);	
	}

	Car(String color) {
		this(color, "auto", 4);
	}
	Car(String color, String gearType, int door) {
		this.color    = color;
		this.gearType = gearType;
		this.door     = door;
	}
}

class CarTest2 {
	public static void main(String[] args) {
		Car c1 = new Car();	
		Car c2 = new Car("blue");

		System.out.println("c1의 color=" + c1.color + ", gearType=" + c1.gearType+ ", door="+c1.door);
		System.out.println("c2의 color=" + c2.color + ", gearType=" + c2.gearType+ ", door="+c2.door);
	}
}
```

위의 예제에서 생성자 Car()에서 또 다른 생성자 Car(String color, String gearType, int door)를 호출하였다. 이처럼 생성자간의 호출에는 생성자의 이름 대신 this를 사용해야만 하므로 ‘Car’대신 ‘this’를 사용하였다. 그리고 첫줄에서 호출하여 다른 생성자를 불렀다.

```java
Car(String color, String gearType, int door) {
		this.color    = color;
		this.gearType = gearType;
		this.door     = door;
	}
```

위의 코드처럼 생성자의 매개변수로 인스턴스 변수들의 초기값을 제공받는 경우가 많아 인스턴스변수의 이름과 일치하는 경우가 자주 있다. 이때 구별하기 위해 this를 사용하여 구별한다.

**this는 참조변수로, 인스턴스 자신을 가르킨다.** 참조변수를 통해 인스턴스의 멤버에 접근할 수 있는 것처럼 thi로 인스턴스변수에 접근할 수 있는 것이다.

또한 this을 사용할 수 있는 것은 인스턴스 멤버뿐이다. static 메서드에서는 인스턴스 멤버들을 사용할 수 없는 것처럼 this 역시 사용할 수 없다.

> this : 인스턴스 자신을 가르키는 참조변수, 인스턴스의 주소가 저장되어있다
모든 인스턴스 메서드에 지역변수에 숨겨진 채로 존재한다.
this() : 같은 클래스의 다른 생성자를 호출할 때 사용된다.
> 

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>