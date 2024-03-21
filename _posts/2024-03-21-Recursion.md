---
title: "[알고리즘] 재귀"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, C]
render_with_liquid: false
---
프로그래밍의 반복 알고리즘에 사용되는 알고리즘은 크게 2가지가 있다. 하나는 **반복문**을 이용해 순회하는 방식이고, 다른 하나는 **재귀**를 이용한 방식이다. 재귀란 **자기 자신을 호출**하면서 반복적으로 수행하는 코드이다. 팩토리얼을 계산하는 알고리즘을 재귀 형식으로 구현해보자.

![Untitled.png](/assets/images/Recursion/Untitled.png)

위 알고리즘은 재귀형식으로 팩토리얼을 구하는 방식으로 `Factorial()`인 함수가 **자기 자신을 호출**하면서 값을 누적하는 것을 알 수 있다.

![Untitled.png](/assets/images/Recursion/Untitled1.png)

재귀를 해결하려면 2가지의 과정이 필요하다. 첫번째로는 문제를 **탑다운방식**으로 **나누고**, 문제를 **바텀탑방식**으로 **풀어야한다.**

## 재귀 코드 설계

---

재귀형식으로 코드를 구현하려면 2가지 조건이 필요하다.

**Base Case** : 문제를 해결해야 하는 조건

**General Case** : 문제를 작은 문제로 사이즈를 줄여야 하는 조건

모든 재귀 알고리즘은 반드시 Base Case를 포함해야 한다. 앞서 팩토리얼 예제에서는 Base Case가 `factorial(0)`이 되고, general case는 `n X factorial(n-1)`이 된다.

따라서 재귀 알고리즘을 설계할때는 다음의 과정을 거치면된다.

1. Base Case 정의
2. General Case 정의
3. Base Case와 General Case를 합친다.

팩토리얼을 구하는 알고리즘을 재귀형식으로 구하면 다음과 같다.

```c
int resursiveFactorial(int n) {
		// base case
		if (n == 0) {
        return 1;
    } else { 
        return n * recursiveFactorial(n - 1); // general case
    }
}
```

## 재귀 VS 반복문

---

그럼 재귀와 반복문의 차이는 무엇일까? 차이를 알아보기 위해 팩토리얼을 구하는 코드를 반복문을 통해 구해보자.

```c
int iteraionFactorial(int n) {
		int sum = 1;
		for (int i = 1; i <= n; i++){
				sum *= i;
		}
		return sum;
}
```

차이를 살펴보면 **재귀**를 이용한 방식은 **지역변수 없이** 코드가 구성되고 **매번 다른 매개변수**를 통해 코드가 반복되고 있다. 재귀로 코드를 구현하면 코드가 **훨씬 단순하게** 구성할 수 있다. 하지만 재귀를 사용할때 주의점이 있다.

## 재귀의 한계

---

재귀를 사용하면 **추가적인 오버헤드**가 발생한다. 왜냐하면 재귀는 **자기 자신을 호출**하기 때문에 **Call Stack**에 **추가적인 메모리 할당**이 필요하기 때문이다. 그래서 재귀는 일반적으로 **반복문**보다 **더 느리게** 동작하게 된다. 따라서 재귀를 구현하기 전에 먼저 **주어진 공간과 시간**안에 해결할 수 있는지, 재귀 방식의 코드가 **더 짧고 이해하기 쉬운지**를 고려하여 사용해야 한다.

<aside>
📖 references <br>
Richard F. Gilberg, Behrouz A. Forouzan - Data Structures_ A Pseudocode Approach with C-Cengage Learning (2004)

</aside>