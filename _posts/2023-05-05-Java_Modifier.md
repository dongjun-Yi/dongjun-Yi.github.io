---
title: "[자바의 정석] 제어자"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---
## 제어자란?

---

제어자란 클래스, 변수 또는 메서드의 선언부와 함께 사용되어 부가적인 의미를 부여한다.

## static - 클래스의, 공통적인

---

인스턴스와 static 메서드의 근본적인 차이는 메서드 내에서 인스턴스 멤버를 사용하는가의 여부에 있다.

| 제어자 | 대상 | 의미 |
| --- | --- | --- |
| static | 멤버변수 | - 모든 인스턴스에 공통적으로 사용되는 클래스변수가 된다.
- 클래스 변수는 인스턴스를 생성하지 않고도 사용 가능하다.
- 클래스가 메모리에 로드될때 생성된다. |
|  | 메서드 | - 인스턴스를 생성하지 않고도 호출이 가능한 static 메서드가 된다.
- static 메서드 내에서는 인스턴스멤버들을 직접 사용할 수 없다. |

```java
class StaticTest {
			static int width = 200; //클래스 변수(static 변수)
			static int height = 120; //클래스 변수(static 변수)

			static { } //클래스 초기화 블럭(static 변수의 복잡한 초기화 수행)
			
			static int max(int a, int b) { //클래스 메서드(static 메서드)
						return a > b ? a : b
			}
} 
```

## final - 마지막의, 변경될 수 없는

---

final은 변수에 사용되면 값을 변경할 수 없는 상수가 되며, 메서드에 사용되면 오버라이딩을 할 수 없게 되고 클래스에 사용되면 자신을 확장하는 자손 클래스를 정의하지 못하게 된다.

| 제어자 | 대상 | 의미 |
| --- | --- | --- |
| final | 클래스 | 변경될 수 없는 클래스. 확장될 수 없는 클래스가 된다.
그래서 final로 지정된 클래스는 다른 클래스의 조상이 될 수 없다. |
|  | 메서드 | 변경될 수 없는 메서드, final로 지정된 메서드는 오버라이딩을 통해 재정의 될 수 없다. |
|  | 멤버변수 | 변수 앞에 final이 붙으면, 값을 변경할 수 없는 상수가 된다. |
|  | 지역변수 |  |

```java
final class FinalTest { //조상이 될 수 없는 클래스
				final int MAX_SIZE = 10; //값을 변경할 수 없는 멤버변수

				final void getMaxSize() { //오버라이딩할 수 없는 메서드
						final int LV = MAX_SIZE; //값을 변경할 수 없는 지역변수
						return MAX_SIZE;
				}
}
```

## 접근제어자(access modifier)

---

접근제어자는 멤버 또는 클래스에 사용되어, 해당하는 멤버 또는 클래스를 외부에서 직접 못하도록 역할을 한다.

| 제어자 | 설명 |
| --- | --- |
| public | 접근 제한이 전혀 없다. |
| protected | 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근이 가능하다. |
| default | 같은 패키지 내에서만 접근이 가능하다. |
| private | 같은 클래스 내에서만 접근이 가능하다. |

<aside>
📖 references Java의 정석(3판) [남궁 성/도우출판/2016]

</aside>