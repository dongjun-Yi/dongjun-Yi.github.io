---
title: "[자바의 정석] 오버라이딩"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 오버라이딩이란?

---

조상 클래스로부터 상속받은 메서드의 내용을 변경하는 것을 오버라이딩(overriding)이라 한다.

### 오버라이딩의 조건

자손 클래스에서 오버라이딩하는 메서드와 조상 클래스의 메서드의 

- 이름이 같아야 한다.
- 매개변수가 같아야 한다.
- 반환타입이 같아야 한다.
- 접근 제어자는 조상 클래스의 메서드보다 좁은 범위로 변경할 수 없다.
- 조상 클래스의 메서브보다 많은 수의 예외를 선언할 수 없다.
- 인스턴스 메서드를 static 메서드로 또는 그 반대로 변경할 수 없다.

오버라이딩의 예로 2차원 좌표계에 점을 표현하기 위한 Point 클래스와 Point클래스를 상속받은 Point3D클래스가 있다고 하자.

```java
class Point {
			int x;
			int y;
			String getLocation() {
					return "x : " + x + ", y : " + y;
			}
}

class Point3D extends Point {
			int z;
			String getLocation() {
					return "x : " + x + ", y : " + y + ", z: " + z;
			}
}
```

이 두 클래스는 서로 상속관계를 가지고있어 Point3D 클래스는 Point클래스의 `getLocation()`을 상속받아 사용할 수 있지만 3차원 좌표계의 한 점을 표현하기 위한 클래스 이므로 조상 클래스의 `getLocation()`의 로직에 맞지 않는다.
따라서 Point3D클래스에서 getLocation()을 자신에 맞게 z축에 좌표값도 포함하여 반환하도록 오버라이딩 한것이다. 이렇게 하여 새로운 메서드를 작성하는 것보다는 오버라이딩하여 코드를 구성할 수 있다.

## super

---

super는 자손 클래스에서 조상 클래스로부터 상속받은 멤버를 참조하는데 사용되는 참조변수이다.
조상 클래스로부터 상속받은 멤버도 자손 클래스 자신의 멤버이므로 super 대신 this를 사용할 수 있다. 그래도 조상 클래스의 멤버와 자손 클래스의 멤버가 중복 정의되어 서로 구별해야하는 경우에만 super를 사용하는 것이 좋다.

ch7/SuperTest.java

```java
class SuperTest {
	public static void main(String args[]) {
		Child c = new Child();
		c.method();
	}
}

class Parent {
	int x=20;
}

class Child extends Parent {
	void method() {
		System.out.println("x=" + x);
		System.out.println("this.x=" + this.x);
		System.out.println("super.x="+ super.x);
	}
}
```

```java
//실행결과
x = 20
this.x = 20
super.x = 10
```

이처럼 조상 클래스에 선언된 멤버변수와 같은 이름의 멤버변수를 자손 클래스에서 중복해서 정의하는것이 가능하며 참조변수 super를 이용해서 구별할 수 있다.

## super() - 조상 클래스의 생성자

---

this()와 마찬가지로 `super()` 역시 생성자이다. this()는 같은 클래스의 다른 생성자를 호출하는 데 사용되지만, `super()`는 조상 클래스의 생성자를 호출하는데 사용된다.

### 생성자의 첫 줄에서 조상 클래스의 생성자를 호출해야 하는 이유는?

자손 클래스의 멤버가 조상 클래스의 멤버를 사용할 수도 있으므로 조상의 멤버들이 먼저 초기화되어 있어야 하기 때문이다.

```java
class PointTest {
	public static void main(String argsp[]) {
		Point3D p3 = new Point3D();
		System.out.println("p3.x=" + p3.x);
		System.out.println("p3.y=" + p3.y);
		System.out.println("p3.z=" + p3.z);
	}
}

class Point {
	int x=10;	
	int y=20;

	Point(int x, int y) {
		//컴파일러는 super()를 한다. 여기서 super()는 Object의 생성자를 말한다. 
		this.x = x;
		this.y = y;
	}
}

class Point3D extends Point {
	int z=30;

	Point3D() {
		this(100, 200, 300);	// Point3D(int x, int y, int z)¸Ś ČŁĂâÇŃ´Ů.
	}

	Point3D(int x, int y, int z) {
		super(x, y);			// Point(int x, int y)¸Ś ČŁĂâÇŃ´Ů.
		this.z = z;
	}
}
```

컴파일러는 다음과 같이 자동적으로 `super()`를 Point클래스에 넣어준다.
위의 예제에서 `Point3D p3 = new Point3D();`를 실행하면 다음과같은 순서로 생성자가 호출된다.

`Point3D()` → `Point3D(int x, int y, int z)` → `Point(int x, int y)` → `Object()`

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>