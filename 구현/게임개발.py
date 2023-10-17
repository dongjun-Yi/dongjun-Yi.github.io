n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해 0으로 초기화
d = [[0] * m for i in range(n)]

# 현재 캐릭터 x, y, direction정보 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1  # (1,1)

# 전체 맵 정보 입력받기
array = []
for i in range(n):
  array.append(list(map(int, input().split())))

#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽으로 회전
def turn_left():
  global direction
  direction -= 1
  if direction == -1:
    direction = 3  #배열의 마지막 요소로 대입


# 시뮬레이션 시작
count = 1
# 네 방향 모두가 이미 가본칸인것들을 알기 위해 표시하는 변수
turn_time = 0

while True:
  # 왼쪽으로 회전 (1번 조건)
  turn_left()
  nx = x + dx[direction]
  ny = y + dy[direction]
  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동(2번 조건의 첫번째 케이스)
  if d[nx][ny] == 0 and array[nx][ny] == 0:
    d[nx][ny] = 1
    x = d[nx]
    y = d[ny]
    count += 1
    turn_time = 0  # 이동 후 아직 네 방향을 안돌았기 때문에 0으로 초기화
    continue
  # 회전한 이후 가보지 않은 칸이 없거나 바다인 경우(2번 조건의 두번째 케이스)
  else:
    turn_time += 1
  # 네 방향 이미 가본 칸인 경우
  if turn_time == 4:
    nx = x - dx[direction]
    ny = y - dy[direction]
    # 뒤로 갈 수 있다면 이동(3번 조건의 첫번째 케이스)
    if array[nx][ny] == 0:
      x = nx
      y = ny
    #뒤가 바다로 막혀있는 경우(3번 조건의 두번째 케이스)
    else:
      break
    turn_time = 0

print(count)