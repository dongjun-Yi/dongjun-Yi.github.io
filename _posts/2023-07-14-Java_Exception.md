---
title: "[자바의정석] 예외처리"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 프로그램 오류

---

프로그램이 실행 중 어떤 원인에 의해서 오작동을 하거나 비정상적으로 종료되는 경우가 있다. 이러한 결과를 초래하는 원인을 프로그램 에러 또는 오류라고 한다. 이를 발생 시점에 따라 컴파일 에러와 런타임 에러로 나뉜다.

- 컴파일 에러 : 컴파일 할 때 발생하는 에러
- 런타임 에러 : 실행 시 발생하는 에러
- 논리적 에러 : 실행은 되지만, 의도와 다르게 동작하는 것.

컴파일 에러는 프로그램 실행 전에 오류를 검사해줘서 걸러줄 수 는 있지만, 런타임 에러는 프로그램 실행 중에 잠재적인 오류까지 검사할 수 는 없다. 따라서 자바에서는 런타임 에러를 방지하기 위해 실행 시 발생할 수 있는 프로그램 오류를 에러와 예외 두가지로 구분한다.

에러는 메모리 부족이나 스택 오버플로우 같은 복구할 수 없는 심각한 오류를 말하고, 예외는 발생하더라도 수습될 수 있는 상황을 말한다. 따라서 예외는 발생하더라고 프로그래머가 적절한 코드를 작성해  프로그램의  비정상적인 종료를 막을 수 있다.

## 예외 클래스의 계층 구조

---

자바에서는 실행 시 발생할 수 있는 오류를 클래스로 정의하였다. Exception과 Error클래스의 조상 Object클래스로 이루져 있는 구조다.

![Untitled.png](/assets/images/Java_Exception/Untitled.png)

모든 예외의 최고 조상은 Exception클래스이며, 상슥계층도를 Exception클래스로부터 도식화하면 다음과 같다.

![Untitled.png](/assets/images/Java_Exception/1.png)

위의 사진에서 볼 수 잇듯이 예외 클래스는 Exception클래스와 그 자손들 그룹과 RuntimeException클래스와 그 자손들로 나눠진다.

RuntimeException들은 주로 프로그래머의 실수에 의해서 발생될 수 있는 예외들로 예를 들면, 배열의 범위를 번어난 ArrayIndexOutOfBoundsException, 값이 null인 참조변수의 멤버를 호출한 NullPointerException 등이 발생한다.
Exception클래스들은 주로 외부의 영향으로 발생할 수 있는 것들로서, 프로그램의 사용자들의 동작에 의해서 발행하는 경우가 많다. 예를 들면 존재하지 않는 파일의 이름을 입력했다던가(FileNotFoundException),실수로 클래스의 이름을 잘못 적었다던가(ClassNotFoundException)인 경우에 발생한다.

## 예외처리하기 try-catch문

---

예외처리(error handling)란, 프로그램 실행 시 발생할 수 있는 예기치 못한 예외의 발생에 대비한 코드를 작성하는 것이며, 예외처리의 목적은 예외의 발생으로 인한 실행중인 프로그램의 갑작스런 비정상 종료를 막고, 정상적인 실행상태를 유지할 수 있도록 하는 것이다.

예외를 처리하기 위한 try-catch문의 구조는 다음과 같다.

```java
class ExceptionEx1 {
	public static void main(String[] args) 
   {
		try  {
			try	{	} catch (Exception e)	{ }
		} catch (Exception e)	{
			try	{	} catch (Exception e) { }	// 에러. 변수 e가 중복 선언되었다.
		} // try-catch의 끝

		try  {

		} catch (Exception e)	{

		} // try-catch의 끝
	}	// main메서드의 끝
}
```

catch블럭 내의 코드에서도 예외가 발생할 수 있기 때문에 try-catch문에 또 다른 try-catch문을 사용할 수 있다. 여기서 try-catch문에 또 다른 try-catch문을 사용할 경우 같은 이름의 참조변수를 사용하면 참조변수의 영역이 서로 겹치므로 다른 이름으로 사용해야 한다.

ch8/Exception2.java

