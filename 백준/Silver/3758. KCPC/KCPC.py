import sys

T = int(input())

for _ in range(T):
  n, k, t, m = map(int, sys.stdin.readline().split())
  # 점수, 제출횟수, 제출시간 배열에 저장
  score = [[0 for _ in range(k)] for _ in range(n)]
  submit = [0 for _ in range(n)]
  time = [0 for _ in range(n)]

  for j in range(m):
    ex = list(map(int, input().split()))
    score[ex[0] - 1][ex[1] - 1] = max(score[ex[0] - 1][ex[1] - 1], ex[2])
    submit[ex[0] - 1] += 1
    time[ex[0] - 1] = j

  line = []

  for h in range(n):
    line.append([sum(score[h]), submit[h], time[h], h])

  # 점수는 내림차순
  line.sort(key=lambda x: (-x[0], x[1], x[2]))

  for rank in range(n):
    # t인팀 순위 출력
    if line[rank][3] == t - 1:
      print(rank + 1)
