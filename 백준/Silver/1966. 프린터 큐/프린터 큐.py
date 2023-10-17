from collections import deque

T = int(input())

for _ in range(T):
  res = []
  n, m = map(int, input().split())
  need = list(map(int, input().split()))

  for i in range(n):
    res.append((i, need[i]))

  dq = deque(res)
  cnt = 0
  while dq:
    cur = dq.popleft()
    if any(cur[1] < x[1] for x in dq):
      dq.append(cur)
    else:
      cnt += 1
      if cur[0] == m:
        print(cnt)
        break
