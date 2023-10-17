s = input()
one = 0
zero = 0

for i in range(len(s)):
  tmp = int(s[i])
  if tmp == 0:
    if int(s[i - 1]) == 0 and i > 0:
      continue
    zero += 1

for i in range(len(s)):
  tmp = int(s[i])
  if tmp == 1:
    if int(s[i - 1]) == 1 and i > 0:
      continue
    one += 1
cnt = 0

if one > zero:
  for i in range(len(s)):
    tmp = int(s[i])
    if tmp == 0:
      if int(s[i - 1]) == 0 and i > 0:
        continue
      cnt += 1

else:
  for i in range(len(s)):
    tmp = int(s[i])
    if tmp == 1:
      if int(s[i - 1]) == 1 and i > 0:
        continue
      cnt += 1

print(cnt)
