---
title: "[자바의 정석] 다형성"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 다형성이란?

---

객체지향개념에서 다형성이란 여러가지 형태를 가질 수 있는 능력을 의미하며, **자바에서는 한 타입의 참조변수로 여러 타입의 객체를 참조할 수 있도록 함으로써 다형성을 프로그램적으로 구현**한 것이다.

예제를 통해 알아보자. 

```java
class Tv { 
		boolean power;
		int channel;

		void power() { power = !power; }
		void channelUp() { ++channel; } 
		void channelDown() { --chanell; } 
}

class CaptionTv extends Tv {
			String text;
			void caption(){}
} 
```

Tv클래스와 CaptionTv클래스가 위와 같이 정의되어 있을 때, 두 클래스간의 관계를 그림으로 나타내면 아래와 같다.

![Untitled.png](/assets/images/Java Polymorphism/Untitled.png)

여기서 인스턴스를 생성하려면 다음과 같은 코드를 작성해야 한다.

```java
Tv t = new Tv();
CaptionTv c = new CaptionTv();
```

위의 예처럼 인스턴스의 타입과 참조변수의 타입이 일치하는 것이 보통이지만, Tv와 CaptionTv클래스가 서로 상속관계에 있을 경우, 다음과 같이 조상 클래스 타입의 참조변수로 자손 클래스의 인스턴스를 참조하도록 하는 것도 가능하다!

```java
Tv t = new CaptionTv(); //조상 타입의 참조변수로 자손 인스턴스를 참조
```

그러면 이렇게 쓰는게 가능한데, 인스턴스랑 참조변수의 타입이 같을 때랑 조상 타입의 참조변수로 참조하는 것은 어떤 차이가 있는지 알아보자.

```java
CaptionTv c = new CaptionTv();
Tv t = new CaptionTv();
```

위의 코드를 그림으로 나타내면 다음과 같다.

![Untitled.png](/assets/images/Java Polymorphism/Untitled 1.png)


Tv타입의 참조변수로는 CaptionTv 인스턴스 중에서 Tv클래스의 멤버들만 사용할 수 있다. 따라서 생성된 CaptionTv 인스턴스의 멤버 중에서 Tv클래스에 정의 되지 않은 멤버, text와 caption()은 참조변수 t로 사용이 불가능하다. 둘 다 같은 타입의 인스턴스지만 참조변수의 타입에 따라 사용할 수 있는 멤버의 개수가 달라진다.

반대로 자손타입의 참조변수로 조상타입의 인스턴스를 참조하는 것은 불가능하다!!

```java
CaptionTv c = new Tv();
```

 자손타입의 참조변수로 조상타입의 인스턴스를 참조하는 것은 불가능한 이유는 실제 인스턴스 Tv의 멤버 개수보다 참조변수 c가 사용할 수 있는 멤버 개수가 더 많기 때문이다.

> 조상타입의 참조변수로 자손타입의 인스턴스를 참조할 수 있다.
반대로 자손타입의 참조변수로 조상타입의 인스턴스를 참조할 수는 없다.
> 

## 참조변수의 형변환

---

기본형 변수와 같이 참조변수도 형변환이 가능하다. 자손타입의 참조변수를 조상타입의 참조변수로, 조상타입의 참조변수를 자손타입의 참조변수의 형변환만 가능하다.
조상타입의 참조변수를 자손타입의 참조변수로 변환하는 것을 다운캐스팅(down-casting)이라고 하며, 자손타입의 참조변수를 조상타입의 참조변수로 변환하는 것을 업캐스팅이(up-casting)라고한다.

예를 들어 Car, FireEngine, Amubulane클래스가 있다고 해보자.

```java
class Car {
			String color;
			int door;
			void drive() {}
			void stop() {}
}

class FireEngine extends Car {
			void water() {}
}

class Ambulance extends Car{
			void siren(){}
}
```

여기서 Car타입 참조변수와 FireEngine타입 참조변수 간의 형변환을 하면

```java
Car car = null;
FireEngine fe = new FireEngine();
FireEngine fe2 = null;

car = fe; //업캐스팅
fe2 = (FireEngine)car; //다운 캐스팅
```

여기서 자손타입의 참조변수를 조상타입의 참조변수에 할당할 경우 형변환을 생략할 수 있어서`car = fe;`라고 해도된다. 반대로 조상타입의 참조변수를 자손타입의 참조변수에 저장할 경우 형변환을 생략할 수 없어
 `fe = (FireEngine) car;`와 같이 명시적으로 형변환을 해주어야 한다.

그렇다면 조상타입의 참조변수를 자손타입의 참조변수로 변환하는 것은 명시적으로 캐스팅해주어야하고, 자손타입의 참조변수를 조상타입의 참조변수로 변환하는 것은 생략가능할까?

예를 들어 Car타입의 참조변수 c를 Car타입의 조상인 Object타입의 참조변수로 형변환 하는 것은 참조변수가 다룰수 있는 멤버의 개수가 실제 인스턴스가 갖고 있는 멤버의 개수보다 적을 것이 분명해 문제가 되지 않는다!
반대로 Car타입의 참조변수 c를 자손인 FireEngine타입으로 변환하는 것은 참조변수가 다룰 수 있는 멤버의 개수를 늘리는 것으로, 실제 인스턴스의 멤버 개수보다 참조변수가 사용할 수 있는 멤버의 개수가 더 많아지므로 문제가 발생할 가능성이 있다!

