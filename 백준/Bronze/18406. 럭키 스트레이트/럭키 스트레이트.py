s = input()
mid = len(s) // 2
sum1 = sum2 = 0
for i in range(mid):
  sum1 += int(s[i])

for i in range(mid, len(s)):
  sum2 += int(s[i])

if sum1 == sum2:
  print("LUCKY")
else:
  print("READY")