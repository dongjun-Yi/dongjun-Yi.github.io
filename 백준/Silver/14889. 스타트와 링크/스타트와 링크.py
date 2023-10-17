import sys

input = sys.stdin.readline
n = int(input())

graph = []

visited = [False for _ in range(n)]
min_value = 1e9
for _ in range(n):
  graph.append(list(map(int, input().split())))


def dfs(depth, index):
  global min_value
  if depth == n // 2:
    start, link = 0, 0
    
    for i in range(n):
      for j in range(i + 1, n):
        if visited[i] and visited[j]:
          start += (graph[i][j] + graph[j][i])

        elif not visited[i] and not visited[j]:
          link += (graph[i][j] + graph[j][i])
    min_value = min(min_value, abs(start - link))
    return

  for i in range(index, n):
    if not visited[i]:
      visited[i] = True
      dfs(depth + 1, i + 1)
      visited[i] = False


dfs(0, 0)
print(min_value)
