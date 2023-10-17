import sys

T = int(input())

for _ in range(T):
  n = int(input())
  # 크로스 컨트리 입력받기
  a = list(map(int, input().split()))

  # 참가팀 count
  country = list(set(a))

  # count 하지 말아야할 팀을 담아둘 변수
  no_score = []

  # 참가팀 중 해당 팀이 6명이 이하인 경우 해당 팀 배열 삽입
  for i in range(len(country)):
    if a.count(country[i]) < 6:
      no_score.append(country[i])

  # 참가선수의 점수 기록
  res = [[] for _ in range(len(country) + 1)]
  rank = 1
  for i in range(n):
    if a[i] not in no_score:
      res[a[i]].append(rank)
      rank += 1
    else:
      res[a[i]].append(None)

  # 팀의 점수 기록
  team_score = [0] * (len(country) + 1)

  # 4번째 팀원까지의 점수 합 기록
  for scores in range(1, len(res)):
    if scores not in no_score:
      for i in range(4):
        team_score[scores] += res[scores][i]

  for i in range(len(team_score)):
    if team_score[i] == 0:
      team_score[i] = sys.maxsize

  # 4번째 팀원끼리의 합이 같은 경우 5번째 팀원까지의 합산
  if team_score.count(min(team_score)) > 1:
    idx = []
    for i, score in enumerate(team_score):
      if min(team_score) == score:
        idx.append(i)

    min_value = sys.maxsize
    for x in idx:
      if min_value > res[x][4]:
        min_value = res[x][4]
        ans = x
    print(ans)

  else:
    # 점수가 가장 낮은 팀 출력
    winner_team = team_score.index(min(team_score))
    print(winner_team)
