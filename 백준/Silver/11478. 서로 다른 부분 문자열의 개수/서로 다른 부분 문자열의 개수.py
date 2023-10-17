s = input()

res = 0
ans = set()

for i in range(len(s)):
  for j in range(i, len(s)):
    tmp = s[i:j + 1]
    ans.add(tmp)

print(len(ans))
