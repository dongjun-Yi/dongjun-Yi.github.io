# 2차원 배열까지는 생각, but 전체적인 감을 못잡았음음
# 2차원배열에 n까지의 수 중에서, k개를 만들 수 있는 경우의수를 담는다. dy[n][k]
# 이후 규칙을 찾음 dy[i][j] = dy[i-1][j] + dy[i][j-1]

n, k = map(int, input().split())
dy = [[0] * (k + 1) for _ in range(n + 1)]
dy[0][0] = 1

for i in range(n + 1):
  for j in range(1, k + 1):
    dy[i][j] = dy[i - 1][j] + dy[i][j - 1]

print(dy[n][k] % 1000000000)
