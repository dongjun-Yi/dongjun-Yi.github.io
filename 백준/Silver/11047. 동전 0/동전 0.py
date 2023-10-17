n, k = map(int, input().split())
coin = []

for i in range(n):
  coin.append(int(input()))

res = []
for x in coin:
  if x <= k:
    res.append(x)

res.sort(reverse=True)
cnt = 0

for i in range(len(res)):
  if k == 0:
    break
  cnt += k // res[i]
  k %= res[i]

print(cnt)