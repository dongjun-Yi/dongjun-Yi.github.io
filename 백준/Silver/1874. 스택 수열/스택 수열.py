n = int(input())

stack = []
ans = []
cur = 1

for _ in range(n):
  num = int(input())

  while cur <= num:
    stack.append(cur)
    ans.append("+")
    cur += 1
  if stack[-1] == num:
    ans.append("-")
    stack.pop()
  else:
    print("NO")
    break

else:
  for x in ans:
    print(x)