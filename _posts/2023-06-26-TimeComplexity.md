---
title: "[알고리즘] 복잡도"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
# 복잡도

복잡도는 알고리즘의 성능을 나타내는 척도다. 복잡도는 시간복잡도와 공간복잡도로 나눌 수 있다.

## 시간복잡도

---

**시간 복잡도**란 알고리즘을 위해 필요한 연산의 횟수를 말한다. 시간 복잡도라고 해서 프로그램이 실행되는 시간을 나타내는 것 같지만, **주요로직의 반복횟수에 중점으로 측정된다.**

예를 들어 아래의 코드가 실행되는 시간을 측정해보자.

```python
sum =0
start = time.time()
for i in range(1,10000):
		sum+=1
end = time.time()

print(f"{end - start:.5f} sec")

# 첫번째 실행 결과 : 0.00133 sec
# 두번째 실행 결과 : 0.00154 sec
# 세번쨰 실행 결과 : 0.00201 sec
```

위의 결과를 보면 실행할 때마다 측정되는 값이 달라진다. 이는 컴퓨터 사양이나 실행될때 매번 달라지며 이것으로 시간복잡도를 측정하기 애매하다. 그래서 시간 복잡도는 **반복횟수에 중점을 맞춰서 측정하는 것이다.**

## 시간 복잡도 표기

---

시간 복잡도를 표현할 때는 빅오 표기법을 사용한다. 이 빅오 표기법은 함수의 상한만을 나타낸다
예를 들어 N개의 데이터가 있을 때, 모든 데이터의 값을 더한 결과를 출력하는 프로그램을 생각해보자

```python
array = [3, 5, 1, 2, 4]
sum = 0

for x in array:
    sum +=x

print(sum)

# 결과 : 15
```

이 부분에서 반복 횟수는 array에 있는 요소 개수와 비례하여, 만약 배열의 요소 개수를 n이라고 하면 n이 커짐에 따라 연산을 수행하므로 시간 복잡도는 O(N)이라고 표기한다.

```python
array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i*j
        print(temp)
```

이 소스코드는 데이터의 개수가 N개일 때 O(N제곱)의 시간 복잡도를 가진다. 이는 반복문이 2중 반복문이라서 반복횟수가 N * N 만큼 연산이 필요한 것이다.

> **일반적으로 코딩테스에서는 최악의 경우에 대한 연산 횟수가 가장 중요하다**
> 

## 공간 복잡도

---

공간 복잡도는 **입력 크기에 대해 어떠한 알고리즘이 실행되는데 필요한 메모리 공간의 양**이다. 공간 복잡도를 표기할 때도 빅오 표기법을 이용한다. 

다음은 C언어에서의 배열 선언 코드이다.

```c
int a[N];
```

여기서 int 자료형은 4byte이며, N개의 요소를 선언했으므로 공간은 4N byte가 필요할 것이다. 이것을 빅오 표기법으로 나타내면 O(4N) = O(N)여서 공간 복잡도는 O(N)이다.

파이썬에서는 int형에 자료가 없어, getsizeof()함수를 사용하여 알 수 있다.

```python
import sys

n = int(input())

print(sys.getsizeof(n))  #  객체의 크기 출력
```

이 함수는 파이썬 객체의 메모리 크기를 바이트 단위로 반환한다.

<aside>
📖 references 이것이 코딩테스다 with 파이썬 [한빛미디어]

</aside>