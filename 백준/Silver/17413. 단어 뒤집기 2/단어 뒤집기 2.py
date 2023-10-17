import sys
s = sys.stdin.readline().strip() + ' '
stack = []

res = ''
flag = 0

for x in s:
  if x == '<':
    flag = 1
    for _ in range(len(stack)):
      res +=stack.pop()
  stack.append(x)

  if x == '>':
    flag = 0
    for _ in range(len(stack)):
      res +=stack.pop(0)

  if x == ' ' and flag == 0:
    stack.pop() # 들어간 공백 빼주기
    for _ in range(len(stack)):
      res +=stack.pop()
    res += ' '

print(res)
    