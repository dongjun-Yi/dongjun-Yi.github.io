T = int(input())
for _ in range(T):
  s = list(map(int, input().split()))
  num = s.pop(0)

  res = []
  res.append(s[0])
  step = 0
  for i in range(1, 20):
    for j in range(len(res)):
      if s[i] < res[j]:
        res.insert(j, s[i])
        step += len(res[j + 1:])
        break
    else:
      res.append(s[i])

  print(num, step)
