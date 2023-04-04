---
title: "[자바의 정석] 상속"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 상속이란?

---

상속이란, 기존의 클래스를 재사용하여 새로운 클래스를 작성하는 것이다. 

```java
class 자손클래스 extends 조상클래스{}
```

- 상속받을 클래스의 이름 뒤에 상속받고자 하는 클래스의 이름을 키워드 `extends` 를 함께 써주면 된다.
- 상속해주는 클래스를 “조상 클래스”, 상속 받는 클래스를 “자손 클래스”라고 한다.
- 자손 클래스는 조상 클래스의 모든 멤버를 상속 받는다.

Point와 Point3D가 있다고 해보자

```java
class Point{
			int x;
			int y
}

class Point3D{
			int x;
			int y;
			int z;
}
```

Point3D 클래스의 멤벼변수는 3개를 가지고 있고 Point는 멤버 변수 2개를 가지고 있는 상황에서, int x, int y의 코드가 중복되는 것을 볼 수 있다. 이때 상속관계를 이용하여 코드를 작성하면 훨씬 간결하게 구성할 수 있다.
**이처럼 클래스간의 상속관계를 맺어 주면 자손 클래스들의 공통적인 부분은 조상 클래스에서 관리되고 자손 클래스는 자신에 정의된 멤버들만 관리하면 되므로 각 클래스의 코드가 적어져서 관리가 쉬어진다.**

상속관계를 이용한 Point3D

```java
class Point3D extends Point{
			int z;
}
```

여기서 Point와 Point3D의 관계를 그림으로 나타내면 다음과 같다.

![Untitled.png](/assets/images/Java_Inheritance/Untitled.png)
자손 클래스는 조상 클래스의 모든 멤버를 상속 받으므로 항상 조상 클래스보다 같거나 많은 멤버를 갖는다. 즉, 상속에 상속을 거듭할수록 상속받는 클래스의 멤버 개수는 점점 늘어나게 된다.
그래서 상속을 받는다는 것은 조상 클래스를 확장(`extend`)한다는 의미로 해석할 수 있다.

 

> **- 생성자와 초기화 블럭은 상속되지 않는다. 멤버만 상속된다.
- 자손 클래스의 멤버 개수는 조상 클래스보다 항상 같거나 많다.**
> 

ch7/CaptionTvTest.java

```java
class Tv {
	boolean power; 	// 전원상태(on/off)
	int channel;	// 채널

	void power()        {   power = !power; }
	void channelUp()    { 	 ++channel;     }
	void channelDown()  {	 --channel;	    }
}

class CaptionTv extends Tv {
	boolean caption;		// 캡션상태(on/off)
	void displayCaption(String text) {
		if (caption) {	// 캡션 상태가 on(true)일 때만 text를 보여 준다.
			System.out.println(text);
		}
	}
}

class CaptionTvTest {
	public static void main(String args[]) {
		CaptionTv ctv = new CaptionTv();
		ctv.channel = 10;				// 조상 클래스로부터 상속받은 멤버
		ctv.channelUp();				// 조상 클래스로부터 상속받은 멤버
		System.out.println(ctv.channel);
		ctv.displayCaption("Hello, World");	
		ctv.caption = true;				    // 캡션기능을 켠다.
		ctv.displayCaption("Hello, World");	// 캡션을 화면에 보여 준다.
	}
}
```

자손 클래스의 인스턴스를 생성하면 조상 클래스의 멤버도 함께 생성되기 때문에 따로 조상 클래스의 인스턴스를 생성하지 않고도 조상 클래스의 멤버들을 사용할 수 있다.

> **자손 클래스의 인스턴스를 생성하면 조상 클래스의 멤버와 자손 클래스의 멤버가 합쳐진 하나의 인스턴스로 생성한다.**
> 

## 클래스간의 관계 설정하기(포함 OR 상속)

---

클래스를 작성하는데 “~은 이다” 와 “~은 ~을 가지고 있다”의 문자을 이용하여 클래스간의 관계가 포함관계인지 상속관계인지 정의하면 명확해진다.

ch7/DrawShape.java

