---
title: "[알고리즘] 가장 긴 팰린드롬 부분 문자열"
author:
  name: dongjun-Yi
categories: [algorithm]
tags: [algorithm, python]
render_with_liquid: false
---
## [문제](https://leetcode.com/problems/longest-palindromic-substring/){: target="_blank"}

가장 긴 팰린드롬 부분 문자열을 출력하라

## 입력

```
"babad"
```

```
"cbbd"
```

## 출력

```
"bab"
```

```
"bb"
```

## 풀이 (중앙을 중심으로 확장하는 풀이)

---

팰린드롬을 판별하기 위해, 포인터가 이동하면서 만약 포인터의 문자가 같을 때 중앙을 중심으로 점점 확장해 나가면서 가장 긴 팰린드롬을 찾을 수 있다.

방법을 자세히 설명하자면, 크기가 2개와 3개로 구성된 두개의 포인터가 앞으로 전진해나가는 방식이다. 2개로 구성된 포인터는 한칸씩 전진하고, 3개로 구성된 포인터는 2칸씩 전진한다. 이 방식은 **슬라이딩 윈도우**라고 부르며, 이때 윈도우에 들어온 문자열이 팰린드롬인 경우 그자리에서 멈추고 투포인터가 양옆으로 점점 확장해 나가는 방식이다. 

![Untitled.png](/assets/images/LongestPalindrome/python-38.jpg)

위의 그림과 같이 포인터가 이동하면서 팰린드롬인지 확인하며, 위의 그림에서는 홀수 포인터가 “454”라는 팰린드롬을 확인하고, 이 지점에서 왼쪽과 오른쪽으로 점차 확장해나가며 팰린드롬 중 가장 긴 팰린드롬을 찾아나간다.

코드로 살펴보면 다음과 같다.

```python
result = ''
for i in range(len(s) - 1):
  result = max(result,
               expand(i, i + 1),
               expand(i, i + 2),
               key=len)
```

먼저 짝수와 홀수 포인터가 이동하면서 가장 긴 팰린드롬인지 `expand()`함수로 확인하고, 그 중에서 가장 긴 문자열을 result변수에 담아 마지막에 최종적으로 result를 반환하게 된다.
여기서 **`max(key = len)` 은** 시퀀스중에서 가장 길이가 큰 요소를 반환해준다.

```python
def expand(left: int, right: int) -> str:
  while left >= 0 and right < len(s) and s[left] == s[right]:
      left -= 1
      right += 1
  return s[left + 1:right]
```

이 `expand()`함수에서는 만약 왼쪽과 오른쪽의 문자가 같다면 이 위치에서 양 옆으로 확장해 나가 가장 긴 팰린드롬을 찾을 수 있게 해준다.

만약 문자열 입력이 “babab”이라면, 팰린드롬을 판별하는 방식(홀수개의 팰린드롬인 경우)은 아래와 같다.

![Untitled.png](/assets/images/LongestPalindrome/python-381.jpg)

i = 0일 때 expand(0,2)가 호출되면서 s[0]과 s[2]의 문자가 같으므로 이 위치에서 양 옆으로 확장해 나간다. 이 예에서는 “bab”로 반환이 된다. (”aba”도 해당)

문자열 입력이 “cbbd”일때, 판별하는 방식이다.

![Untitled.png](/assets/images/LongestPalindrome/python-37.jpg)

이 예는 짝수개의 팰린드롬을 판별하는 방식이며 마찬가지로 가장 긴 팰린드롬을 반환해주는것을 확인할 수 있다.

전체 코드는 아래와 같다.

```python
	def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 해당 사항이 없을때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result
```

## 정리

---

포인터가 이동하면서 팰린드롬인지 확인하는 형태인 투 포인터에 대해서 배웠고, 파이썬의 내장 함수인 `max(len=key)`가 시퀀스(리스트, 문자열, 튜플 등) 중에서 가장 길이가 큰 요소를 찾을 때 사용하는 방법 중 하나라는 것을 알게되었다.

<aside>
📖 references 파이썬 알고리즘 인터뷰 - [책만]

</aside>