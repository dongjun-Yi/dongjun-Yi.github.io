---
title: "[Design Pattern] 데코레이터 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
데코레이터 패턴은 **기본 기능에** **추가할 수 있는 기능의 종류가 많은 경우**에 각 추가 기능을 Decorator 클래스로 정의한 후 필요한 Decorator 객체를 조합함으로써 **추가 기능의 조합을 설계**하는 방식

데코레이터 패턴을 이해하기 위해 예를 들어보자

네비게이션에 도로를 표시하는 기능을 생각해보자. 여기서 **기본 기능**은 도로를 간단한 선으로 표시하는 것이고, **추가적으로** 차선을 표시하는 기능이 있다고 하자.

따라서 필요한 클래스는 

- RoadDisplay : 기본 도로 표시 기능을 제공하는 클래스
- RoadDisplayWithLane : 기본 도로 표시에 추가적으로 차선을 표시하는 클래스

RoadDisplay

```java
public class RoadDisplay { // 기본 도로 표시 클래스
	public void draw() {
		System.out.println("도로 기본 표시") ;
	}
}
```

RoadDisplayWithLane

```java
public class RoadDisplayWithLane extends RoadDisplay { // 기본 도로 표시 + 차선 표시 클래스
    public void draw() {
        super.draw(); // 상위 클래스 즉 RoadDisplay의 draw 메서드를 호출해서 기본 도로를 표시
        drawLane();
    }
    private void drawLane() {
        System.out.println("차선 표시") ;
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        RoadDisplay road = new RoadDisplay() ;
        road.draw() ; // 기본 도로만 표시
        RoadDisplay roadWithLane = new RoadDisplayWithLane() ;
        roadWithLane.draw() ; // 기본 도로 + 차선 표시
    }
}
```

But, 1. 만약 추가적으로 도로표시 기능을 추가하고싶다면?

  2. 그리고 추가적으로 여러가지 추가 기능을 조합하여 추가하고싶다면?

먼저 1번의 요구사항을 해결하기 위해서는 RoadDisplay를 상속하여 클래스를 생성하면 된다.

RoadDisplayWithTraffic

```java
public class RoadDisplayWithTraffic extends RoadDisplay {
    public void draw() {
        super.draw();
        drawTraffic();
    }
    private void drawTraffic() {
        System.out.println("교통량 표시") ;
    }
}
```

문제점 1번의 요구사항은 클래스를 추가하면 문제가 되지 않지만 문제점 2번을 만족하려면 저 각각의 조합마다 클래스를 추가해야 한다. 즉, 이들을 조합하면 많은 수 의 클래스가 설계되어 문제가 된다.

이를 해결하기 위해서는 각 추가 기능별로 개별작인 클래스를 설계하고 기능을 조합할 때 각 클래스의 객체 조합을 이용하면 된다.

→ **기본기능을 제공하는 클래스와 추가기능을 제공하는 인터페이스를 만들어 기본기능과 추가기능 클래스를 분리한다.**

클래스 다이어그램의 형태는 다음과 같다.

![Untitled.png](/assets/images/Decorator Pattern/Untitled.png)

- 여기서 Display 인터페이스와 이를 상속받은 DisplayDecorator 간의 연관관계를 맺은 이유는 기본 기능을 제공하는 draw()를 사용하기 위해 상속관계가 아닌 기본기능과 추가기능 간의 연관관계로 관계를 맺은 것이다.

Display

```java
public abstract class Display {
    public abstract void draw() ;
}
```

RoadDisplay

```java
public class RoadDisplay extends Display { // 기본 도로 표시 클래스
    public void draw() {
        System.out.println("도로 기본 표시") ;
    }
}
```

DisplayDecorator

```java
// 다양한 추가 기능에 대한 공통 클래스
public class DisplayDecorator extends Display {
    private Display decoratedDisplay ;
    public DisplayDecorator(Display decoratedDisplay) {
        this.decoratedDisplay = decoratedDisplay ;
    }
    public void draw() {
        decoratedDisplay.draw() ;
    }
}
```

LaneDecorator

```java
public class LaneDecorator extends DisplayDecorator { // 차선표시를 축하는 클래스
    public LaneDecorator(Display decoratedDisplay) { // 기존 표시 클래스의 설정
        super(decoratedDisplay);
    }
    public void draw() {
        super.draw(); // 설정된 기존 표시 기능을 수행
        drawLane() ; // 추가적으로 차선을 표시
    }
    private void drawLane() { System.out.println("\t차선 표시") ; }
}
```

TrafficDecorator

```java
public class TrafficDecorator extends DisplayDecorator { // 교통량 표시를 추가하는 클래스
    public TrafficDecorator(Display decoratedDisplay) { // 기존 표시 클래스의 설정
        super(decoratedDisplay);
    }
    public void draw() {
        super.draw(); // 설정된 기존 표시 기능을 수행
        drawTraffic() ; // 추가적으로 교통량을 표시
    }
    private void drawTraffic() { System.out.println("\t교통량 표시") ; }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        Display road = new RoadDisplay();
        road.draw(); // 기본 도로 표시
        Display roadWithLane = new LaneDecorator(new RoadDisplay());
        roadWithLane.draw(); // 기본 도로 표시 + 차선 표시
        Display roadWithTraffic = new TrafficDecorator(new RoadDisplay());
        roadWithTraffic.draw(); // 기본 도로 표시 + 교통량 표시
    }
}
```

Decorator Pattern

![Untitled.png](/assets/images/Decorator Pattern/Untitled 1.png)

- **Component : 기본 기능을 뜻하는 ConcreteComponent와 추가 기능을 뜻하는 Decorator의 공통 기능을 정의**
- **ConcreteComponent : 기본 기능을 구현하는 클래스**
- **Decorator : 많은 수가 존재하는 구체적인 Decorator의 공통 기능을 제공**
- **ConcreteDecorcator : Decorator의 하위 클래스로 기본 기능에 추가되는 개별적인 기능을 뜻함.**

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>