```java
class DrawShape {
	public static void main(String[] args) {
		Point[] p = {   new Point(100, 100),
                        new Point(140,  50),
                        new Point(200, 100)
					};

		Triangle t = new Triangle(p);
		Circle   c = new Circle(new Point(150, 150), 50);

		t.draw(); // 삼각형을 그린다.
		c.draw(); // 원을 그린다.
	}
}

class Shape {
	String color = "black";
	void draw() {
		System.out.printf("[color=%s]%n", color);
	}
}

class Point {
	int x;
	int y;

	Point(int x, int y) {
		this.x = x;
		this.y = y;
	}

	Point() {
		this(0,0);
	}

	String getXY() {  
		return "("+x+","+y+")"; // x와 y의 값을 문자열로 반환
	}
}

class Circle extends Shape {
	Point center;	// 원의 원점좌표
	int r;			// 반지름

	Circle() {		
		this(new Point(0, 0), 100); // Circle(Point center, int r)를 호출
	}

	Circle(Point center, int r) {
		this.center = center;
		this.r = r;
	}

	void draw() { // 원을 그리는 대신에 원의 정보를 출력하도록 했다.
		System.out.printf("[center=(%d, %d), r=%d, color=%s]%n", center.x, center.y, r, color);
	}
}

class Triangle extends Shape {
	Point[] p = new Point[3];

	Triangle(Point[] p) {
		this.p = p;
	}

	void draw() { 
		System.out.printf("[p1=%s, p2=%s, p3=%s, color=%s]%n", p[0].getXY(), p[1].getXY(), p[2].getXY(), color);
	}
}
```

위의 예제에서 Circle클래스와 Point클래스를 보면 “원은 점이다.” 와 “원은 점을 가지고 있다.”을 보면 첫번째 문장보다 두번째 문장이 더 옳다는 것을 알 수있다. 이럴 때는 Circle클래스와 Point클래스의 관계는 포함관계를 맺어주어야 한다. 
또한 Shape클래스와 Circle클래스의 관계를 설정하는거를 보면 “원은 도형이다”가 맞기 때문에 Shape와 Circle클래스의 관계는 상속관계로 맺어주어야 한다.

> 상속관계 : “~은 이다.”(is-a)
포홤관계 : “~은 ~을 가지고 있다”(has-a)
> 

## 단일상속(Single inheritance)

---

자바에서는 단일 상속만을 허용한다.

다중상속을 허용하면 여러 클래스로부터 상속을 받을 수 있기 때문에 복합적인 기능을 가진 클래스를 쉽게 작성할 수 있다는 장점이 있지만, 클래스간의 관계가 매우 복잡해진다는 것과 서로 다른 클래스로부터 상속받은 멤버간의 이름이 같은 경우 구별할 수 있는 방법이 없다는 단점을 가지고 있다.

만일 아래 코드처럼 TVCR클래스가 TV클래스와 VCR클래스를 모두 조상으로 하여 두 클래스의 멤버들을 상속받는다고 가정하자.

```java
class TVCR extends TV, VCR{}
```

TV클래스와 VCR클래스에 power()라는 메서드가 있을 때, 자손인 TVCR클래스는 어느 조상 클래스의 power()를 받아야 되나?
만약 인스턴스 메서드의 경우 선언부가 같은 두 메서드를 구별할 수 있는 방법은 없다. 이를 해결하려면 조상 클래스의 메서드의 이름이나 매개변수를 바꾸는 방법 밖에 없다. 그러나, 이렇게 하면 조상 클래스의 power()메서드를 사용하는 모든 클래스들도 변경해야 하므로 그리 간단한 문제가 아니다.

**이 때문에 자바는 다중상속을 지원하지 않는다!!**

## Object 클래스 - 모든 클래스의 조상

---

Object클래스는 모든 클래스 상속계층도의 최상위에 있는 조상 클래스이다. 
다른 클래스로부터 상속 받지 않는 모든 클래스들은 자동적으로 Object클래스로부터 상속받게 함으로써 이것을 가능하게 한다.

만약 다음과 같은 Tv클래스가 있다고 가정하자.

```java
class Tv{}
```

위의 코드를 컴파일 하면 컴파일러는 위의 코드를 다음과 같이 자동적으로 `extends Object`를 추가하여 Tv클래스가 Object클래스로부터 상속받도록 한다.

```java
class Tv extends Object{}
```

이 때문에 toString()이나 equals()와 같은 메서드를 따로 정의하지 않고도 사용할 수 있었던 이유는 이 메서드들이 Object클래스에 정의된 것들이기 때문이다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>