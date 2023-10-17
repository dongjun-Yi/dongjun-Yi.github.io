n = int(input())
arr = list(map(int, input().split()))

visited = [False]*n

def dfs(res):
  global ans
  if len(res) == n:
    total = 0
    for i in range(n-1):
      total +=abs(res[i] - res[i+1])
    ans = max(ans, total)
    return
    
  else:
    for i in range(n):
      if not visited[i]:
        visited[i] = True
        res.append(arr[i])
        dfs(res)
        visited[i] = False
        res.pop()
ans = 0
dfs([])

print(ans)