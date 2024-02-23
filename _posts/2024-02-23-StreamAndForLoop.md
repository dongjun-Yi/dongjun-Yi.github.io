---
title: "Java Stream과 for 문"
author:
  name: dongjun-Yi
categories: [java]
tags: [java]
render_with_liquid: false
---

자바 `Stream API`를 이용해 코드를 구성하면 다양한 데이터 소스를 일관성있게 다룰 수 있다는 장점이 있어 가독성을 향상시키는 효과를 준다. 그럼 `for문`과 `Stream API`를 이용한 **반복문은** 성능의 차이가 있을까?

## for loop vs Stream

---

비교를 위해 원시타입 `int`를 저장하는 배열을 하나 만들고, 배열에서 가장 큰 원소를 찾는 함수를 각각 `for-loop`와 순차 스트림으로 만들어보자.

```java
int[] ints = new int[500000];

int[] a = ints;
int e = ints.length;
int m1 = Integer.MIN_VALUE;

long start1 = System.nanoTime();
for (int i = 0; i < e; i++) { // for loop
    if (a[i] > m1) m1 = a[i];
}
long end1 = System.nanoTime();
System.out.println("for-loop : " + (end1 - start1) + "ns");

long start2 = System.nanoTime();
int m2 = Arrays.stream(ints) // stream
        .reduce(Integer.MIN_VALUE, Math::max);
long end2 = System.nanoTime();
System.out.println("sequential stream : " + (end2 - start2) + "ns");
```

```java
for-loop : 4419500ns
sequential stream : 12006875ns
```

`for loop`과 `stream`을 비교해보니 결과가 매번 달랐지만 `for문이` **약 3배** 차이로 빠르게 실행되었다. 그 이유는 JIT 컴파일러가 `for문`을 40년이상 다뤄와서 그만큼 **최적화가** 되어있었지만 `stream`은 2015년에 도입되어 아직 컴파일러가 최적화를 못했다는 것이다. 그러면 `for문`이 무조건 `stream`을 이용한 반복보다 좋을까? **그렇지 않다.** 다음 예시를 통해 확인해보자.

```java
List<Integer> myList = new ArrayList(500000);
int m3 = Integer.MIN_VALUE;

long start3 = System.nanoTime();
for (int i : myList) // for loop
    if (i > m3) m3 = i;
long end3 = System.nanoTime();
System.out.println("for-loop wrapped Type : " + (end3 - start3) + "ns");

long start4 = System.nanoTime();
int m4 = myList.stream() // stream
        .reduce(Integer.MIN_VALUE, Math::max);
long end4 = System.nanoTime();
System.out.println("sequential stream wrapped Type : " + (end4 - start4) + "ns");
```

```java
for-loop wrapped Type : 181667ns
sequential stream wrapped Type : 1876333ns
```

위의 코드는 원시타입 `int`가 아닌 `Integer` 타입으로 비교해 `ArrayList`에서 가장 큰 값을 찾는 로직이다. 실행결과를 보면 매번 값이 달랐지만 `for문`과 `stream` **속도 차이가 줄어든것**을 확인할 수 있다. 그 이유는 무엇일까?

## Primitive Type Vs Reference Type

---

앞서 `for문`과 `stream`의 성능 차이가 얼마 나지 않았는데, 그 이유는 바로 `ArrayList`를 순회하는 비용이 워낙 커서 `for문`과  `stream`간의 성능을 압도해버린 것이다. `ArrayList`를 **순회하는 비용이 컸던 이유**는 바로 **참조형 타입**의 값을 사용했기 때문이다.

`int`와 같은 원시타입은 JVM내에서 `stack`에 저장되어 **직접 값을 참조**해서 가져올 수 있지만, `참조 타입`은 JVM내에서 `heap` 영역에 저장되기 때문에 `stack`에 있는 참조변수를 통해 **간접적으로** 값을 가져와야 한다. `참조 타입`을 `heap` 영역에 간접 참조하여 값을 가져오는 것은, 단순히 두 숫자 간의 크기 비교를 하는 것보다 훨씬 비싼 비용이다. 결국 **순회 비용**이 **계산 비용**보다 높았기 때문에 앞선 예제에서 `Integer`타입으로 가장 큰 숫자를 찾는 로직을 `for문`과 `stream`으로 비교했을 때 성능의 차이가 많이 나지 않았던 것이다.
그러면 **순회하는 비용**보다 **계산하는 비용**이 크게 된다면 결과는 달라질까?

****

![Untitled.png](/assets/images/StreamAndForLoop/Untitled.png)

이 자료는 Effective Java의 공저자인 Angelika Langer가 JAX London 2015에서 발표했던 ['The Performance Model of Streams in Java 8"](http://www.angelikalanger.com/Conferences/Videos/Conference-Video-GeeCon-2015-Performance-Model-of-Streams-in-Java-8-Angelika-Langer.html) 이라는 발표 자료 파일이다. 계산 비용을 크게 하기 위해 아파치 라이브러인 `slowSin()`을 이용할 수 있다. 이 메서드는 파라미터로 넘겨지는 메서드에 대해서 sin함수값을 취하고 이에 대한 테일러 급수를 계산하는 함수이다. 전과 같이 `int`타입의 배열과 `Integer` 타입에 대한 `ArrayList`를 10000개의 원소를 순회하여 `slowSin()`을 적용해보면 다음과 같다.

![Untitled.png](/assets/images/StreamAndForLoop/Untitled_1.png)

결과를 보면 `for문`과 `stream`의 차이가 없으며 **계산 비용**이 **순회비용**을 앞서 성능의 차이가 없는 것을 확인할 수 있다. 이로써 순회비용과 계산 비용이 충분히 크다면 `stream`의 속도는 `for문`에 가까워지는 것을 확인할 수 있다. 

## for loop Vs Stream 결론

---

Angelika Langer가 JAX London 2015에서 발표했던 'The Performance Model of Streams in Java 8"의 강의를 수강하여 `for문`과 `stream`의 성능을 예제를 통해 비교해보고 확인해보았다. `for문`은 오래전부터 사용되어 컴파일러가 최적화를 하였기 때문에 `stream`보다 성능이 빨랐지만, 원시타입과 참조타입의 값을 사용했을 때의 **순회비용**이 **계산비용보다** 앞서게 되면 `stream`의 성능이 `for문`과 비슷하였고, 계산비용도 마찬가지로 충분히 크게되면 `stream`이 `for문`과 비슷한 성능을 가진다는 것을 알게되었다. 
처음에는 `stream`은 `for문`보다 **성능이 떨어지는** 대신 **가독성을 향상**시켜준다는 **trade-off**가 있다는 것을 알았지만 **순회비용**과 **계산비용**이 `stream` 성능을 좌우하고 상황에 맞게 `for문`과 `stream API`를 이용해야겠다는 공부가 되었다.

<br>

<aside>
📖 references 
<br>
[[http://www.angelikalanger.com/Conferences/Videos/Conference-Video-GeeCon-2015-Performance-Model-of-Streams-in-Java-8-Angelika-Langer.html](http://www.angelikalanger.com/Conferences/Videos/Conference-Video-GeeCon-2015-Performance-Model-of-Streams-in-Java-8-Angelika-Langer.html)]
<br>
[[https://jaxlondon.com/wp-content/uploads/2015/10/The-Performance-Model-of-Streams-in-Java-8-Angelika-Langer-1.pdf](https://jaxlondon.com/wp-content/uploads/2015/10/The-Performance-Model-of-Streams-in-Java-8-Angelika-Langer-1.pdf)]

</aside>