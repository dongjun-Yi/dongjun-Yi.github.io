---
title: "[자바의 정석] 변수와 메서드"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 선언위치에 따른 변수의 종류

---

변수는 변수의 선언된 위치에 따라 3가지로 나뉜다.

- 클래스 변수
- 인스턴스 변수
- 지역변수

멤버변수를 제외한 나머지 변수들은 모두 지역변수이며, 멤버변수 중 static이 붙은 것은 클래스변수, 붙지 않은 것은 인스턴스 변수이다.

```java
class Variables{
		int iv;  //인스턴스 변수
		static int cv; //클래스 변수

		void method(){
				int lv=0; //지연 변수
		}
}
```

| 변수의 종류 | 선언위치 | 생성시기 |
| --- | --- | --- |
| 클래스 변수 | 클래스 영역 | 클래스가 메모리에 올라갈 때 |
| 인스턴스 변수 | 클래스 영역 | 인스턴스가 생성되었을 때 |
| 지역 변수 | 클래스 영역 외의 영역 | 변수 선언문이 수행되었을 때 |

## 클래스변수와 인스턴스변수

---

클래스변수와 인스턴스변수의 차이를 이해하기 위한 예로 카드 게임에 사용되는 카드를 클래스로 정의해보자.

```java
class Card {
	String kind ;				// 카드의 무늬 - 인스턴스 변수
	int number;				    // 카드의 숫자 - 인스턴스 변수
	static int width = 100;		// 카드의 폭  - 클래스 변수
	static int height = 250;	// 카드의 높이 - 클래스 변수
}
```

각 Card인스턴스는 자신만의 무늬와 숫자가 있어서 인스턴스 변수로 선언해야 하고, 각 카드의 폭과 높이는 모든 인스턴스가 공통적으로 같은 값을 유지해야 하므로 클래스 변수로 선언한것이다.

ch6/CardTest.java

```java
class CardTest{
	public static void main(String args[]) {
		System.out.println("Card.width = "  + Card.width);
		System.out.println("Card.height = " + Card.height);

		Card c1 = new Card();
		c1.kind = "Heart";
		c1.number = 7;

		Card c2 = new Card();
		c2.kind = "Spade";
		c2.number = 4;

		System.out.println("c1은 " + c1.kind + ", " + c1.number + "이며, 크기는 (" + c1.width + ", " + c1.height + ")" );
		System.out.println("c2는 " + c2.kind + ", " + c2.number + "이며, 크기는 (" + c2.width + ", " + c2.height + ")" );		

		System.out.println("c1의 width와 height를 각각 50, 80으로 변경합니다.");
		c1.width = 50;
		c1.height = 80;

		System.out.println("c1은 " + c1.kind + ", " + c1.number + "이며, 크기는 (" + c1.width + ", " + c1.height + ")" );
		System.out.println("c2는 " + c2.kind + ", " + c2.number + "이며, 크기는 (" + c2.width + ", " + c2.height + ")" );
	}
 }
```

위와 같이 Card.width, c1.width, c2.width 모두 같은 저장공간을 참조하므로 항상 같은 값을 갖게 된다.

> 클래스 변수를 사용할 때는 Card.width와 같이 ‘클래스이름.클래스변수’의 형태로 하는 것이 좋다. 참조변수 c1,c2를 통해서도 클래스변수를 사용할 수 있지만 이렇게 하면 클래스변수를 인스턴스변수로 오해하기 쉽기 때문이다.
> 

## 메서드

---

메서드는 크게 두 부분 선언부와 구현부로 이루어져 있다. 

```java
반환타입 메서드이름 (타입 변수명, 타입 변수명, ...){ //선언부
																					//구현부
}

int add(int a, int b) { //선언부
	int result = a+b ;    //구현부
	return result;			
}		
```

- 메서드 선언부는 메서드 이름, 매배변수 선언, 반환타입으로 구성되어 있다.
- 구현부에는 수행할 문장들을 넣으면 된다.
- 반환타입과 return할 변수의 타입은 같아야 하고, return 문은 저장된 변수 값을 호출한 메서드로 반환한다.

## JVM의 메모리 구조

---

응용 프로그램이 실행되면, JVM은 시스템으로부터 프로그램을 수행하는데 필요한 메모리를 할당받고

JVM은 이 메모리를 용도에 따라 여러 영역으로 나누어 관리한다. 그 중 3가지 주요 영역에 대해서 알아보자