```java
class ExceptionEx2 {
	public static void main(String args[]) {
		int number = 100;
		int result = 0;

		for(int i=0; i < 10; i++) {
			result = number / (int)(Math.random() * 10);
			System.out.println(result);
		}
	} // main의 끝
}
```

```java
//실행결과
20
100
java.lang.AritihimaticExcetpion : / by zero
		at ExceptionEx2.main (ExceptionEx2.java : 7)
```

위의 예제는 100을 0~9사이의 랜덤수로 나눈 결과를 출력하는 일을 10번한다. random()을 사용하여 매번 실행할 때마다 결과가 달라지겠지만, 대부분 10번이 출력되기 전에 예외가 발생하여 프로그램이 비정상적으로 종료될 것이다.
위의 결과는 ArithmeticException이 발생하였고, 이 오류는 산술과정에서 오류가 있을 때 발생하는 예외이다. 정수는 0으로 나누는 것이 금지 되었기 때문에 발생한 것이다.

이 오류를 try-catch문으로 예외가 발생하지 않게 코드를 아래와 같이 구성할 수 있다.

```java
class ExceptionEx3 {
	public static void main(String args[]) {
		int number = 100;
		int result = 0;

		for(int i=0; i < 10; i++) {
			try {
				result = number / (int)(Math.random() * 10);
				System.out.println(result);
			} catch (ArithmeticException e)	{
				System.out.println("0");	
			} 
		}
	} 
}
```

이렇게 작성하면 오류가 발생해도 catch구문에서 오류를 잡아주기 때문에 프로그램이 오류나지 않고 정상적으로 실행되게 된다.

## 예외의 발생과 catch블럭

---

catch블럭은 ()와 {}로 구성되는데 괄호 내에는 처리하고자 하는 예외와 같은 타입의 참조변수 하나를 선언해야 한다.
예외가 발생하면 동작 순서는 다음과 같다.

1. 발생한 예외에 해당하는 클래스의 인스턴스가 만들어진다.
2. 예외가 발생한 문장이 try블럭에 포함되어 있다면, 이 예외를 처리할 수 있는 catch블럭 있는지 찾는다.
3. catch블럭을 찾으면서 catch블럭의 괄호()내에 선언된 참조변수의 종류와 생성된 예외 클래스의 인스턴스에 instanceof연산자를 이용해서 검사하게 되는데, 검사결과가 true인 catch블럭을 만날때까지 검사는 계속된다.
4. 검사결과가 true인 catch블럭을 찾게 되면, 블럭에 있는 문장들을 모두 수행한 후에 try-catch문을 빠져나가고 예외는 처리되지만, 검사결과가 true인 catch블럭이 하나도 없으면 예외는 처리되지 않는다.

예제를 통해 살펴보자.

```java
class ExceptionEx7 {
	public static void main(String args[]) {
		System.out.println(1);			
		System.out.println(2);
		try {
			System.out.println(3);
			System.out.println(0/0);
			System.out.println(4); 		// 실행되지 않는다.
		} catch (ArithmeticException ae)	{
			if (ae instanceof ArithmeticException) 
				System.out.println("true");	
			System.out.println("ArithmeticException");
		} catch (Exception e)	{
			System.out.println("Exception");
		}	// try-catch의 끝
		System.out.println(6);
	}	// main메서드의 끝
}
```

try블럭에서 ArithmeticException이 발생해서 catch블럭을 하나씩 차례로 검사하게 되는데, 첫 번째 검사에서 일치하는 catch블럭을 찾았기 때문에 두 번째 catch블럭은 검사하지 않는다.

## 예외 발생시키기

---

`throw` 키워드를 사용해 프로그래머가 고의로 예외로 발생시킬 수 있으며, 방법은 아래와 같다.

1. 먼저 연산자 `new`를 이용하여 발생시키려는 예외 클래스의 객체를 만든다.

```java
Exception e = new Exception("고의로 발생시켰음");
```

1. 키워드 `throw`를 이용해 예외를 발생시킨다.

```java
throw e;
```

ch8/ExceptionEx9.java

