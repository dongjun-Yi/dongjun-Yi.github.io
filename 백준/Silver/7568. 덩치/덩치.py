n = int(input())

people = []

for _ in range(n):
  a, b = map(int, input().split())
  people.append((a, b))

res = []
for i in range(n):
  rank = 1
  for j in range(n):
    if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
      rank += 1
  res.append(rank)

for x in res:
  print(x, end=' ')
