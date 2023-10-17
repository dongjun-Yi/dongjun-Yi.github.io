import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

for x in b:
  lt = 0
  rt = n - 1

  while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == x:
      print(1)
      break
    elif a[mid] < x:
      lt = mid + 1
    else:
      rt = mid - 1
  else:
    print(0)
