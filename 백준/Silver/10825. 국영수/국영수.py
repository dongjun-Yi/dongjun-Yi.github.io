n = int(input())
arr = []
for _ in range(n):
  name, kor, eng, math = input().split()
  arr.append((name, int(kor), int(eng), int(math)))

arr.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in arr:
  print(x[0])