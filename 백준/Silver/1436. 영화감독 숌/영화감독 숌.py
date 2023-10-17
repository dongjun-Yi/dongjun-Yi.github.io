n = int(input())

cnt = 0
num = 1

while True:
  if '666' in str(num):
    cnt += 1
  if cnt == n:
    print(num)
    break
  num += 1
