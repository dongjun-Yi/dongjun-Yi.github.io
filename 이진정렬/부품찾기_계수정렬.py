n = int(input())

array = [0] * 1000001

x = list(map(int, input().split()))

for i in x:
  array[i] += 1

m = int(input())
y = list(map(int, input().split()))

for i in y:
  if array[i] == 1:
    print("yes", end=' ')
  else:
    print("no", end=' ')