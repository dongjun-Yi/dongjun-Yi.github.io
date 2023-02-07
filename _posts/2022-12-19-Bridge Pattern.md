---
title: "[Design Pattern] 브릿지 패턴"
author:
  name: dongjun-Yi
categories: [Design Pattern]
tags: [java, design pattern]
render_with_liquid: false
---
**구현부에서 추상층에서 분리하여 각자 독립적으로 변형할 수 있게 하는 패턴**

TV로 채널과 소리를 제어할 수있는 리모컨의 사용에 대한 예로 브릿지 패턴의 사용을 알아보자

Tv

```java
public class Tv {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;
    public boolean isEnabled() { return on;}
    public void enable() { on = true; }
    public void disable() { on = false; }
    public int getVolume() { return volume; }
    public void setVolume(int volume) {
        if (volume > 100) {
            this.volume = 100;
        } else if (volume < 0) {
            this.volume = 0;
        } else {
            this.volume = volume;
        }
    }
		public int getChannel() { return channel; }
    public void setChannel(int channel) { this.channel = channel; }
    public void printStatus() {
        System.out.println("------------------------------------");
        System.out.println("| I'm TV set.");
        System.out.println("| I'm " + (on ? "enabled" : "disabled"));
        System.out.println("| Current volume is " + volume + "%");
        System.out.println("| Current channel is " + channel);
        System.out.println("------------------------------------\n");
    }
}
```

Remote

```java
public class Remote {
    protected Tv device;
    public Remote(Tv device) {
        this.device = device;
    }
    public void power() {
        System.out.println("Tv Remote: power toggle");
        if (device.isEnabled()) {
            device.disable();
        } else {
            device.enable();
        }
    }
    public void volumeDown() {
        System.out.println("Tv Remote: volume down");
        device.setVolume(device.getVolume() - 10);
    }
    public void volumeUp() {
        System.out.println("Tv Remote: volume up");
        device.setVolume(device.getVolume() + 10);
    }
		public void channelDown() {
				System.out.println("Tv Remote: channel down");
				device.setChannel(device.getChannel() - 1);
		}
		public void channelUp() {
				System.out.println("Tv Remote: channel up");
				device.setChannel(device.getChannel() + 1);
		}
}
```

만약 여기서 remote의 기능을 TV가 아닌 Radio로 바꾸고 싶다면 Remote.java에서 device로 된것을 Radio로 다 바꿔줘야 되기때문에 OCP에 위배되는것을 알 수 있다.

그래서 TV와 Radio를 포함할 수 있는 인터페이스 Device를 만들어 구성할 수 있다.

**클래스 다이어그램**

![Untitled.png](/assets/images/Bridge Pattern/Untitled.png)

But, 만약 Device쪽에 변화가 일어나는것이 아닌 Remote쪽에 변화가 일어나면?

예를 들어 Remote의 추가 기능중 Mute기능을 추가하고 싶다면 Remote 클래스를 상속받아 자식 클래스에서 정의하도록 구성할 수 있다.

**클래스 다이어그램**

![Untitled1.png](/assets/images/Bridge Pattern/Untitled 1.png)

Device

```java
public interface Device {
    boolean isEnabled();
    void enable();
    void disable();
    int getVolume();
    void setVolume(int percent);
    int getChannel();
    void setChannel(int channel);
    void printStatus();
}
```

Radio

```java
public class Radio implements Device {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;

    public boolean isEnabled() { return on;}
    public void enable() { on = true; }

    public void disable() { on = false; }

    public int getVolume() { return volume; }

    public void setVolume(int volume) {
        if (volume > 100) {
            this.volume = 100;
        } else if (volume < 0) {
            this.volume = 0;
        } else {
            this.volume = volume;
        }
    }

    public int getChannel() { return channel; }

    public void setChannel(int channel) { this.channel = channel; }
    public void printStatus() {
        System.out.println("------------------------------------");
        System.out.println("| I'm Radio set.");
        System.out.println("| I'm " + (on ? "enabled" : "disabled"));
        System.out.println("| Current volume is " + volume + "%");
        System.out.println("| Current channel is " + channel);
        System.out.println("------------------------------------\n");
    }
}
```

TV

