---
title: 어댑터 패턴
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**클래스의 인터페이스를 사용자가 기대하는 인터페이스 형태로 변환시킨다. 서로 일치하지 않는 인터페이스를 갖는 클래스들을 함께 동작시킨다.**

Adder라는 인터페이스를 이용해 UserAdd가 덧셈을 구현하는 방식을 클래스 다이어그램으로 나타내면 다음과 같다.

![Untitled.png](/assets/images/Adapter Pattern/Untitled.png)

UserAdder는 Adder를 상속한 Adder객체와 더할 두 정수를 생성자의 매개변수로 받게 되어 계산을 하게 된다.

Adder

```java
public interface Adder {
    public int plus(int x, int y);
}
```

MyAdder

```java
public class MyAdder implements Adder {
    @Override
    public int plus(int x, int y) {
        return x + y;
    }
}
```

UserAdder

```java
public class UseAdder {
    public int add(Adder adder, int x, int y) {
        int r = 0;
        r = adder.plus(x, y);
        return r;
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        Adder adder = new MyAdder();
        UseAdder use = new UseAdder();
        System.out.println(use.add(adder, 10, 20));
      }
}

```

이런 상황에서는 문제가 없지만 만약 수정할 수 없는 라이브러리로 주어진 Adder형태를 사용해야한다면 이 구조로 사용이 가능할까? 그러면 Adder 인터페이스를 상속 받지 못하고 위의 예제에서 plus라는 기능을 사용못하고 라이브러리가 제공하는 형태에 맞춰서 사용을 해야한다. 이와 같은 제약사항에서 사용하는 패턴인 adpter 패턴이다.

사용하려는 인터페이스와 제공하는 인터페이스가 다르다면 **adpter 패턴을 적용하여 이 둘 사이에 호환이 되게끔 adpter 클래스**를 만들면 된다.

제공하는 인터페이스를 YourAdder라고 하면 YourAdder에서는 add라는 메소드를 제공하지만 UseAdder는 plus라는 연산을 사용하므로  이 둘을 연결해주는 YourAdapter 클래스를 만들어 사용하면 된다.

![Untitled1.png](/assets/images/Adapter Pattern/Untitled 1.png)

YourAdder

```java
public class YourAdder {
    public int add3(int x, int y, int z) {
        return x + y + z;
    }
}
```

YourAdder

```java
public class YourAdderAdapter implements Adder {
    private YourAdder yourAdder;
    public YourAdderAdapter(YourAdder yourAdder) {
        this.yourAdder = yourAdder;
    }
    @Override
    public int plus(int x, int y) {
        return yourAdder.add3(x, y, 0);
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        Adder adder = new MyAdder();
        UseAdder use = new UseAdder();
        System.out.println(use.add(adder, 10, 20));
        Adder adder1 = new YourAdderAdapter(new YourAdder());
        System.out.println(use.add(adder1, 10, 20));
    }
}
```

이렇게 되면 제공하는 인터페이스가 달라도 기존의 코드 수정없이 adpter만 추가하여 덧셈 연산을 구현할 수 있게 된다.

![Untitled2.png](/assets/images/Adapter Pattern/Untitled 2.png)

- **Client(UseAdder) : Target 인터페이스를 만족하는 객체와 동작할 대상**
- **Target(Adder) : 사용자가 사용할 응용 분야에 종속적인 인터페이스를 정의하는 클래스**
- **Adapter(yourAdapter) : Target 인터페이스에 Adaptee의 인터페이스를 적응 시키는 클래스**
- **Adaptee(YourAdder) : 인터페이스의 적응이 필요한 기존 인터페이스를 정의 하는 클래스로, 적응 대상자라고 함**

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>