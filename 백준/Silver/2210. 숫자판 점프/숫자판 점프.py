graph = []

for _ in range(5):
  graph.append(list(map(int, input().split())))

visited = [[False] * 5 for _ in range(5)]

# 상하좌우
dx= [1,-1,0,0]
dy =[0,0,-1,1]

res = [0] * 6
tmp = []
def dfs(L, x,y):
  global res
  global tmp
  
  res[L] = graph[x][y]
  
  if L == 5:
    ch=""
    for s in res:
      ch += str(s)
    if ch not in tmp:
      tmp.append(ch)
    return
    
  else:
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >=5 or ny <0 or ny >= 5:
        continue
      dfs(L+1, x+dx[i], y+dy[i])
        

for i in range(5):
  for j in range(5):
    visited = [[False] * 5 for _ in range(5)]
    dfs(0,i,j)

print(len(tmp))