```java
class ExceptionEx9 {
	public static void main(String args[]) {
		try {
			Exception e = new Exception("고의로 발생시켰음.");
			throw e;	 // 예외를 발생시킴
		//  throw new Exception("고의로 발생시켰음.");  

		} catch (Exception e)	{
			System.out.println("에러 메시지 : " + e.getMessage());
		     e.printStackTrace();
		}
		System.out.println("프로그램이 정상 종료되었음.");
	}
}
```

Exception 인스턴스를 생성할 때, 생성자에 String을 넣어 주면, 이 String이 Exception 인스턴스에 메세지로 저장된더. 이 메세지는 `getMessage()`로 얻을 수 있다.

## 메서드에 예외 선언하기

---

메서드에 예외를 선언하려면, 메서드의 선언부에 키워드 `throws`를 사용해서 메서드 내에서 발생할 수 있는 예외를 적어주기만 하면 된다.

```java
void method() throws Exception1, Exception2 .. ExceptionN {
		...
}
```

이렇게 예외를 선언하면, 이 예외뿐만 아니라 그 자손타입의 예외까지도 발생할 수 있다는 점에 주의해야 한다.
메서드 선언부에 예외를 선언하면 메서드를 사용하려는 사람이 메서드의 선언부를 봤을 때, 이 메서드를 사용하기 위해서는 어떠한 예외들이 처리되어져야 하는지 쉽게 알 수 있다!

다음 예제를 보면서 throws를 이해해보자.

ch8/ExceptionEx12.java

```java
class ExceptionEx12 {
	public static void main(String[] args) throws Exception {
		method1();	 // 같은 클래스내의 static멤버이므로 객체생성없이 직접 호출가능.
  	}	// main메서드의 끝

	static void method1() throws Exception {
		method2();
	}	// method1의 끝

	static void method2() throws Exception {
		throw new Exception();
	}	// method2의 끝
}
```

```java
//실행결과
Exception in thread "main" java.lang.Exception
	at ExceptionEx12.method2(ExceptionEx12.java:11)
	at ExceptionEx12.method1(ExceptionEx12.java:7)
	at ExceptionEx12.main(ExceptionEx12.java:3)
```

위의 예제를 보았듯이 사실 예외를 메서드의 throws에 명시하는 것은 예외를 처리하는 것이 아니라, 자신(예외가 발생할 가능성이 있는 메서드)을 호출한 메서드에게 예외를 전달하여 예외처리를 떠맡기는 것이다.

따라서 위의 결과로부터 호출스택을 보면 다음과 같이 정리할 수 있다.

1. 예외가 발생했을 때, 모두 3개의 메서드가 호출스택에 있었다.
2. 예외가 발생한 곳은 제일 윗줄에 있는 method2()라는 것과
3. main메서드가 method1()을, 그리고 method1()은 method2()를 호출했다는 것을 알 수 있다.

> 이처럼 예외가 발생한 메서드에게서 예외처리를 하지 않고 자신을 호출한 메서드에게 예외를 넘겨줄 수 있지만, 이것으로 예외가 처리된 것이 아니고 예외를 단순히 전달만 한다.
> 

## finally 블럭

---

finally블럭은 예외의 발생여부에 상관 없이 실행되어야할 코드를 포함시킬 목적으로 사용된다. try-catch문의 끝에 덧붙여 사용할 수 있으며, try-catch-finally의 순서로 구성된다.

```java
try {
		//예외가 발생할 가능성이 있는 문장들을 넣는다.
} catch(Exception e) {
		//예외 처리를 위한 문장을 넣는다.
} finally {
		//예외의 발생여부에 관계없이 항상 수행되어야하는 문장들을 넣는다.
		//finally블럭은 try-catch문의 맨 마지막에 위치해야 한다.
}
```

## 사용자 정의 예외 만들기

---

기존에 정의된 예외 클래스 외에 필요에 따라 프로그래머가 새로운 예외 클래스를 정의하여 사용할 수 있다.

```java
class MyException extends Exception { 
			MyException(Stringm msg) {
					super(msg);
			}
}
```

위와 같이 사용자가 원하는대로 예외 클래스를 정의하여 사용할 수 있다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>