n = int(input())

arr = list(map(int, input().split()))
erase_node = int(input())


def dfs(x):
  arr[x] = -2
  for i in range(n):
    if x == arr[i]:
      dfs(i)


dfs(erase_node)

cnt = 0
for i in range(n):
  if arr[i] != -2 and i not in arr:
    cnt += 1

print(cnt)