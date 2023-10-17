n, k = map(int, input().split())

res = []
for i in range(1, n + 1):
  if n % i == 0:
    res.append(i)

for i in range(len(res)):
  if len(res) < k:
    print(0)
    break
  elif i == (k - 1):
    print(res[i])
    break