n, b = map(int, input().split())

res = []

alphbaet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while True:
  if n // b == 0:
    tmp = int(n)
    if tmp > 9:
      tmp1 = alphbaet[tmp - 10]
    else:
      tmp1 = str(tmp)
    res.append(tmp1)
    break
  tmp = int(n % b)
  if tmp > 9:
    tmp1 = alphbaet[tmp - 10]
  else:
    tmp1 = str(tmp)
  res.append(tmp1)
  n = int(n / b)

res = res[::-1]

for x in res:
  print(x, end='')
