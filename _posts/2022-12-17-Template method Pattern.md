---
title: 템플릿 메서드 패턴
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**객체의 연산에는 알고리즘의 뼈대만 정의하고 각 단계에서 수행할 구체적 처리는 서브클래스 쪽으로 미룬다. 알고리즘의 구조 자체는 그대로 놔둔 채 알고리즘 각 단계를 서브 클래스에서 재정의할 수 있게 해주는 패턴**  

템플릿 메소드 패턴이 어떻게 적용 되는지 알기 위해 엘레베이터 제어 시스템에서 모터를 구동시키는 기능을 예로 들어 보자

현재 모터를 이용하는 제어 시스템이 잇고 HyundaiMotor 클래스에 move 메서드를 정의할 수 있다.

- HyundaiMotor : 모터의 구동을 제어하여 엘레베이터를 이동시키는 기능
- Door : 문을 열거나 닫는 기능을 제공

**클래스 다이어그램**

![Untitled.png](/assets/images/Template Pattern/Untitled.png)

또한 엘레베이터의 이동방향(위, 아래)과 모터의 상태(정지, 이동 중), 문의 상태(닫힘, 열림)를 나태내주는 변수들이 필요하므로 이 변수들을 enum class에 따로 생성하게 되면 다음과 같다.

```java
public enum DoorStatus { CLOSED, OPENED }
public enum MotorStatus { MOVING, STOPPED}
public enum Direction {UP, DOWN};
```

이 예제에서 동작 순서를 설명하면

1. HyundaiMotor 클래스에 move() getMotorStatus()를 호출해 모터의 상태를 확인한다.
2. 만약 모터가 동작 중이면 move()는 return후 종료하게 된다.
3. Door 클래스에 getDoorStatus()를 호출해 문의 상태를 확인한다. 만약 문이 열려 있다면 Door 클래스에 close()를 호출해 문을 닫는다. 
4. moveHyundaiMotor()를 호출해 모터를 구동시키고, setMotorStatus()를 호출해 모터의 상태를 MOVING으로 바꾼다.

Door

```java
public class Door {
    private DoorStatus doorStatus ; 
    public Door() {
        doorStatus = DoorStatus.CLOSED ; 
    }
    public DoorStatus getDoorStatus() { 
        return doorStatus ;
    }
    public void close() {
        doorStatus = DoorStatus.CLOSED ; }
    public void open() {
        doorStatus = DoorStatus.OPENED ;
    } 
}
```

HyundaiMotor

```java
public class HyundaiMotor {
    private Door door;
    private MotorStatus motorStatus;

    public HyundaiMotor(Door door) {
        this.door = door;
        motorStatus = MotorStatus.STOPPED; // 초기에는 멈춘 상태 
    }

    private void moveHyundaiMotor(Direction direction) { // Hyundai Motor를 구동시킨다.
    }

    public MotorStatus getMotorStatus() {
        return motorStatus;
    }

    private void setMotorStatus(MotorStatus motorStatus) {
        this.motorStatus = motorStatus;
    }

    public void move(Direction direction) {
        MotorStatus motorStatus = getMotorStatus();
        if (motorStatus == MotorStatus.MOVING) return; // 이미 이동 중이면 아무 작업을 하지 않음
        DoorStatus doorStatus = door.getDoorStatus();
        if (doorStatus == DoorStatus.OPENED) door.close(); // 만약 문이 열려 있으면 먼저 문을 닫음
        moveHyundaiMotor(direction); // 모터를 주어진 방향으로 이동
        setMotorStatus(MotorStatus.MOVING); // 모터 상태를 이동 중으로 변경함 
    }
}
```

```java
public class Main{
	public static void main(String[] args) {
        Door door = new Door() ;
        HyundaiMotor hyundaiMotor = new HyundaiMotor(door) ; hyundaiMotor.move(Direction.UP) ;
    }
}
```

**But,** 

만약 hyundaiMotor말고 다른 회사의 모터를 사용하게 된다면?

LGMotor클래스를 만들어 다른 회사 모터를 사용하게 되면 다음 코드와 같다.

LGMotor

```java
public class LGMotor {
    private Door door ;
    private MotorStatus motorStatus ; public LGMotor(Door door) {
        this.door = door ; motorStatus = MotorStatus.STOPPED ; 
    }
    private void moveLGMotor(Direction direction) { // LG Motor를 구동시킴
    }
    public MotorStatus getMotorStatus() { return motorStatus; } 
    private void setMotorStatus(MotorStatus motorStatus) {
        this.motorStatus = motorStatus; 
    }
    public void move(Direction direction) {
        MotorStatus motorStatus = getMotorStatus() ;
        if ( motorStatus == MotorStatus.MOVING ) 
            return ;
        DoorStatus doorStatus = door.getDoorStatus() ;
        if ( doorStatus == DoorStatus.OPENED ) 
            door.close() ;
        moveLGMotor(direction) ; // move 메서드는 이 문장을 제외하면 HyundaiMotor와 동일함 setMotorStatus(MotorStatus.MOVING) ;
    } 
}
```

여기서 LGMotor 클래스와 HyndaiMotor 클래스를 비교해보면 여러 개의 메소드가 동일한 코드로 구성되어 두개의 클래스는 많은 중복 코드를 가져 문제가 생기게 된다.!

중복을 최소한으로 줄이기 위해 중복되는 부분을 추상화시켜 상속을 이용해 문제를 해결할 수 있다.

