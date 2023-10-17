import sys

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

arr.sort()  # O(nlogn)

lt = 0
rt = n - 1
res = sys.maxsize
res1 = 0
res2 = 0

while lt < rt:  # O(n)

  if abs(arr[lt] + arr[rt]) < res:
    res = abs(arr[lt] + arr[rt])
    res1 = arr[lt]
    res2 = arr[rt]
  if arr[lt] + arr[rt] > 0:
    rt -= 1
  else:
    lt += 1

print(res1, res2)
