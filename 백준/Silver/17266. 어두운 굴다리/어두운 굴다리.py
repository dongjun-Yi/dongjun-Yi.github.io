n = int(input())
m = int(input())

light = [0] + list(map(int, input().split())) + [n]

lt, rt = 0, n
res = 0

while lt <= rt:
  mid = (lt + rt) // 2

  # 양 끝 값에 가로등 불빛이 비춰지는지 확인 (맨처음과 맨 끝)
  if (light[1] - light[0]) > mid or (light[-1] - light[-2]) > mid:
    lt = mid + 1
    continue

  # 양 끝을 제외한 중앙이 불빛이 채워지는지 확인 (0+1 ~ light(n)-2)
  # 중앙의 경우 가로등 불빛은 양옆으로 채워지기 때문에 가로등 사이의 거리에 /2로 불빛이 채워지는지 측정
  # (가로등1 + 가로등2) / 2 = 높이
  for i in range(1, len(light) - 2):
    if (light[i + 1] - light[i]) / 2 > mid:
      lt = mid + 1
      break

  # 가로등 높이의 최소값 갱신
  else:
    res = mid
    rt = mid - 1

print(res)
