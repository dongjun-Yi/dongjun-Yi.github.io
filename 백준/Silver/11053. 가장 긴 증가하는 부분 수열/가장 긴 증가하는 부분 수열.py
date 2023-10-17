n = int(input())
a = list(map(int, input().split()))
dy = [1] * n

for i in range(1, n):
  for j in range(i):
    if a[j] < a[i]:
      dy[i] = max(dy[i], dy[j] + 1)

print(max(dy))