> 참조변수의 형변환을 통해서, **참조하고 있는 인스턴스에서 사용할 수 있는 멤버의 범위를 조절**하는 것뿐이다.
> 

## instanceof 연산자

---

참조변수가 참조하고 있는 인스턴스의 실제 타입을 알아보기 위해 instanceof 연산자를 사용한다.

예를 들어 살펴보자

ch7/InstanceofTest.java

```java
class InstanceofTest {
	public static void main(String args[]) {
		FireEngine fe = new FireEngine();

		if(fe instanceof FireEngine) {
			System.out.println("This is a FireEngine instance.");
		} 

		if(fe instanceof Car) {
			System.out.println("This is a Car instance.");
		} 

		if(fe instanceof Object) {
			System.out.println("This is an Object instance.");
		} 

		System.out.println(fe.getClass().getName()); // 클래스의 이름 출력
	}
} // class
class Car {}
class FireEngine extends Car {}
```

```java
//실행결과
This is a FireEngine instance.
This is a Car instance.
This is an Object instance.
FireEngine
```

여기서 innstanceof 를 사용해 fe의 타입을 알아보니 모두 true가 되어 if문이 실행되었다.
그 이유는 FireEngine클래스는 Object클래스와 Car클래스의 자손 클래스이므로 조상이 멤버들을 상속받았기 때문에, FireEngine인스턴스는 Object인스턴스와 Car인스턴스를 포함하고 있는 셈이다.

> 어떤 타입에 대한 instanceof 연산의 결과가 true라는 것은 검사한 타입으로 형변환이 가능하다는 것을 뜻한다.
> 

## 참조변수와 인스턴스의 연결

---

메서드의 경우 조상 클래스의 메서드를 자손의 클래스에서 오버라이딩한 경우에도 참조변수의 타입에 관계없이 항상 실제 인스턴스의 메서드가 호출되지만, 멤버변수의 경우 참조변수의 타입에 따라 달라진다.

이말을 이해하기 위해 예제를 들어보자.
ch7/BindingTest.java

```java
class BindingTest{
	public static void main(String[] args) {
		Parent p = new Child();
		Child c = new Child();

		System.out.println("p.x = " + p.x);
		p.method();

		System.out.println("c.x = " + c.x);
		c.method();
	}
}

class Parent {
	int x = 100;

	void method() {
		System.out.println("Parent Method");
	}
}

class Child extends Parent {
	int x = 200;

	void method() {
		System.out.println("Child Method");
	}
}
```

```java
//실행결과
p.x = 100
Child Method
c.x = 200
Child Method
```

위의 코드로 실행해보면 우선 메서드들을 조상타입의 참조변수와 자식타입의 참조변수로 접근해서 메서드를 호출하면 똑같은 결과가 나오지만, 멤버변수들은 참조변수에 따라 값이 다르게 나온다.

> **메서드의 경우 조상 클래스의 메서드를 자손의 클래스에서 오버라이딩한 경우에도 참조변수의 타입에 관계없이 항상 실제 인스턴스의 메서드가 호출되지만, 멤버변수의 경우 참조변수의 타입에 따라 달라진다.**
> 

## 매개변수의 다형성

---

참조변수의 다형적인 특징은 메서드의 매개변수에 유용하게 적용할 수 있다.
언제 유용한지 알기 위해 Product, Tv, Computer, Audio, Buyer 클래스가 정의되어 있다고 예를 들어보자.

 

```java
class Product {
			int price;
			int bonusPoint;
}

class Tv extends Product{}
class Computer extends Product{}
class Audio extends Product{}

class Buyer {
			int money = 100;
			int bonusPoint = 0;
}
```

Product 클래스는 Tv, Audio, Computer 클래스의 조상이며, Buyer클래스는 제품을 구입하는 사람을 클래스로 표현한 것이다.
여기서 Buyer 클래스에 물건을 구입하는 기능의 메서드를 추가할거다. 구입할 대상이 필요하므로 매개변수로 구입할 제품을 넘겨받도록 할 것이다.

```java
void buy(Tv t) { 
			money = money - t.price;
			bonusPoint = bonusPoint + t.bonusPoint;
}
```

이런식으로 메서드를 작성하였지만, 지금 현재 매개변수로 Tv 타입의 인스턴스만 받을 수 있도록 되어있는데 만약 여기서 상품들이 더 들어난다면 그 개수만큼 메서드를 만들어야할 것이다. 이때 매개변수에 다형성을 적용하면 다음과 같이 하나의 메서드로 간단히 처리할 수 있다.

```java
void buy(Product p) { 
			money = money - p.price;
			bonusPoint = bonusPoint + p.bonusPoint;
}
```

이렇게 하면 Product타입의 참조변수로 Product 클래스의 자손 타입의 참조변수들을 매개변수로 받아들일 수 있어 훨씬 간단하게 코드를 구성할 수 있게 됐다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>