![Untitled.png](/assets/images/Java_Variable_Method/Untitled.png)

JVM의 메모리 구조

1. Method Area
- 프로그램 실행 중 어떤 클래스가 사용되면, JVM은 해당 클래스의 클래스파일(.class)을 읽어서 분석하여 클래스에 대한 정보를 이곳에 저장한다. 이 때, 그 클래스의 클래스변수도 이 영역에 저장된다.
1. Heap
- 인스턴스가 생성되는 공간. 프로그램 실행 중 생성되는 인스턴스는 모두 이곳에 생성된다.
- 인스턴수의 변수들이 생성되는 공간이다.
1. 호출스택(Call stack 또는 execution stack)
- 호출스택은 메서드의 작업에 필요한 메모리 공간을 제공한다. 메서드가 호출되면, 호출스택에 호출된 메서드를 위한 메모리가 할당되며, 이 메모리는 메서드가 작업을 수행하는 동안 지역변수(매개변수 포함)들과 연산의 중간결과등을 저장하는데 사용된다. 그리고 메서드가 작업을 마치면 할당되었던 메모리 공간은 반환되어 비워진다.

호출스택을 예제로 살펴보자

```java
class CallStackTest {
	public static void main(String[] args) {
		firstMethod();
	}

	static void firstMethod() {
		secondMethod();
	}

	static void secondMethod() {
		System.out.println("secondMethod()");		
	}
}
```

위의 실행결과를 그림으로 살펴보면

![Untitled.png](/assets/images/Java_Variable_Method/1.png)

예제를 실행하면 JVM이 main메서드를 호출하여 먼저 main이 실행되고, main이 `firstMethod()`를 호출하여 (3)처럼 호출스택에 firstMethod가 위에 쌓여 있는것을 볼 수 있다. firstMethod가 `secondMethod()`를 호출하여 secondMethod()가 실행되고 `println`을 호출하여 화면에 출력한다. 출력한 후 `println()`은 호출스택에서 사라지고 `sceondMethod()`도 종료하여 호출스택에서 제거된다. `firstMethod()`도 더 이상 실행할 코드가 없어 호출스택에서 제거되고 main도 더 이상 수행할 코드가 없어 종료되어 호출스택은 비워지고 프로그램은 종료하게 된다. 

## 기본형 매개변수와 참조형 매개변수

---

메서드의 매개변수를 기본형으로 선언하면 단순히 저장된 값만 얻지만, 참조형으로 선언하면 값이 저장된 곳의 주소를 알 수 있기 때문에 값을 읽어 오는 것은 물론 값을 변경하는 것도 가능하다.

ch6/PrimitiveParamEx.java

```java
class Data { int x; }

class PrimitiveParamEx {
	public static void main(String[] args) {
		Data d = new Data();
		d.x = 10;
		System.out.println("main() : x = " + d.x);

		change(d.x);
		System.out.println("After change(d.x)");
		System.out.println("main() : x = " + d.x);
	}

	static void change(int x) {  // ±âº»Çü ¸Å°³º¯¼ö
		x = 1000;
		System.out.println("change() : x = " + x);
	}
}
```

```java
//실행결과
main() : x = 10
change() : x = 1000
After change(d.x)
main() : x = 10
```

위의 예제를 보면 change()에 매개변수로 넘겨준 x값을 1000을 대입했지만 대입한후 main함수에서 x의값을 출력하면 여전히 10이 출력되는 것을 볼 수 있다. 이처럼 기본형 매개변수는 변수에 저장된 값만 읽을 수만 있을 뿐 변경할 수 없다.

ch6/ReferenceParamEx.java

```java
class Data { int x; }

class ReferenceParamEx {
	public static void main(String[] args) {

		Data d = new Data();
		d.x = 10;
		System.out.println("main() : x = " + d.x);

		change(d);
		System.out.println("After change(d)");
		System.out.println("main() : x = " + d.x);

	}

	static void change(Data d) { // 참조형 매개변수
		d.x = 1000;
		System.out.println("change() : x = " + d.x);
	}
}
```

```java
//실행결과
main() : x = 10
change() : x = 1000
After change(d)
main() : x = 1000
```

이전 예제와 달리 change메서드를 호출한 후에 d.x의 값이 변경되었다. change메서드의 매개변수가 참조형이라서 값이 아니라 ‘값이 저장된 주소’를 change메서드에게 넘겨주었기 때문에 값을 읽어 오는것 뿐만 아니라 변경도 가능하다.

