---
title: "[자바의 정석] 클래스와 객체"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 클래스와 객체

---

클래스는 객체의 설계도 또는 틀이라고 정의하며, 객체는 클래스에 정의된 내용대로 메모리에 생성된 것을 뜻한다.

## 객체와 인스턴스

---

객체와 인스턴스는 같은 의미이지만, 객체는 모든 인스턴스를 대표하는 포괄적인 의미를 갖고 있으며. 인스턴스는 어떤 클래스로부터 만들어진 것인지를 강조하는 보다 구체적인 의미를 갖고 있다.

```java
ex) 책상은 인스턴스다. -> 책상은 객체다.
		책상은 클래스의 객체이다 -> 책상은 클래스의 인스턴스이다.
```

## 객체의 구성요소 - 속성과 기능

---

객체는 속성과 기능의 집합

Tv의 속성과 기능을 예로 들어보자. Tv를 나타내는 속성으로는 크기, 길이, 높이, 색상 등이 있고 Tv의 기능에는 켜기/끄기, 볼륨 높이기/낮추기, 채널 변경하기 등이 있다.

이 속성과 기능은 프로그래밍으로는 변수와 메서드로 나타낼 수 있으며 Tv 클래스를 만들어보면 아래와 같다.

```java
class Tv {
		String color;
		boolean power;
		int channel;

		void power() { power != power;}
		void channelUp(); { channel++;}
		void channelDown(); { channel--;}
}
```

## 인스턴스의 생성과 사용

---

클래스를 선언한 것은 설계도를 작성한 것이고, 객체를 생성해야 사용할 수 있다.

```java
클래스명 변수명;
변수명 = new 클래스명();
```

ch6/TvTest.java

```java
class Tv { 
     // Tv의 속성(멤버변수) 
     String color;           	// 색상 
     boolean power;         	// 전원상태(on/off) 
     int channel;           	// 채널 

     // Tv의 기능(메서드) 
     void power()   { power = !power; }  // TV를 켜거나 끄는 기능을 하는 메서드  
     void channelUp()   {  ++channel; }  // TV의 채널을 높이는 기능을 하는 메서드 
     void channelDown() { --channel; }   // TV의 채널을 낮추는 기능을 하는 메서드  
}

class TvTest { 
      public static void main(String args[]) { 
            Tv t;                  // Tv인스턴스를 참조하기 위한 변수 t를 선언       
            t = new Tv();          // Tv인스턴스를 생성한다. 
            t.channel = 7;         // Tv인스턴스의 멤버변수 channel의 값을 7로 한다. 
            t.channelDown();       // Tv인스턴스의 메서드 channelDown()을 호출한다. 
            System.out.println("현재 채널은 " + t.channel + " 입니다."); 
      } 
}
```

### 인스턴스 생성 과정

1. `Tv t;`
    - Tv 클래스 타입의 참조변 수 t를 선언한다. 메모리에 참조변수 t를 위한 공간이 마련된다. 아직 인스턴스가 생성되지 않았으므로 참조변수로 아무것도 할 수 없다.
2. `t = new Tv();`
    - 연산자 new에 의해 Tv 클래스의 인스턴스가 메모리의 빈 공간에 생성 된다. 주소가 0x100인 곳에 생성되었다고 가정하자. 이때, 멤버 변수가 각 자료형에 해당하는 기본값으로 초기화 된다.
    - 이 후 =(대입연산자)에 의해 생성된 객체의 주소값이 참조변수 t에 저장된다. 이제는 참조변수 t를 통해 Tv인스턴스를 접근할 수 있다.
    
    ![Untitled.png](/assets/images/Java_Class_Object/Untitled.png)
    
3. `t.channel=7,  t.channelDown();`
    - `t.channel=7`은 참조변수 t에 저장된 주소에 있는 인스턴스의 멤버변수 channel에 7을 저장한다.
    - `t.channelDown()`은  참조변수 t가 참조하고 있는 Tv인스턴스의 channelDown()을 호출하여 멤버변수 channel을 감소시킨다.

### 인스턴스 공유

- 같은 클래스로부터 생성되도 각 인스턴스의 속성은 서로 다른 값을 유지할 수 있으며, 메서드의 내용은 모든 인스턴스에 대해 동일하다.

ch6/TvTest3.java

```java
class Tv { 
     // Tv의 속성(멤버변수) 
     String color;           // 색상 
     boolean power;          // 전원상태(on/off) 
     int channel;          	 // 채널 

     // Tv의 기능(메서드) 
     void power()   { power = !power; }  // TV를 켜거나 끄는 기능을 하는 메서드 
     void channelUp()   {  ++channel; }  // TV의 채널을 높이는 기능을 하는 메서드 
     void channelDown() {  --channel; }  // TV의 채널을 낮추는 기능을 하는 메서드  
}

class TvTest3 {
	public static void main(String args[]) {
		Tv t1 = new Tv();
		Tv t2 = new Tv();
		System.out.println("t1의 channel값은 " + t1.channel + "입니다.");
		System.out.println("t2의 channel값은 " + t2.channel + "입니다.");

		t2 = t1;		// t1이 저장하고 있는 값(주소)을 t2에 저장한다.
		t1.channel = 7;	// channel 값을 7로 한다.
		System.out.println("t1의 channel값을 7로 변경하였습니다.");

		System.out.println("t1의 channel값은 " + t1.channel + "입니다.");
		System.out.println("t2의 channel값은 " + t2.channel + "입니다.");
	}
}
```

이 예제에 실행과정을 그림으로 보면 다음과 같다.

![Untitled1.png](/assets/images/Java_Class_Object/1.png)
 
t1과 t2는 처음에 각각 다른 인스턴스의 주소를 가지고 있다가, t2=t2;을 실행하면 t2가 가지고있던 참조값은 잃어버리게 되고 t1에 저장되어 있던 값이 t2에 저장되게 된다. 그러면 t2와 t1은 동일한 인스턴스를 가르키게 된다.
위처럼 자바에서는 참조변수를 통해서 객체를 다른 변수와 공유할 수 있다.