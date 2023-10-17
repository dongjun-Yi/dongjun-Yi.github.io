arr =[]

for _ in range(9):
  arr.append(int(input()))

sum_val = sum(arr)

for i in range(8):
  for j in range(i+1, 9):
    if sum_val - (arr[i] + arr[j]) == 100:
      tmp1 = arr[i]
      tmp2 = arr[j]

arr.remove(tmp1)
arr.remove(tmp2)

arr.sort()
for x in arr:
  print(x)