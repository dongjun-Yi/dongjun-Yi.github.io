res = []

for i in range(9):
    res.append(list(map(int, input().split())))

largest = 0

for i in range(9):
  for j in range(9):
    if largest < res[i][j]:
      largest = res[i][j]

for i in range(9):
  for j in range(9):
    if largest == res[i][j]:
      print(largest)
      print(i+1, j+1)
      break