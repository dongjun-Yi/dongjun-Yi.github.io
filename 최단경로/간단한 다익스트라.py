import sys

input = sys.stdin.readline
INF = int(1e9)  # 10억

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]

# 1부터 시작해서 n+1까지 초기화
# 방문 체크 리스트
visited = [False] * (n + 1)
# 벡터 테이블
distance = [INF] * (n + 1)

# 모든 간선 정보 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def get_smallest_node():
  min_value = INF
  # 거리가 가장 짧은 노드의 번호
  index = 0
  for i in range(n + 1):
    # 거리벡터 중 가장 짧은 것을 찾기 위한 비교
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index


def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  # graph안에 (x,y) 형태로 저장되는데 j[0]노드와graph[start] 사이의 거리가 j[1]인것이      다.
  for j in graph[start]:
    distance[j[0]] = j[1]

  for i in range(n - 1):
    now = get_smallest_node()
    visited[now] = True  # 방문 처리

    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])
