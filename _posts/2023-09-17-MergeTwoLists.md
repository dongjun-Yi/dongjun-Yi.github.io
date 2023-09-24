---
title: "[알고리즘] 두 정렬 리스트 병합"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---

## [문제](https://leetcode.com/problems/merge-two-sorted-lists/){: target="_blank"}

정렬되어 있는 두 연결 리스트를 합쳐라.
![Untitled.png](/assets/images/MergeTwoLists/Untitled.png)

## 입력

```
1 -> 2 -> 4, 1 -> 3 -> 4
```

## 출력

```
1 -> 1 -> 2 -> 3 -> 4 -> 4
```

## 풀이 1 (재귀 구조로 연결)

---

입력으로 들어오는 두 연결 리스트는 정렬된 리스트기 때문에 첫 번째 값부터 서로 비교하면서 재귀 형태로 풀 수 있다. 코드는 다음과 같다.

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
```

연결리스트는 해당 값과 다음 노드를 가르키는 변수로 구성되고,`mergeTwoLists()`는 재귀함수로 구현되어있다. 
매개변수로 두개의 연결 리스트를 받아 L1의 값과 L2의 값을 비교하여 L1의 값이 클 때  L2의 값과 교체하여 L1 리스트에 순서대로 정렬해 나간다. 이 때 L1의 다음값은 재귀 형태로 구현되어있는데, 이를 스택의 형태와 L1과 L2의 리스트의 변화되는 모습은 다음과 같다.

![Untitled.png](/assets/images/MergeTwoLists/python-57.jpg)

![Untitled.png](/assets/images/MergeTwoLists/python-58.jpg)

초기에는 L1과 L2는 각 연결리스트의 첫 번째 값을 가리킨다. 만약 L1이 L2의 값보다 크다면 L1과 L2의 값을 바꾸어 L1 리스트에 L2값들을 순서대로 병합하여 리스트를 합쳐 나간다. 
여기서 값을 스왑해나가면서 계속 재귀호출을 하는데, 이는 두개의 리스트를 하나로 합쳐주는 역할을 해준다. 그리고 마지막에 L1이 None이 되면 재귀가 끝나게 되고 호출한 함수쪽으로 return하게 된다. **return하면서 백트래킹이 끝나게 되면 리스트는 하나로 병합된 연결 리스트**가 된다.

## 정리

---

재귀 방식으로 리스트를 하나로 합치는 과정을 이해하는데 살짝 어려웠지만, 재귀로 구현된 코드는 코드의 길이가 짧고 풀이가 명확하다는 장점을 알게 되었다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>