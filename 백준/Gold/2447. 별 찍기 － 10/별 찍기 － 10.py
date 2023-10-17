n = int(input())


# 최소단위인 3의 패턴을 알고, 그 다음 9의 패턴을 안 뒤 N의 패턴을 알게 된다.
def recursion(n):
  if n == 3:
    return ["***", "* *", "***"]
  arr = recursion(n // 3)
  stars = []
  for i in arr:
    stars.append(i * 3)
  for i in arr:
    stars.append(i + ' ' * (n // 3) + i)
  for i in arr:
    stars.append(i * 3)
  return stars


print('\n'.join(recursion(n)))
