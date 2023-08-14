---
title: "[알고리즘] 유효한 팰린드롬"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## 문제의 조건

주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며. 영문자와 숫자만을 대상으로 한다.

## 입력

```
"A man, a plan, a canal: Panama"
```

## 출력

```python
true
```

## 팰린드롬(Palindrome)이란?

---

앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장을 **팰린드롬(Palindrome)**이라고 한다.

## 풀이1

---

먼저 문자열을 입력받고, 이 문자열 중, 문자인 것만 따로 배열에 추가한다. 문자인것을 판별하는 `isalnum()` 함수를 사용하고, 대소문자를 구분하지 않으므로 입력받은 문자열을 모두 `lower()`로 소문자로 변환하고 리스트에 추가한다.

```python
strs = []
for char in s: # s는 입력받은 문자열
	if char.isalnum():
		strs.append(char.lower())
```

위의 코드로 입력값을 받은 후 strs을 `print()`로 출력하게 되면 arr에 담긴 리스트를 다음과 같이 확인할 수 있다.

```python
['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
```

이 후 펠린드롬 여부를 다음과 같이 판별한다.

```python
while len(arr) > 1:
	if arr.pop(0) != arr.pop():
			return False
return True
```

파이썬 리스트의 함수인 `pop(0)`이용하여 맨앞의 값과 `pop()`을 이용하여 마지막 값을 매칭하가면서 만약 일치하지 않은 경우, 펠린드롬이 아니라고 판단하여 False를 반한한다. 만약 while문을 모두 수행했다면 True를 반환한다.

전체 코드는 아래와 같다.

```python
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            arrstrsappend(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
    
```

## 풀이 2 (deque 자료형을 이용한 풀이)

---

위의 풀이1처럼 `pop(0)`연산을 사용하게 되면 첫 번째 값을 꺼내고, 그 안에서 재정렬이 일어나기 때문에 시간복잡도가 O(n)이 되게 된다. 이 연산 시간을 줄이기 위해 deque의 `popleft()`를 사용하여 해결할 수 있다.

```python
from collections import deque

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True
```

풀이 1처럼 리스트를 이용해 구현하고, n번씩 반복하면 시간 복잡도가 O(n^2)이 나오게 되지만, deque를 이용해 구현하게 되면 O(n)으로 성능이 개선되는것을 볼 수 있다.

## 풀이 3 (슬라이싱 사용)

---

슬라이싱을 이용하여 문제를 풀면 코드는 다음과 같다.

```python
import re

def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱
```

`s = re.sub('[^a-z0-9]', '', s)`를 이용해 정규식으로 불필요한 문자를 필터링 한다음, 파이썬의 슬라싱을 이용하여 앞뒤가 똑같은 문자열인지 판별할 수 있다.
파이썬의 슬라이싱에서 `[::-1]`을 이용하여 리스트를 뒤집을 수 있다. 

## 정리

---

유효한 펠린드롬 문제를 3가지 풀이 방법으로 알아보았다. 3가지 풀이 방법 중에서 풀이 3인 슬라이싱을 이용한 풀이 방법이 가장 빠르게 실행되었으며, 슬라이싱을 사용하면 내부적으로 C로 빠르게 구현되어있어 훨씬 더 좋은 속도를 보여주었다. 

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>