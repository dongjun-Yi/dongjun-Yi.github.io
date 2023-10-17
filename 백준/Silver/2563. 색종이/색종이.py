# 각 x,y 좌표가 겹치는 곳은 빼주는거로 하려했는데, 그냥 겹치는거는 하나의 영역으로 계산하는게 답이었다.

n = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(n):
  a, b = map(int, input().split())
  for i in range(10):
    for j in range(10):
      paper[a + i][b + j] = 1

res = 0

for x in paper:
  res += sum(x)

print(res)