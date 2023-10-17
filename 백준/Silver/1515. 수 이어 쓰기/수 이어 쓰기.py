nums = input()

# nums 문자열에 index
idx = 0
# 숫자가 nums배열에 있는지 체크하는 수
n = 0

while True:
  n += 1
  s = str(n)

  for x in s:
    if x == nums[idx]:
      idx += 1
      # nums문자열 길이보다 넘을 경우 다 찾은거기 때문에 출력하고 break
      if idx >= len(nums):
        print(n)
        exit()