```java
public class Tv implements Device {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;

    public boolean isEnabled() { return on;}
    public void enable() { on = true; }

    public void disable() { on = false; }

    public int getVolume() { return volume; }

    public void setVolume(int volume) {
        if (volume > 100) {
            this.volume = 100;
        } else if (volume < 0) {
            this.volume = 0;
        } else {
            this.volume = volume;
        }
    }

    public int getChannel() { return channel; }

    public void setChannel(int channel) { this.channel = channel; }
    public void printStatus() {
        System.out.println("------------------------------------");
        System.out.println("| I'm TV set.");
        System.out.println("| I'm " + (on ? "enabled" : "disabled"));
        System.out.println("| Current volume is " + volume + "%");
        System.out.println("| Current channel is " + channel);
        System.out.println("------------------------------------\n");
    }
}
```

BasicRemote

```java
public class BasicRemote {
    protected Device device;

    public BasicRemote(Device device) {
        this.device = device;
    }

    public void power() {
        System.out.println("Remote: power toggle");
        if (device.isEnabled()) {
            device.disable();
        } else {
            device.enable();
        }
    }

    public void volumeDown() {
        System.out.println("Remote: volume down");
        device.setVolume(device.getVolume() - 10);
    }

    public void volumeUp() {
        System.out.println("Remote: volume up");
        device.setVolume(device.getVolume() + 10);
    }

    public void channelDown() {
        System.out.println("Remote: channel down");
        device.setChannel(device.getChannel() - 1);
    }

    public void channelUp() {
        System.out.println("Remote: channel up");
        device.setChannel(device.getChannel() + 1);
    }

}
```

AdvanceRemoteWithMute

```java
public class AdvanceRemoteWithMute extends BasicRemote {
    public AdvanceRemoteWithMute(Device device) {
        super(device);
    }
    public void mute() {
        System.out.println("Remote: mute");
        device.setVolume(0);
    }
}
```

Main

```java
public class Main {
    public static void main(String[] args) {
        Tv tv = new Tv();
        BasicRemote r1 = new BasicRemote(tv);
        r1.power();
        r1.channelUp();
        tv.printStatus();

        Radio radio = new Radio();
        AdvanceRemoteWithMute r2 = new AdvanceRemoteWithMute(radio);
        r2.power();
        r2.volumeUp();
        radio.printStatus();
        r2.mute();
        radio.printStatus();
    }
}
```

**여기서 Remote의 기능은 TV에 의존된 기능을 제공을 하므로 상위 레벨 개념이고, TV는 하위 레벨 개념이 된다.** Remote 객체는 기능을 실행하기 위해서는 구현부인 TV에서 그 기능을 실행하기 떄문에 추상부(Remote)에서 구현부로 기능을 실현하기 위해 위임한다고 볼 수 있다.

![Untitled2.png](/assets/images/Bridge Pattern/Untitled 2.png)

- 추상부  : AdvancedRemoteWithMute.java
- 구현부 : TV, Radio

![Untitled3.png](/assets/images/Bridge Pattern/Untitled 3.png)

- **abstraction(BasicRemote) : 추상적 개념에 대한 인터페이스를 제공하고 객체 구현자(Implementor)에 대한 참조자를 관리한다.**
- **RefinedAbstraction(AdvanceRemoteWithMute) : 추상적 개념에 정의된 인터페이스를 확장한다.**
- **Implementor(Device) : 구현 클래스에 대한 인터페이스를 제공한다. 실질적인 구현을 제공한 서브 클래스들에 공통적인 연산의 시그니처만을 정의한다. 이 인터페이스는 Abstraction 클래스에 정의된 인터페이스에 정확하게 대응할 필요가 없다. 즉, 두 인터페이스는 서로 다른 형태일 수 있다. 일반적으로 Implemetor 인터페이스는 기본적인 구현 연산을 수행하고, Abstraction은 더 추상화된 서비스의 관점의 인터페이스를 제공한다.**
- **ConcreteImplementor(TV) : Implementor 인터페이스를 구현하는 것으로 실제적인 구현 내용을 담는다.**

<aside>
📖 references                                                                                                                                     정인상, 「JAVA 객체지향 디자인 패턴」, 한빛미디어

</aside>