n, num, p = map(int, input().split())
score = []

if n:
  score = list(map(int, input().split()))

# 내림차순 정렬
score.sort(reverse=True)

rank = 0

for i in range(n):
  if score[i] < num:
    score.insert(rank, num)
    break
  rank += 1
else:
  score.append(num)

if rank + 1 > p:
  print(-1)

else:
  for i in range(len(score)):
    if num == score[i]:
      print(i + 1)
      break
