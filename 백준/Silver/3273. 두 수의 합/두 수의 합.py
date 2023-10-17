import sys

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

x = int(input())
arr.sort()  # O(nlogn)

lt = 0
rt = n - 1
cnt = 0

while lt < rt:  # O(n)
  if arr[lt] + arr[rt] == x:
    cnt += 1
    lt += 1
    rt -= 1
  elif arr[lt] + arr[rt] > x:
    rt -= 1
  else:
    lt += 1

print(cnt)