> 반환타입이 참조형이라는 것은 메서드가 ‘객체의 주소’를 반환한다는 것을 의미한다.
> 

## 클래스 메서드(Static 메서드)와 인스턴스 메서드

---

인스턴스 메서드는 인스턴스 변수와 관련된 작업을 하는 즉, **메서드의 작업을 수행하는데 인스턴스 변수를 필요로 하는 메서드**이다. 반면에 메서드 중에서 **인스턴스와 관계없는(인스턴스 변수나 인스턴스 메서드를 사용하지 않는) 메서드를 클래스 메서드(static 메서드)**로 정의한다.

- static변수는 인스턴스를 생성하지 않아도 사용할 수 있다.
    - static이 변수는 클래스가 메모리에 올라갈 때 이미 자동적으로 생성되기 때문이다.
- 클래스 메서드(static 메서드)는 인스턴스 변수를 사용할 수 없다.
    - 인스턴스 변수는 인스턴스가 반드시 존재해야만 사용할 수 있는데, 클래스 메서드는 인스턴스 생성 없이 호출 가능하므로 클래스 메서드가 호출되었을 때 인스턴스가 존재하지 않을 수도 있다.
    그래서 클래스 메서드에서 인스턴스 변수의 사용을 금지한다.
- **메서드 내에서 인스턴스 변수를 사용하지 않는다면, static을 붙이는 것을 고려한다.**
    - 메서드의 작업내영 중에서 인스턴스 변수를 필요로 한다면, static을 붙일 수 없다. 반대로 인스턴스변수를 필요로 하지 않는다면 static을 붙이자. **메서드 호출시간이 짧아지므로 성능이 향상된다.**

## 클래스 멤버와 인스턴스 멤버간의 참조와 호출

---

같은 클래스에 속한 멤버들 간에는 별도의 인스턴스를 생성하지 않고도 서로 참조 또는 호출이 가능하다. 단, 클래스멤버가 인스턴스 멤버를 참조 또는 호출하고자 하는 경우에는 인스턴스를 생성해야한다.
그 이유는 **인스턴스 멤버가 존재하는 시점에 클래스 멤버는 항상 존재하지만**, **클래스멤버가 존재하는 시점에 인스턴스 멤버가 존재하지 않을 수도 있기 때문**이다.

ch6/MemberCall.java

```java
class MemberCall {
	int iv = 10;
	static int cv = 20;

	int iv2 = cv;
//	static int cv2 = iv;		// 에러. 클래스변수는 인스턴스 변수를 사용할 수 없음.
	static int cv2 = new MemberCall().iv;	 // 이처럼 객체를 생성해야 사용가능.

	static void staticMethod1() {
		System.out.println(cv);
//		System.out.println(iv); // 에러. 클래스메서드에서 인스턴스변수를 사용불가.
		MemberCall c = new MemberCall();	
		System.out.println(c.iv);   // 객체를 생성한 후에야 인스턴스변수의 참조가능.
}

	void instanceMethod1() {
		System.out.println(cv);		
		System.out.println(iv); // 인스턴스메서드에서는 인스턴스변수를 바로 사용가능.
}

	static void staticMethod2() {
		staticMethod1();
//		instanceMethod1(); // 에러. 클래스메서드에서는 인스턴스메서드를 호출할 수 없음.
		MemberCall c = new MemberCall();
		c.instanceMethod1(); // 인스턴스를 생성한 후에야 호출할 수 있음.
 	}
	
	void instanceMethod2() {	// 인스턴스메서드에서는 인스턴스메서드와 클래스메서드
		staticMethod1();		//  모두 인스턴스 생성없이 바로 호출이 가능하다.
		instanceMethod1();
	}
}
```

위의 코드는 같은 클래스 내의 인스턴스 메서드와 static 메서드간의 호출에 대해서 설명하고 있다. 같은 클래스 내의 메서드는 서로 객체의 생성이나 참조변수 없이 직접 호출이 가능하지만 **static 메서드는 인스턴스 메서드를 호출할 수 없다.**

> 인스턴스 멤버는 반드시 객체를 생성한 후에만 참조 또는 호출이 가능하기 때문에 클래스멤버가 인스턴스멤버를 참조, 호출하기 위해서는 객체를 생성하여야 한다.
> 

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>