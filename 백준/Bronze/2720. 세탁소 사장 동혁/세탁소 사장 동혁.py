T = int(input())

coin = [0.25, 0.1, 0.05, 0.01]

res = []

for _ in range(T):
  s = int(input())

  for x in coin:
    x *= 100
    tmp = int(s // x)
    res.append(tmp)
    s = round(s % x, 2)

  for i in res:
    print(i, end=' ')
  print()
  res.clear()
