import sys
from collections import deque
n,m,k,x = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
def bfs(x):
  q = deque([x])
  cnt = 0
  visited[x] = 1
  while q:
    cur = q.popleft()
    for node in graph[cur]:
      if visited[node] == 0:
        visited[node] = visited[cur] + 1
        q.append(node)
    
for _ in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)

bfs(x)
for i in range(len(visited)):
  visited[i]-=1
res = []

for i in range(1, len(visited)):
  if visited[i] == k:
    res.append(i)

if res:
  for x in res:
    print(x)
else:
  print(-1)