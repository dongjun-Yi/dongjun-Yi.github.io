n = int(input())
roads = list(map(int, input().split()))
cost = list(map(int, input().split()))

res = roads[0] * cost[0]

min_value = cost[0]

for i in range(1, n - 1):
  if min_value > cost[i]:
    min_value = cost[i]
  res += min_value * roads[i]

print(res)
