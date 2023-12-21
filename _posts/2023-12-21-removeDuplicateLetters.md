---
title: "[알고리즘] 중복 문자 제거"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## [문제](https://leetcode.com/problems/remove-duplicate-letters/){: target="_blank"}

중복된 문자를 제외하고 사전식 순서로 나열하라.

## 입력

```
"bcabc"
```

## 출력

```
"abc"
```

## 입력

```
"cbacdcbc"
```

## 출력

```
"acdb"
```

## 풀이1 (스택 일치 여부 판별)

---

이 문제를 풀기 전에, 사진식 순서라는 용어를 알아야한다. **사전식 순서**란 **사전에서 가장 먼저 찾을 수 있는 순서**를 말하며, bcabc에서 중복문자를 제외하면 사전에서 가장 먼저 찾을 수 있는 문자열은 abc가 될 것이다. 만약 앞에 e 문자가 하나 더 붙은 ebcabc가 입력값이라면 결과는 eabc가 될 것이다. 반면 입력값이 ebcabce라면 첫 번째 e는 중복으로 제거할 수 있고 마지막 e를 남겨서, 결과는 abce가 될 수 있다.

먼저 전체 코드를 보자.

```python
def removeDuplicateLetters(self, s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]

        # 전체 집합과 접미사 집합이 일치할때 분리 진행
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    return ''
```

중복문자를 제거하는 원리는 중복 문자를 제외한 알파벳순으로 문자열 입력값을 모두 정렬(`sorted(set(s)`)한 다음 접미사 suffix를 분리하여 확인한다. 분리 가능 여부는 **전체 집합**(`set(s)`)과 **접미사 집합**(`set(suffix)`)이 일치하는지 판별한다. 

```python
# 전체 집합과 접미사 집합이 일치할때 분리 진행
if set(s) == set(suffix):
    return char + self.removeDuplicateLetters(suffix.replace(char, ''))
```

이 코드는 사전식 순서를 만들기 위해 분리하는 데, 현재문자가 c라고 했을 때 c를 리턴하는 **재귀 호출 구조**로 처리한다. 이 후 뒤에 이어지는 모든 c는 `replace()`로 제거한다. 이렇게 되면 접미사 suffix가 점점 줄어들어 더 이상 남지 않을 때 백트래킹 되면서 조합된다.

아래는 입력값으로 “cbacdcbc”가 들어왔을 때 중복문자가 제거되는 과정을 보여준다.

![Untitled.png](/assets/images/RemoveDuplicateLetters/python-55.jpg)

![Untitled.png](/assets/images/RemoveDuplicateLetters/python-56.jpg)

`removeDuplicateLetters()`는 `rDL()`로 줄여서 함수를 표기하였고 전체 집합과 접미사 집합이 일치할 경우 분리가 진행되어 재귀형식으로 호출되며 진행되는 것을 볼 수 있다. 입력 예제와 같이 “cbacdcbc”가 입력값으로 들어올 경우, “acdb”가 반환되는 것을 알 수 있다.

## 풀이 2 (스택을 이용한 문자 제거)

---

스택을 이용하여 이 문제를 해결할 수 있는데, 먼저 스택을 이용한 코드를 보면 아래와 같다.

```python
def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
```

코드를 이해하기 위해 다음 실행과정을 살펴보자.

![Untitled.png](/assets/images/RemoveDuplicateLetters/python-57.jpg)

![Untitled.png](/assets/images/RemoveDuplicateLetters/python-58.jpg)

먼저 첫 번째 ‘c’가 스택에 삽입되는 동시에 `seen` 리스트에도 삽입된다. `seen` 리스트는 여기서 중복을 제거하기 위한 체크변수로, 만약 `seen` 리스트에 문자가 있다면 다음 문자로 스킵한다. 
그렇게 문자가 삽입되고 3번과정을 보면 `char=’a’`일 때, a는 문자 b,c보다 사전식으로 먼저오고, b,c는 아직 s문자열에 남아있으므로 스택에 있는 문자를 다 `pop()`되며 스택에 a가 삽입된다. 나머지도 이와 같이 실행되면서 문자가 사전식으로 나열되고 중복을 제거한 형태로 답을 찾을 수 있다.

## 정리

---

두가지 풀이로 이 문제를 풀어보았는데, 이해하기가 상당히 어려웠다. 동작과정을 그려보면서 해보니 이해할 수 있었고 중복을 제거하는 아이디어는 스택을 이용할 수 있다는 것을 배웠다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>