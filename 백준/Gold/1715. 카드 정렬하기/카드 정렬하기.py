import heapq
import sys

n = int(sys.stdin.readline())
cards = []
result = 0
for _ in range(n):
  heapq.heappush(cards, int(sys.stdin.readline()))

if len(cards) == 1:  #1개일 경우 비교하지 않아도 된다
  print(0)
else:
  for i in range(n - 1):  # 2개씩 꺼내기 떄문에 n-1
    previous = heapq.heappop(cards)
    current = heapq.heappop(cards)

    result += previous + current
    heapq.heappush(cards, previous + current)

  print(result)
