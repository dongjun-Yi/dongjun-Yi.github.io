from collections import deque

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


def dfs(v, visited):
  visited[v] = True
  graph[v].sort()
  res1.append(v)
  for x in graph[v]:
    if visited[x] == False:
      dfs(x, visited)


def bfs(v, visited):
  dq = deque([v])
  visited[v] = True

  while dq:
    cur = dq.popleft()
    res2.append(cur)
    graph[cur].sort()

    for x in graph[cur]:
      if visited[x] == False:
        dq.append(x)
        visited[x] = True


res1 = []

dfs(r, visited)

visited = [False] * (n + 1)
res2 = []

bfs(r, visited)

for x in res1:
  print(x, end=' ')
print()
for x in res2:
  print(x, end=' ')
