---
title: "[Design Pattern] 추상 팩토리 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**구체적인 클래스를 지정하지 않고 관련성을 갖는 객체들의 집합을 생성하거나 서로 독립적인 객체들의 집합을 생성할 수 있는 인터페이스를 제공하는 패턴**

엘레베이터 부품 업체 변경하는 문제로 예를 들어보자. 엘레베이터를 구성하는 많은 부품들 중에서 모터와 문이 있다고 하자. LG라는 회사는 LG모터와 LG문을 제공하고, 현대는 현대 모터와 현대문을 제공한다.

우선 LG의 모터와 현대의 모터는 구체적인 제어 방식은 다르지만 엘레베이터 입장에서는 모터를 구동해 엘레베이터를 이동시킨다는 면에서 동일하다. 그러므로 추상 클래스로 Motor를 정의하고 LGMotor와 HyundaiMotor를 하위 클래스로 정의할 수 있다. Door도 마찬가지로 LGDoor와 HyundaiDoor를 하위클래스로 지정할 수 있다.

Motor

```java
public abstract class Motor {
    private Door door;
    private MotorStatus motorStatus;
    public void setDoor(Door door) {
        this.door = door;
        this.motorStatus = MotorStatus.STOPPED;
    }

    public void move(Direction direction) {
        MotorStatus motorStatus = getMotorStatus();
        if (motorStatus == MotorStatus.MOVING) return;
        DoorStatus doorStatus = door.getDoorStatus();
        if (doorStatus == DoorStatus.OPENED) door.close();
        moveMotor(direction); //이 부분이 제조사마다 다르게 구현됨
        setMotorStatus(MotorStatus.MOVING);
    }

    private void setMotorStatus(MotorStatus motorStatus) {
        this.motorStatus = motorStatus;
    }

    protected abstract void moveMotor(Direction direction);

    private MotorStatus getMotorStatus() {
        return motorStatus;
    }
}
```

LGMotor

```java
public class LgMotor extends Motor {
    @Override
    protected void moveMotor(Direction direction) {
        System.out.println("Lg motor is Moving " + direction);
    }
}
```

Motor

```java
public class HyundaiMotor extends Motor {
    @Override
   protected void moveMotor(Direction direction) {
        System.out.println("Hyundai motor is Moving " + direction);
    }
}
```

Door

```java
public abstract class Door {
    private DoorStatus doorStatus;
    public Door() {
        this.doorStatus = DoorStatus.OPENED;
    }

    public DoorStatus getDoorStatus() {
        return doorStatus;
    }

    public void close() {
        if (doorStatus == DoorStatus.CLOSED) return;
        doClose();
        doorStatus = DoorStatus.CLOSED;
    }

    protected abstract void doClose();

    public void open() {
        if (doorStatus == DoorStatus.OPENED) return;
        doOpen(); //이 부분이 제조사마다 다르게 구현됨
        doorStatus = DoorStatus.OPENED;
    }

    protected abstract void doOpen();
}
```

LGDoor

```java
public class LgDoor extends Door {
    @Override
    protected void doClose() {
        System.out.println("Close Lg Door");
    }

    @Override
    protected void doOpen() {
        System.out.println("Open Lg Door");
    }
}

```

HyundaiDoor

```java
public class HyundaiDoor extends Door {
    @Override
    protected void doClose() {
        System.out.println("Close Lg Door");
    }

    @Override
    public void doOpen() {
        System.out.println("Open Lg Door");
    }
}

```

DirectionLamp

```java
public abstract class DirectionLamp {
    private Direction lampStatus;
    public void light(Direction direction) {
        if (lampStatus == getLampStatus()) return;
        doLight(lampStatus); //이 부분이 제조사마다 다르게 구현됨
        setLampStatus(lampStatus);
    }
    public Direction getLampStatus() {
        return lampStatus;
    }

    public void setLampStatus(Direction lampStatus) {
        this.lampStatus = lampStatus;
    }

    protected abstract void doLight(Direction lampStatus);
}
```

LGLamp

```java
public class LgLamp extends DirectionLamp {
    @Override
    protected void doLight(Direction direction) {
        System.out.println("Lg Lamp "+direction);
    }
}
```

HyundaiLamp

```java
public class HyundaiLamp extends DirectionLamp {
    @Override
    protected void doLight(Direction direction) {
        System.out.println("Hyundai Lamp "+direction);
    }
}
```

Elevator

```java
public class Elevator {
    private Motor motor;
    private Door door;
    private DirectionLamp lamp;

    public void setLamp(DirectionLamp lamp) {
        this.lamp = lamp;
    }
    public void setMotor(Motor motor) {
        this.motor = motor;
    }

    public void setDoor(Door door) {
        this.door = door;
    }

    public void move(Direction direction) {
        motor.move(direction);
        lamp.doLight(direction);
    }
}

```

Elevator

```java
public class ElevatorCreator {
    public static Elevator assembleElevator() {
        Elevator elevator = new LgElevator();
        Motor motor = new LgMotor();
        elevator.setMotor(motor);
        Door door = new LgDoor();
        elevator.setDoor(door);
        motor.setDoor(door);
        DirectionLamp lamp = new LgLamp();
        elevator.setLamp(lamp);
        return elevator;
    }

    public static void main(String[] args) {

        Elevator elevator =assembleElevator();
        elevator.move(Direction.UP);
    }
}
```

