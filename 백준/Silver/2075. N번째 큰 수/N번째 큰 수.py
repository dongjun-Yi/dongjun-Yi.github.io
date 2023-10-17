import heapq

n = int(input())

graph = []

hq = []

for _ in range(n):
  numbers = list(map(int, input().split()))

  for number in numbers:
    if len(hq) < n:
      heapq.heappush(hq, number)
    else:
      if hq[0] < number:
        heapq.heappop(hq)
        heapq.heappush(hq, number)

# 최소힙이므로 n개로 구성된 heapq에서 가장 작은 값 출력  => n번째로 큰 수
print(hq[0])