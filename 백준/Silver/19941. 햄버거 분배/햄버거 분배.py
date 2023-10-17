n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n):
  if s[i] == 'P':
    for j in range(i - k, i + k + 1):
      if j >= n or j < 0:
        continue
      if s[j] == 'H':
        s[j] = 'O'
        cnt += 1
        break

print(cnt)