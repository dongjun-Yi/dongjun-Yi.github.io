#내가 쓴 답 : ifelse문으로 해결했는데 이동할 방향을 정의해서 반복문으로
# 그 문자가 일치하면 해당하는 좌표에 있는 배열 좌표를 통해 좌표를 구한다.

# n = int(input())
# x, y = 1, 1
# m = list(input().split())

# for i in m:
#   if i == 'R' and y != n:
#     y += 1
#   elif i == 'L' and y != 1:
#     y -= 1
#   elif i == 'D' and x != n:
#     x += 1
#   elif i == 'U' and x != 1:
#     x -= 1

# print(str(x) + " " + str(y))

#풀이
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, -1]
dy = [-1, -1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if move_types[i] == plan:
      nx = dx[i]
      ny = dy[i]
  if nx < 1 or nx > n or ny < 1 or ny > n:
    continue
  x, y = nx, ny
print(x, y)
