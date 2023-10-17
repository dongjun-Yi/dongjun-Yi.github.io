import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().split()))

res = []
arr1.sort()

for x in arr2:
  lt = 0
  rt = n-1
  while lt <=rt:
    mid = (lt+rt) //2
    if arr1[mid] == x:
      res.append(1)
      break
    if arr1[mid] > x:
      rt = mid-1
    else:
      lt = mid+1
  else:
    res.append(0)
for x in res:
  print(x, end=' ')