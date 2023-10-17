n, k = map(int, input().split())
country = []

for _ in range(n):
  a = list(map(int, input().split()))
  if a[0] == k:
    standard = a
  else:
    country.append(a)

rank = 1
for i in range(len(country)):
  if country[i][1] > standard[1]:
    rank += 1
  elif country[i][1] == standard[1]:
    if country[i][2] > standard[2]:
      rank += 1
    elif country[i][2] == standard[2]:
      if country[i][3] > standard[3]:
        rank += 1

print(rank)
