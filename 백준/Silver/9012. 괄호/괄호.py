t = int(input())

for _ in range(t):
  a = []
  s = input()
  for x in s:
    if x == '(':
      a.append(x)
    else:
      if a and a[-1] == '(':
        a.pop()
      else:
        print("NO")
        break
  else:
    if a:
      print("NO")
    else:
      print("YES")
