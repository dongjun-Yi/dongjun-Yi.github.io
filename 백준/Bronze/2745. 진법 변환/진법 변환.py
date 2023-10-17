n, b = map(str, input().split())

b = int(b)
res = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(len(n)):
  tmp = 0
  a = 1
  for j in range(len(alphabet)):
    if alphabet[j] == n[i].lower():
      tmp = 9 + j + 1
      break
  else:
    tmp = int(n[i])

  for j in range(len(n) - i - 1):
    a *= b

  res += tmp * a

print(res)
