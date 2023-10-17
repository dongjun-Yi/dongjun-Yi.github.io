s = list(input())
c = "abcdefghijklmnopqrstuvwxyz"

for i in c:
  if i in s:
    print(s.index(i), end=" ")
  else:
    print(-1, end=" ")