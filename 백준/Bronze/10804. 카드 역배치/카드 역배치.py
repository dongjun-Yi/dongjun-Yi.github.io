res = list(range(21))

for _ in range(10):
  a, b = map(int, input().split())
  for i in range((b - a + 1) // 2):
    res[a + i], res[b - i] = res[b - i], res[a + i]

res.pop(0)

for x in res:
  print(x, end=' ')
# res.reverse : 내림차순 정렬, 뒤집는게 아님!!
