import sys

input = sys.stdin.readline

n = int(input())
request_cost = list(map(int, input().split()))
total_cost = int(input())


def check_cost(mid):
  sum = 0
  for x in request_cost:
    if x < mid:
      sum += x
    else:
      sum += mid
  return sum


res = -sys.maxsize
lt = 0
rt = max(request_cost)

while lt <= rt:
  mid = (lt + rt) // 2
  if check_cost(mid) > total_cost:
    rt = mid - 1
  else:
    if res < mid:
      res = mid
    lt = mid + 1

print(res)
