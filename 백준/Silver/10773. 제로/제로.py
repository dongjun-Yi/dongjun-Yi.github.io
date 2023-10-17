k = int(input())

arr = list()
for _ in range(k):
  m = int(input())
  if m == 0:
    arr.pop()
  else:
    arr.append(m)

print(sum(arr))