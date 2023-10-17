n = int(input())

arr = []

for _ in range(n):
  arr.append(input())

res = list(arr[0])

for i in range(1, len(arr)):
  tmp = arr[i]
  for j in range(len(res)):
    if res[j] != tmp[j]:
      res[j] = "?"

for x in res:
  print(x, end='')
