n = int(input())

arr = list(map(int, input().split()))
arr.insert(0, 0)
s = int(input())
student = []
for _ in range(s):
  a, b = map(int, input().split())
  student.append((a, b))

for x in student:
  gender, start = x[0], x[1]
  # 남자
  if gender == 1:
    for i in range(start, n + 1, start):
      if arr[i] == 1:
        arr[i] = 0
      else:
        arr[i] = 1
  # 여자
  if gender == 2:
    pointer = 1
    while True:
      if (start - pointer) < 1 or (start + pointer) > n:
        break
      if arr[start - pointer] != arr[start + pointer]:
        break
      else:
        if arr[start - pointer] == 0:
          arr[start - pointer] = 1
          arr[start + pointer] = 1
        else:
          arr[start - pointer] = 0
          arr[start + pointer] = 0
        pointer += 1

    if arr[start] == 0:
      arr[start] = 1
    else:
      arr[start] = 0

for i in range(1, n + 1):
  print(arr[i], end=' ')
  if i % 20 == 0:
    print()