따라서 중복되는 부분의 코드를 따로 Moto라는 추상클래스로 나누게 되면 코드는 다음과 같다.

Motor

```java
public abstract class Motor { // HyundaiMotor와 LGMotor에 공통적인 기능을 구현하는 클래스 protected Door door ;
    private MotorStatus motorStatus ;
    public Motor(Door door) {
        this.door = door ;
        motorStatus = MotorStatus.STOPPED ;
    }
    public MotorStatus getMotorStatus() {
        return motorStatus; 
    }
    protected void setMotorStatus(MotorStatus motorStatus) { 
        this.motorStatus = motorStatus;
    } 
}
```

HyundaiMotor

```java
public class HyundaiMotor extends Motor { // Motor를 상속받아서 HyundaiMotor를 구현함
     public HyundaiMotor(Door door) {
        super(door) ;
    }
    private void moveHyundaiMotor(Direction direction) { // Hyundai Motor를 구동시킨다.
    }
    public void move(Direction direction) {
        MotorStatus motorStatus = getMotorStatus() ;
        if ( motorStatus == MotorStatus.MOVING )
            return ;
        DoorStatus doorStatus = door.getDoorStatus() ;
        if ( doorStatus == DoorStatus.OPENED )
            door.close() ;
        moveHyundaiMotor(direction) ; // move 메서드는 이 구문을 제외하면 LGMotor와 동일함
        setMotorStatus(MotorStatus.MOVING) ;
     }
}
```

LGMotor

```java
public class LGMotor extends Motor { 
    public LGMotor(Door door) {
        super(door) ;
    }
    private void moveLGMotor(Direction direction) { // LG Motor를 구동시킨다.
    }
    public void move(Direction direction) {
        MotorStatus motorStatus = getMotorStatus() ;
        if ( motorStatus == MotorStatus.MOVING ) 
            return ;
        DoorStatus doorStatus = door.getDoorStatus() ; 
        if ( doorStatus == DoorStatus.OPENED )
            door.close() ;
        moveLGMotor(direction) ; // move 메서드는 이 구문을 제외하면 HyundaiMotor와 동일함
        setMotorStatus(MotorStatus.MOVING) ; 
    }
}
```

이렇게 보면 두 코드가 중복되는게 없어 보이지만 HudaniMotor 클래스 move()와 LGMotor 클래스 move()의 로직을 보면 이 메소드도 대부분 구조가 비슷하여 코드가 중복되는것을 알 수 있다. 즉, move()에서 moveHyundaiMotor()와 moveLGMotor() 메소드 호출하는 구문을 제외하면 두 클래스의 move()는 동일하다. 따라서 move()를 상위 Motor클래스로 이동시키고 다른 구문, 즉, moveHyudaniMotor()와 moveLGMotor() 호출 부분을 하위 클래스에서 재정의하는 방식으로 코드를 수정해야 코드의 중복을 줄일 수 있게 된다.

**클래스 다이어그램**

![Untitled1.png](/assets/images/Template Pattern/Untitled 1.png)

Motor

```java
public abstract class Motor {
    private Door door;
    private MotorStatus motorStatus;

    public Motor(Door door) {
        this.door = door;
        motorStatus = MotorStatus.STOPPED;
    }

    public MotorStatus getMotorStatus() {
        return motorStatus;
    }

    private void setMotorStatus(MotorStatus motorStatus) {
        this.motorStatus = motorStatus;
    }

    public void move(Direction direction) { // LGMotor와 HyundaiMotor의 move에서 공통만을 가짐 MotorStatus motorStatus = getMotorStatus() ;
        if (motorStatus == MotorStatus.MOVING)
            return;
        DoorStatus doorStatus = door.getDoorStatus();
        if (doorStatus == DoorStatus.OPENED)
            door.close();
        moveMotor(direction); // 하위 클래스에서 override됨
        setMotorStatus(MotorStatus.MOVING);
    }

    protected abstract void moveMotor(Direction direction);
}
```

HyudaniMotor

```java
public class HyundaiMotor extends Motor { 
    public HyundaiMotor(Door door) {
        super(door); 
    }
    protected void moveMotor(Direction direction) { // Hyundai Motor를 구동시킨다.
    } 
}
```

LGMotor

```java
public class LGMotor extends Motor { 
		public LGMotor(Door door) {
			super(door); 
		}
		protected void moveMotor(Direction direction) { // LG Motor를 구동시킨다.
		} 
}
```

위와 같이 **전체적으로 동일하면서 부분적으로 다른 구문으로 구성된 메소드의 코드가 중복될때 사용되는** 디자인 패턴이 바로 **템플릿 메소드 패턴**이다.

- **템플릿 메소드 패턴은 전체적인 알고리즘을 구현하면서 상이한 부분은 하위클래스에서 구현할 수 있도록 해주는 디자인 패턴으로서 전체적인 알고리즘의 코드를 재사용하는데 유용하다.**

![Untitled2.png](/assets/images/Template Pattern/Untitled 2.png)

- AbstractClass : 템플릿 메소드를 정의하는 클래스. 하위 클래스에 공통 알고리즘을 정의하고 하위 클래스에서 구현될 기능을 primitive 메소드 또는 hook 메소드로 정의하는 클래스.
- ConcreteClass : 물려받은 primitive 메소드나 hook 메소드를 구현하는 클래스. 상위 클래스에 구현된 템플릿 메소드의 일반적인 알고리즘에서 하위 클래스에 적합하게 primitive 메소드나 hook 메소드를 override하는 클래스.

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>