---
title: "[알고리즘] 로그 파일 재정렬"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## [문제](https://leetcode.com/problems/reorder-data-in-log-files/){: target="_blank"}

로그를 재정렬하라. 기준은 다음과 같다.

1. 로그의 가장 앞부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

## 입력

```python
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
```

## 출력

```python
["let1 art can", "let3 art zero","let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]
```

## 풀이 (람다와 + 연산자 사용)

---

먼저 문제의 조건에서 문자로 구성된 로그가 숫자 로그보다 이전에 오며, 숫자 로그는 입력 순서대로 둔다.
문자와 숫자를 구분해서 따로 저장하고, 정렬된 문자에 숫자를 이어 붙이면 된다. 받은 문자열에서 숫자인지 아닌지 판단은 `isdigit()`을 사용한다.

```python
for log in logs: # logs는 입력받은 문자열
	if log.split()[1].isdigit():
		digits.append(log)
	else:
		letters.append(log)
```

여기서 `log.split()[1]`은 받은 문자열에서 식별자를 제외하면 1번째 값으로, 이 값이 숫자이면 digits 리스트에 보관해 맨 나중에 letters 리스트가 순서가 정해지면 뒤에 붙이면 된다.
그래서 digits에 저장된 값을 출력해보면 다음과 같다.

```python
print(digits)
['dig1 8 1 5 1', 'dig2 3 6']
```

이후 문자 로그는 letters에 모두 모였으므로 다음 같이 정렬하면 된다.

```python
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
```

람다식을 이용하여 문자열에서 맨 첫번째 식별자를 제외한 첫번째 문자열부터 정렬하고, 동일한 경우 후순위 식으로 [0]를 지정해 정렬한다. 그래서 키는 [1:]로 정렬하고, 후순위 식은 [0]이 된다. 이후 문자로그와 숫자가 포함된 로그를 이어 붙여 반환하면 해결할 수 있다.

```python
return letters + digits
```

전체 코드는 다음과 같다.

```python
def reorderLogFiles(self, logs: List[str]) -> List[str]:
      letters, digits = [], []
      for log in logs:
          if log.split()[1].isdigit():
              digits.append(log)
          else:
              letters.append(log)

      # 두 개의 키를 람다 표현식으로 정렬
      letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
      return letters + digits
```

## 정리

---

람다식에서 키를 지정해서 정렬할 수 있고, 후 순위로도 정렬할 수 있다는 것을 배웠다. 람다식을 사용하여 정렬하니 코드가 짧아지고 간결해지는 장점이 있어 정렬에 유용하게 쓰면 좋을 것 같다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>