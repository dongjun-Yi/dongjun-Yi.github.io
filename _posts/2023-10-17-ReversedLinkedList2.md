---
title: "[알고리즘] 역순 연결 리스트 II"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---

## [문제](https://leetcode.com/problems/reverse-linked-list-ii/){: target="_blank"}

인덱스 m에서 n까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

![Untitled.png](/assets/images/ReversedLinkedList2/Untitled.png)

## 입력

```
1 -> 2 -> 3 -> 4 -> 5 -> NULL, m = 2, n = 4
```

## 출력

```
1 -> 4 -> 3 -> 2 -> 5 -> NULL
```

## 풀이 ( 반복 구조로 노드 뒤집기)

---

이 풀이에서는 `start`와 `end`변수를 이용하여 풀이할 수 있다. `start`와 `end`를 기준으로 반복하면서 역순으로 뒤집으면서 풀이할수 있다. 

```python
root = start = ListNode(None)
root.next = head

# start, end 지정
for _ in range(m - 1):
    start = start.next

end = start.next
```

여기서 `start`는 변경이 필요한 2의 바로 앞 지점인 1을 가르키게 하고 `end`는 `start.next`인 2를 지정한다. `head`는 1이고 `root`가 `head`를 가르키게 하여 최종적으로 `root.next`를 반환하게 된다. 

그리고 `start`와 `end`는 **끝까지 값이 변하지 않는다**. 아래 코드는 start와 end를 기준으로 연결 리스트를 역순으로 바꾸는 역할을 한다. 위의 입력 예제로 코드와 함께 동작과정을 살펴보자.

![Untitled.png](/assets/images/ReversedLinkedList2/python-60.jpg)

```python
tmp = start.next
start.next = end.next
end.next = end.next.next
start.next.next = tmp
```

1. `start.next`를 `tmp`로 지정한다.
2. `start.next`는 `end.next`가 된다.
3. `end.next`는 `end.next.next`로 한 칸 더 앞의 값을 가르킨다.
4. `start.next.next` 는 `tmp`로 지정한다.

위와 같은 구조로 n-m번 반복하면 최종결과가 나오게 된다.

반복하면서 역순으로 리스트를 구성할 때 다중 할당 형태로 코드를 구성할 수 있다.

```python
def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
	  # 예외 처리
	  if not head or m == n:
	      return head
	
	  root = start = ListNode(None)
	  root.next = head

	  # start, end 지정
	  for _ in range(m - 1):
	      start = start.next
	  end = start.next
	
	  # 반복하면서 노드 차례대로 뒤집기
	  for _ in range(n - m):
	      tmp, start.next, end.next = start.next, end.next, end.next.next
	      start.next.next = tmp
	  return root.next
```

## 정리

---

반복문을 활용해서 연결 리스트를 역순으로 뒤집을 수 있고, 노드를 차례대로 뒤집을 때 다중 할당 구조를 사용하면 소스코드가 간결해지는 것을 볼 수 있었다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>