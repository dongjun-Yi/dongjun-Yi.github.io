---
title: "[알고리즘] 팰린드롬 연결 리스트"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## [문제](https://leetcode.com/problems/palindrome-linked-list/){: target="_blank"}

연결 리스트가 팰린드롬 구조인지 판별하라.
![Untitled.png](/assets/images/PalindromeList/Untitled.png)

## 입력

```
1 -> 2
```

## 출력

```
false
```

## 입력

```
1 -> 2 -> 2 -> 1
```

## 출력

```
true
```

## 풀이1  (리스트 변환)

---

파이썬 리스트의 `pop()`연산을 통해 연결 리스트의 입력을 리스트로 변환하여 풀 수 있다.

먼저 연결 리스트를 구현한 ListNode클래스는 다음과 같다.

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

클래스로 정의된 ListNode는 해당 노드의 값(self.val)과 다음 값이 연결될 노드(self.next)로 구성되어 있다.

그래서 파이썬 리스트로 변환하여 풀이를 하면 다음과 같다.

```python
def isPalindrome(self, head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True
```

`q.pop(0) != q.pop()`를 통해 앞뒤 값을 비교하고 팰린드롬인지를 판별할 수 있다.

## 풀이 2 (데크를 이용한 최적화)

---

앞서 풀이의 `pop(0)`는 첫 번째 값을 꺼내오면 모든 값이 한 칸씩 시프팅 되어 시간복잡도가 O(n)이 된다. 이는 deque에서 `popleft()`를 이용하여 맨 앞의 값을 꺼내오는 연산을 O(1)로 풀이 될 수 있다.

```python
def isPalindrome(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        if q.popleft() != q.pop():
            return False

    return True
```

## 풀이 3 (런너를 이용한 우아한 풀이)

---

런너(Runner)는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법이다. **한 포인터가 다른 포인터보다 앞서게 하여** 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.

![Untitled.png](/assets/images/PalindromeList/python-54.jpg)

위의 그림처럼 각각 빠른 런너, 느린 런너라고 부르는 포인터 2개가 있고, 빠른 런너는 두칸씩 이동하고, 느린 런너는 한칸 씩 이동한다. 이때 빠른 런너가 연결 리스트의 끝에 도달하면, 느린 런너는 정확히 연결 리스트의 중간 지점을 가르킨다. 이를 이용해 **중앙값을 기준으로 앞뒤 문자가 같은지 확인하여 풀이**할 수 있다.
그래서 빠른런너와 느린런너의 이동을 코드로 나타내면 다음과 같다.

```python
fast = fast.next.next
slow = slow.next
```

위와 같이 빠른런너와 느린런너가 이동하면서 빠른런너가 리스트의 끝에 도달할 때까지 진행하면서 rev라는 리스트에다가 역순으로 값을 삽입한다.

![Untitled.png](/assets/images/PalindromeList/python-55.jpg)

```python
while fast and fast.next:
  fast = fast.next.next
  rev, rev.next, slow = slow, rev, slow.next
```

위와 같이 rev의 초기값은 None에서 시작하고, 느린 런너가 이동하면서  1→ None, 2 → 1 → None과 같이 역순으로 연결된다.

그리고 만약 연결리스트의 길이가 홀수이면 느린 런너가  팰린드롬인지 확인하기 위해  한칸 앞으로 이동한다.

```python
if fast:
  slow = slow.next
```

이 후 역순으로 런너를 통해 역순으로 구성된 rev와 slow의 런너를 통해 값이 일치하는지 확인하면 된다.

```python
while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next
```

전체 코드는 다음과 같다.

```python
def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev
```

## 정리

---

리스트에서의 연산 `pop()`연산을 deque `popleft()`연산을 통해 시간 복잡도를 O(1)로 줄일 수 있었고 런너를 활용한 풀이에서 빠른 런너가 리스트 끝에 도달했을 때 느린 런너가 중장지점에 온다는 것을 이용하여 역순으로 리스트로 구성해 팰린드롬인지 판별하는 방법도 알아보았다. 풀이 3개중에는 마지막에 풀이한 런너를 이용한 풀이가 가장 빠르게 실행되는 것을 알 수 있었다. 

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>