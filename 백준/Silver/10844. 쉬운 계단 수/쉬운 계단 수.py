n = int(input())
dy = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
  dy[1][i] = 1

for i in range(2, n + 1):
  for j in range(10):
    if j == 0:
      dy[i][j] = dy[i - 1][1]
    elif j == 9:
      dy[i][j] = dy[i - 1][8]
    else:
      dy[i][j] = dy[i - 1][j - 1] + dy[i - 1][j + 1]

print(sum(dy[n]) % 1000000000)
