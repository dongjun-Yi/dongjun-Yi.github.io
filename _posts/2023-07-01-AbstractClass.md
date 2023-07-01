---
title: "[자바의 정석] 추상클래스"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 추상클래스란?

---

클래스를 설계도에 비유한다면, **추상클래스는 미완성 설계도**에 비유할 수 있다. 즉, **미완성 메서드(추상메서드)를 포함하고 있는 클래스**라는 의미이다.

```java
abstract class 클래스이름{}
```

## 추상메서드(abstract method)

---

메서드의 선언부만 작성하고 구현부는 작성하지 않은 채로 남겨 둔 것이 추상메서드이다. 즉, 설계만 해놓고 실제 수행될 내용은 작성하지 않았기 때문에 미완성 메서드인 것이다.
왜 그러면 메서드를 이와 같이 미완성 상태로 남겨놓았을까? 그 이유는 **메서드 내용이 상속받는 클래스에 따라 달라질 수 있기 때문에** 조상 클래스에서는 선언부만 작성하고, 실제 내용은 상속받는 클래스에서 구현하도록 비워 두는 것이다.

```java
abstract class Player { 
			abstract void play(int pos);
			abstract void stop();
}

class AudioPlayer extends Player {
			void play(int pos) { }
			void stop() {}
}

abstract class AbstractPlayer extends Player {
			void play(int pos){}
}
```

## 추상메서드로 선언하는 이유

---

예를 들어 Player 추상클래스가 있다고 가정해보자.

```java
abstract class Player {
		boolean pause;
		int currentPos;
	
		Player() {
				pause = 0;
				currentPos = 0;
		}

		abstract void play(int pos);
		abstract void stop();
		
		void play() {
				play(currentPos); //추상메서드를 사용할 수 있다.
		}
```

사실 이 클래스는 추상클래스가 아닌 일반 클래스로 작성하여 abstract 메서드에는 아무내용 없는 메서드로 작성하면 된다. 근데 왜 굳이 abstract를 붙여서 추상 클래스를 사용하는걸까?

그 이유는 **자손 클래스에서 추상메서드를 반드시 구현**하도록 강요하기 위해서이다.

만일 추상메서드로 정의되어 있지 않고 위와 같이 빈 몸통만 가지도록 정의되어 있다면, 상속받는 자손 클래스에서는 이 메서드들이 온전히 구현된 것으로 인식하고 오버라이딩을 통해 자신의 클래스에 맞도록 구현하지 않을 수도 있기 때문이다! 그래서 추상메서드로 정의해놓으면, 자손 클래스를 작성할 때 이들이 추상메서드이므로 내용을 구현해주어야 한다는 사실을 인식하고 자신의 클래스에 알맞게 구현할 것이다.

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>