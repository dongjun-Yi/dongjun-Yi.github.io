n = int(input())
arr = []
dy = [1] * n

for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])

for i in range(1, n):
  for j in range(i):
    if arr[j][1] < arr[i][1]:
      dy[i] = max(dy[i], dy[j] + 1)

print(n - max(dy))
