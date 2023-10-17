import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [i for i in range(101)]
visited = [0] * 101
for _ in range(n + m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a] = b

dice = [1, 2, 3, 4, 5, 6]


def bfs():
  q = deque([1])
  while q:
    cur = q.popleft()

    for i in range(6):
      nx = cur + dice[i]
      if nx < 0 or nx > 100:
        continue

      cnt = graph[nx]

      if visited[cnt] == 0:
        q.append(cnt)
        visited[cnt] = visited[cur] + 1

        if cnt == 100:
          return


bfs()

print(visited[100])
