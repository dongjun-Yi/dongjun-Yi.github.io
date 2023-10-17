a = []

for i in range(5):
  a.append(list(map(str, input())))

largest = 0
for i in range(5):
  if largest <len(a[i]):
    largest = len(a[i])

for i in range(5):
  while len(a[i]) < largest:
    a[i].append(-1)

res =''

for i in range(largest):
  for j in range(5):
    if a[j][i] == -1:
      continue
    else:
      res +=a[j][i]

print(res)