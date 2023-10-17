n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))


def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에 종료 : 0,0부터 시작하기 때문에 n과 m 이상이면 범위를 벗어난다.
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    graph[x][y] = 1

    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1
print(result)