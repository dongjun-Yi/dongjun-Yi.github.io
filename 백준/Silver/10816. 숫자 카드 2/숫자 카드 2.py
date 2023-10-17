import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
res = []

a.sort()


def binary_search(lt, rt, target):
  while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == target:
      return a[lt:rt + 1].count(target)
    elif a[mid] > target:
      rt = mid - 1
    else:
      lt = mid + 1
  return 0


n_dic = {}

for x in b:
  lt = 0
  rt = n - 1
  if x not in n_dic:
    n_dic[x] = binary_search(lt, rt, x)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in b))
