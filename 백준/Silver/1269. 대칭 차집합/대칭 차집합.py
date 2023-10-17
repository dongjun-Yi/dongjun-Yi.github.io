n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
b.sort()


def check(x):
  lt = 0
  rt = m - 1

  while lt <= rt:
    mid = (lt + rt) // 2

    if x == b[mid]:
      return True
    elif x > b[mid]:
      lt = mid + 1
    else:
      rt = mid - 1
  return False


for x in a:
  if check(x):
    res.append(x)

cnt1 = n - len(res)
cnt2 = m - len(res)
print(cnt1 + cnt2)
