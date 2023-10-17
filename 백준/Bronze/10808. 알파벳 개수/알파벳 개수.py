s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

res = [0 * i for i in range(26)]

for x in s:
  for i in range(len(alphabet)):
    if alphabet[i] == x:
      res[i] += 1

for x in res:
  print(x, end=' ')
