s = input().split('-')

num = []
for x in s:
  sum = 0
  tmp = x.split('+')
  for y in tmp:
    sum += int(y)
  num.append(sum)

n = num[0]

for i in range(1, len(num)):
  n -= num[i]

print(n)
