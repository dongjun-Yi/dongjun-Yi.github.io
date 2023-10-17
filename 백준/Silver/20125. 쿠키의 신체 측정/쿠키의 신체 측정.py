n = int(input())
body = []

for _ in range(n):
  body.append(list(map(str, input())))

head = ()
for i in range(n):
  if head:
    break
  for j in range(n):
    if body[i][j] == '*':
      head = (i, j)
      break

# 심장 위치 출력
heart_x, heart_y = head[0] + 1, head[1]
print(heart_x + 1, heart_y + 1)

# 왼쪽 팔 길이
left_arm_length = 0
left_arm_y = heart_y - 1

while 0 <= left_arm_y < n and body[heart_x][left_arm_y] == '*':
  left_arm_y -= 1
  left_arm_length += 1

# 오른쪽 팔 길이
right_arm_length = 0
right_arm_y = heart_y + 1

while 0 <= right_arm_y < n and body[heart_x][right_arm_y] == '*':
  right_arm_y += 1
  right_arm_length += 1

# 허리 길이
waist_length = 0
waist_x = heart_x + 1

while 0 <= waist_x < n and body[waist_x][heart_y] == '*':
  waist_x += 1
  waist_length += 1

# 왼쪽 다리
left_leg_length = 0
left_leg_x = waist_x

while 0 <= left_leg_x < n and body[left_leg_x][heart_y - 1] == '*':
  left_leg_x += 1
  left_leg_length += 1

# 오른쪽 다리
right_leg_length = 0
right_leg_x = waist_x

while 0 <= right_leg_x < n and body[right_leg_x][heart_y + 1] == '*':
  right_leg_x += 1
  right_leg_length += 1

print(left_arm_length, right_arm_length, waist_length, left_leg_length,
      right_leg_length)
