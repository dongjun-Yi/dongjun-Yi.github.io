def makeKan(n):
  if n == 1:
    return "-"
  else:
    left = makeKan(n // 3)
    center = " " * (n // 3)
    return left + center + left


while True:
  try:
    N = int(input())

    rst = makeKan(3**N)
    print(rst)
  except:
    break
