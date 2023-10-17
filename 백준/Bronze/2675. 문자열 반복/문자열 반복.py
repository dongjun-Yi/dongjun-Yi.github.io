n = int(input())

for i in range(n):
  m, s = input().split()
  for j in s:
    for k in range(int(m)):
      print(j, end="")
  print()