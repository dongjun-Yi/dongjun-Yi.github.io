n = int(input())
dy = [0] * 1000001

for i in range(2, n + 1):
  dy[i] = dy[i - 1] + 1

  if i % 2 == 0:
    dy[i] = min(dy[i // 2] + 1, dy[i])
  if i % 3 == 0:
    dy[i] = min(dy[i // 3] + 1, dy[i])

print(dy[n])
