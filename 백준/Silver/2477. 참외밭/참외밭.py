k = int(input())

a = []
width = []
height = []

for _ in range(6):
  direction, length = map(int, input().split())
  # 가로, 세로, 전체 입력 받기
  if direction == 1 or direction == 2:
    width.append(length)
    a.append(length)
  else:
    height.append(length)
    a.append(length)

# 가장 큰 사각형의 넓이
big_box = max(width) * max(height)

max_height_index = a.index(max(height))
max_width_index = a.index(max(width))

# 전체 배열에서 가장 큰 세로 길이의 인덱스 앞뒤가 작은 사각형의 가로가 됨. 반대로 가장 큰 가로 길이의 인덱스 앞뒤가 작은 사각형의 세로가 됨
small_width = abs(a[max_width_index - 1] -
                  a[max_width_index -
                    5 if max_width_index == 5 else max_width_index + 1])
small_height = abs(a[max_height_index - 1] -
                   a[max_height_index -
                     5 if max_height_index == 5 else max_height_index + 1])

# 큰 사각형에서 작은 사각형의 넓이를 뺴줌
small_box = small_width * small_height
area = big_box - small_box

print(area * k)
