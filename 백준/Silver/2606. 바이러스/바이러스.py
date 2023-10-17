n = int(input())
graph = [[] for _ in range(n + 1)]

computer = int(input())

for i in range(computer):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

res = 0
visited = [False] * (n + 1)


def dfs(graph, v, visited):
  global res
  visited[v] = True
  res += 1
  for x in graph[v]:
    if not visited[x]:
      dfs(graph, x, visited)


dfs(graph, 1, visited)
print(res - 1)
