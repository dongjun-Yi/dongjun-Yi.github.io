import sys
input = sys.stdin.readline
n= int(input())

graph =[[] for _ in range(n+1)]

for i in range(1,n+1):
  graph[i].append(int(input()))

ans = []

def dfs(num):
  if visited[num] == False:
    visited[num] = True
    for i in graph[num]:
      tmp_up.add(num)
      tmp_bottom.add(i)

      if tmp_up == tmp_bottom:
        ans.extend(list(tmp_bottom))
        return
      dfs(i)

for i in range(1,n+1):
  visited= [False] * (n+1)
  tmp_up = set()
  tmp_bottom = set()
  dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)
