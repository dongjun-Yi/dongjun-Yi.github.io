---
title: "[알고리즘] 순열"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## [문제](https://leetcode.com/problems/permutations/){: target="_blank"}

서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.

## 입력

```
[1,2,3]
```

## 출력

```
[
	[1,2,3],
	[1,3,2],
	[2,1,3],
	[2,3,1],
	[3,1,2],
	[3,2,1]
]
```

## 풀이1 (DFS를 활용한 순열 생성)

---

순열은 모든 가능한 경우를 그래프 형태로 나열할 수 있기 때문에 그래프로 표현하면 다음과 같다.

![Untitled.png](/assets/images/Permutation/python-56.jpg)

위 그래프 형태를 만족시키는 코드로 구성하려면 재귀 형태로 구현하면 된다. 이전 값을 하나씩 덧붙여서 계속 재귀 호출을 하다가 리프노드(`len(elements) ==0`)에 도달한 경우 `result`변수에 결과를 담는다.
코드는 다음과 같다.

```python
def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results
```

재귀 형태로 구성했을 때 변수들의 변화량은 아래와 같이 진행된다.

![Untitled.png](/assets/images/Permutation/python-57.jpg)

## 풀이2 (itertools 모듈 사용)

---

```python
import itertools

def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
```

파이썬의 `itertools` 모듈을 사용해서 순열을 구할 수 있다. `itertools` 모듈은 반복자 생성에 최적화된 효율적인 기능들을 제공하므로 문제 풀이 속도도 빠르고 코드도 훨씬 간편하게 구성할 수 있다.

## 정리

---

순열의 모든 경우의 수를 그래프 형태로 나타내고 이 그래프 형태를 구현하기 위해 재귀방법을 사용하여 순열의 모든 경우의 수를 구할 수 있었다. 또한 itertools를 사용해 순열을 구할 수 있어 라이브러리 사용만으로 순열을 쉽게 구할 수 있는 방법도 알게 되었다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>