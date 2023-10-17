n, m = map(int, input().split())

r, c, direction = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room = []
ch = [[0] * m for _ in range(n)]

ch[r][c] = 1
for _ in range(n):
  room.append(list(map(int, input().split())))


def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3


cnt = 1
turn_time = 0

while True:
  turn_left()
  nx = r + dx[direction]
  ny = c + dy[direction]

  if room[nx][ny] == 0 and ch[nx][ny] == 0:
    cnt += 1
    r = nx
    c = ny
    turn_time = 0
    ch[r][c] = 1
    continue
  else:
    turn_time += 1

  if turn_time == 4:
    nx = r - dx[direction]
    ny = c - dy[direction]

    if room[nx][ny] == 0:
      r = nx
      c = ny

    else:
      break
    turn_time = 0

print(cnt)
