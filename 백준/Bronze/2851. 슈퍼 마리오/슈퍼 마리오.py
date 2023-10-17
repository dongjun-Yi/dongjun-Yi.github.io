import sys

arr = []
for i in range(10):
  arr.append(int(input()))

sum = 0

for i in range(10):
  if abs(100 - sum) < abs(100 - (sum + arr[i])):
    print(sum)
    sys.exit(0)
  else:
    sum += arr[i]
else:
  print(sum)
