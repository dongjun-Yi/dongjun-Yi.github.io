n = int(input())
line = 1

while n > line:
  n -= line
  line += 1

# 해당 숫자가 속한 줄이 짝수이면 증감 형태가 분자 +1/ 부모 -1
if line % 2 == 0:
  up = n
  down = line - n + 1
else:
  up = line - n + 1
  down = n

print(up, '/', down, sep='')
