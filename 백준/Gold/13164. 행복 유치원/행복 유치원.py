n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
res = []
for i in range(1, n):
  res.append(arr[i] - arr[i - 1])

res.sort(reverse=True)
print(sum(res[k - 1:]))