위의 코드에서 만약 [Elevator.java](http://Elevator.java)에서 LGElevator를 HyundaioElevator로 바꾸게 된다면 기존 코드를 변경해야 되므로 OCP에 위반되는것을 알 수 있다. **따라서 객체 생성을 자식 클래스에서 정의하도록 하기 위해 팩토리 메소드 패턴**을 적용하게되면 Elevator Factory는 다음과 같이 구성된다.

```java
public class ElevatorFactory {
    public static Elevator createElevator(VendorId id) {
        Elevator elevator = null;
        switch (id) {
            caseLG: elevator = new LgElevator(); break;
            caseHYUNDAI:elevator = new HyundaiElevator(); break;
        }
        return elevator;
    }
}
```

ElevatorFactory와 마찬가지로 Door, Motor, Lamp도 각각 Factory클래스를 만들고 ElevatorCreator.java는 다음과 같이 구성된다.

```java
public class ElevatorCreator {
    public static Elevator assembleElevator(VendorId id) {
        Elevator elevator = ElevatorFactory.createElevator(id);
        Motor motor = MotorFactory.createMotor(id);
        elevator.setMotor(motor);
        Door door = DoorFactory.createDoor(id);
        elevator.setDoor(door);
        motor.setDoor(door);
        DirectionLamp lamp = LampFactory.createLamp(id);
        elevator.setLamp(lamp);
        return elevator;
    }

    public static void main(String[] args) {

        Elevator elevator =assembleElevator(VendorId.HYUNDAI);
        elevator.move(Direction.UP);
    }
}

```

**But, 만약 새로운 제조업체의 부품을 사용한다면 각각 Factory 클래스에 새로운 제조업체에 대한 객체 생성을 해주어야하고,  만약 엘레베이터에 필요한 부품들이 10개면 Factory 클래스를 10개를 만들어야 된다.**

그래서, 부품별로 클래스를 구성하는게 아니라 제조업체 별로 팩토리를 정의해야 한다. 이러한 패턴을 추상 팩토리 패턴이다.

**클래스 다이어그램**

![Untitled.png](/assets/images/Abstract Factory Pattern/Untitled.png)

![Untitled1.png](/assets/images/Abstract Factory Pattern/Untitled 1.png)

ElevatorFactory

```java
public abstract class ElevatorAbstractFactory {
    public abstract Motor createMotor();
    public abstract Door createDoor();
    public abstract DirectionLamp createLamp();
    public abstract Elevator createElevator();
}
```

LGElevatorFactory

```java
public class LgElevatorFactory extends ElevatorAbstractFactory {
    @Override
    public Motor createMotor() {
        return new LgMotor();
    }

    @Override
    public Door createDoor() {
        return new LgDoor();
    }

    @Override
    public DirectionLamp createLamp() {
        return new LgLamp();
    }

    @Override
    public Elevator createElevator() {
        return new LgElevator();
    }
}
```

LGDoor

```java
public class LgDoor extends Door {
    @Override
    protected void doClose() {
        System.out.println("Close Lg Door");
    }

    @Override
    protected void doOpen() {
        System.out.println("Open Lg Door");
    }
}

```

LGMotor

```java
public class LgMotor extends Motor {
    @Override
    protected void moveMotor(Direction direction) {
        System.out.println("Lg motor is Moving " + direction);
    }
}

```

위와 같이 제조업체별로 팩토리 클래스를 만들고 하위 클래스에서 제조업체의 부품들을 정의해나가면 추상 팩토리 패턴을 적용할 수 있게 된다.

ElevatorCreator

```java
public class ElevatorCreator {
    public static Elevator assembleElevator(ElevatorAbstractFactory factory) {
        Elevator elevator = factory.createElevator();
        Motor motor = factory.createMotor();
        elevator.setMotor(motor);
        Door door = factory.createDoor();
        elevator.setDoor(door);
        motor.setDoor(door);
        DirectionLamp lamp = factory.createLamp();
        elevator.setLamp(lamp);
        return elevator;
    }
    public static void main(String[] args) {
        ElevatorAbstractFactory factory = null;
        if (args[0].equalsIgnoreCase("LG")) factory = new LgElevatorFactory();
        else if (args[0].equalsIgnoreCase("Hyundai")) factory = new HyundaiElevatorFactory();
        else factory = new SamsungElevatorFactory();
        Elevator elevator =assembleElevator(factory);
        elevator.move(Direction.UP);
    }
}
```

팩토리 메소드 패턴은 한 종류의 객체를 생성하기 위해 사용되지만, 추상 팩토리 메소드는 연관되거나 의존적인 객체로 이루어진 여러 종류의 객체를 생성하기 위해 생성된다.

![Untitled2.png](/assets/images/Abstract Factory Pattern/Untitled 2.png)

추상 팩토리 패턴은 이와 같이 관련성 있는 여러 종류의 객체를 일관된 방식으로 생성하는 경우에 유용하다.

- **AbstractFactory : 실제 팩토리 클래스의 공통 인터페이스. 각 제품의 부품을 생성하는 기능을 추상 메소드로 정의한다.**
- **ConcreteFactory : 구체적인 팩토리 클래스로 AbstractFactory 클래스의 추상 메소드를 오버라이딩함으로써 구체적인 제품을 생성한다.**
- **AbstractProduct : 제품의 공통 인터페이스**
- **ConcreteProduct : 구체적인 팩토리 클래스에서 생성되는 구체적인 제품**

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>