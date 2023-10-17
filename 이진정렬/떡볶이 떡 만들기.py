# 딱 6에 맞추는 것이 아니라 최대한 덜 잘랐을 때가 정답이여서 중간에 기록해야함
n, m = map(int, input().split())

array = list(map(int, input().split()))

result = 0


def binary_search(array, target, start, end):
  global result
  while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in array:
      if i > mid:
        sum += i - mid

    if sum >= target:
      result = mid
      start = mid + 1
    else:
      end = mid - 1


binary_search(array, m, 0, max(array))
print(result)
