k, n = map(int, input().split())

line = []
for _ in range(k):
  line.append(int(input()))

lt = 1
rt = max(line)
res = 0


def Count(mid):
  sum = 0
  for x in line:
    sum += (x // mid)
  return sum


while lt <= rt:
  mid = (lt + rt) // 2

  if Count(mid) >= n:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)
