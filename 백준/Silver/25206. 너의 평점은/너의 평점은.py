grade = [('A+', 4.5), ('A0', 4.0), ('B+', 3.5), ('B0', 3.0), ('C+', 2.5),
         ('C0', 2.0), ('D+', 1.5), ('D0', 1.0), ('F', 0)]
sum = 0
point = 0
for i in range(20):
  a, b, c = map(str, input().split())
  b = float(b)
  for x in grade:
    if c == x[0]:
      sum += b * x[1]
      point += b

res = sum / point
print(res)