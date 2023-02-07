---
title: "[Design Pattern] 스트래티지 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**스트래티지 패턴은 전략을 쉽게 바꿀 수 있도록 해주는 디자인 패턴이다.  여기에서 전략이란 문제를 해결하는 알고리즘으로 이해할 수 있다.**
- 같은 문제를 해결하는 여러 알고리즘이 클래스 별로 캡슐화 되어 있고 이들이 필요할 때 교체할 수 있도록 함으로써 동일한 문제를 다른 알고리즘으로 해결할 수 있게 하는 디자인 패턴

Robot 클래스로 예를 들어 보자. 로봇은 아톰과 태권V가 있고, 이 두 로봇은 공격 기능과 이동 기능이 있다. 아톰은 공격할 때 주먹만 사용하지만 하늘을 날 수가 있고 태권V는 미사일로 공격할 수는 있지만 날아다니지 못하고 걷기만 할 수 있다.

**클래스 다이어그램**

![Untitled1.png](/assets/images/Strategy Pattern/Untitled.png)

**Robot**

```java
public abstract class Robot {
    private String name;

    public Robot(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }
		
		public abstract void attack();
		public abstract void move();
}
```

**TaekwonV**

```java
public class TaekwonV extends Robot{
 
    public TaekwonV(String name) {
        super(name);
    }

    @Override
    public void attack() {
        System.out.println("I have Missile and can attack with it.");
    }

    @Override
    public void move() {
        System.out.println("I can only walk.");
    }
}
```

**Atom**

```java
public class Atom extends Robot{
    public Atom(String name) {
        super(name);
    }

    @Override
    public void attack() {
        System.out.println("I have strong punch and can attack with it.");
    }

    @Override
    public void move() {
        System.out.println("I can fly");
    }
}
```

**Main**

```java
public class Main {
    public static void main(String[] args) {
        Robot r1 = new TaekwonV("taekwonV");
        Robot r2 = new Atom("atom");
				
				r1.move();
				r1.attack();

				r2.move();
				r2.attack();
    }
}
```

TaekwonV와 Atom 클래스는 추상클래스를 상속하여 구현하여 공격과 이동 기능이 있는 로봇을 나타나게 하였다. 아톰과 태권V의 이동 기능과 공격 기능이 서로 다르기 때문에 Robot 클래스에서 attack과 move 메소드를 추상메소드로 설정해 자식클래스에서 각각 정의하도록 하였다.

### But,

만약 아톰이 날수 없고 오직 걷게만 만들고 싶다면 atom 클래스에서 move메소드를 수정해야한다.

이는 새로운 기능으로 변경하려고 하면 기존 코드의 내용을 수정해야 해서  OCP(Open Closed Principle)에 위배된다.

→ 만약 걷는 방식에 문제가 있거나 새로운 방식으로 수정하려면 모든 중복된 코드를 일관성 있게 변경해야만 한다.

### 해결책

이 예제에서 변화되면서 문제를 발생시키는 요인은 로봇의 **이동 방식과 공격 방식의 변화**다. 

즉, 새로운 방식의 이동 및 공격 기능이 계속해서 추가될  수 있으므로 기존의 로봇이나 새로운 로봇이 이러한 기능을 별다른 코드 변경 없이 제공받거나 기존의 공격이나 이동 방식을 다른 공격이나 이동 방식으로 쉽게 변경할 수 있어야한다.

→ **무엇이 변화되는지를 찾은 후에 이를 클래스로 캡슐화 한다**.

캡슐화 하기 위해서는 외부에서 구체적인 이동 방식과 공격 방식을 담은 구체적인 클래스들을 은닉해야 한다. 이를 위해 공격과 이동을 위한 **인터페이스를 각각 만들고 이들을 실제 실현한 클래스를 만들어야 한다.**

![Untitled1.png](/assets/images/Strategy Pattern/Untitled 1.png)

**개선된 클래스 다이어그램**

![Untitled1.png](/assets/images/Strategy Pattern/Untitled 2.png)

Robot

```java
public abstract class Robot {
    private String name;
    private MovingStrategy movingStrategy;
    private AttackStrategy attackStrategy;

    public void setMovingStrategy(MovingStrategy movingStrategy) {
        this.movingStrategy = movingStrategy;
    }

    public void setAttackStrategy(AttackStrategy attackStrategy) {
        this.attackStrategy = attackStrategy;
    }

    public void move(){
        this.movingStrategy.move();
    }
    public void attack(){
        this.attackStrategy.attack();
    }
    public Robot(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

**MovingStrategy interface**

```java
public interface MovingStrategy {
    public void move();
}
```

```java
public class FlyingStrategy  implements MovingStrategy{
    @Override
    public void move() {
        System.out.println("can fly");
    }
}
```

```java
public class WalkingStrategy implements MovingStrategy{
    @Override
    public void move() {
        System.out.println("can only walk");
    }
}
```

**AttackStrategy interface**

```java
public interface AttackStrategy {
    public void attack();
}
```

```java
public class MissileStrategy implements AttackStrategy{
    @Override
    public void attack() {
        System.out.println("can bomb");
    }
}
```

```java
public class PunchStrategy implements AttackStrategy{
    @Override
    public void attack() {
        System.out.println("Punch");
    }
}
```

**Main**

```java
public class Main {
    public static void main(String[] args) {
        Robot r1 = new TaekwonV("taekwonV");
        Robot r2 = new TaekwonV("Atom");

        r1.setAttackStrategy(new MissileStrategy());
        r1.setMovingStrategy(new FlyingStrategy());
        r1.move();
        r1.attack();

        r2.setMovingStrategy(new WalkingStrategy());
        r2.setAttackStrategy(new PunchStrategy());
        r2.move();
        r2.attack();
    }
}
```

위와 같이 strategy pattern으로 작성하면 이들 기능을 이용하는 로봇 객체와는 상관없이 향후 등장할 이동 방식과 공격 방식의 변화뿐만 아니라 현재 변화도 잘 처리할 수 있게 된다. 즉, **새로운 기능의 추가가 기존의 코드에 영향을 미치치 못하게 하므로 OCP를 만족하는 설계**가 된다.

또한 위와 같은 코드는 외부에서 로봇 객체의 이동 방식과 공경 방식을 임의대로 바꾸도록 해주는 메소드가 추가로 필요하게 된다. 이를 위해 Robot 클래스에 setMovingStrategy와 setAttackStrategy 메소드를 정의해 로봇의 이동 방식과 공격 방식이 필요할 때 바꿀 수 있도록 한다.

![Untitled1.png](/assets/images/Strategy Pattern/Untitled 3.png)

![Untitled1.png](/assets/images/Strategy Pattern/Untitled 4.png)

Strategy - Quicksort or Mergesort [algo change]

Command - Open or Close [action change]

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>