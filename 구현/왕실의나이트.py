# 내 풀이 -> 나이트가 움직일 수 있는 경우의 수가 8가지라는거는 알았는데 이거를
# 그 체스판 벗어나는거에 일일이 케이스를 구하려다가 못푼거같다.
# 상하좌우 문제처럼 나이트가 갈 수 있는 방향들을 배열에 정의해놓고 문자를 숫자로 변환 후 비교한다.
# 체스판 안벗어나게끔 오류 처리
# 를 해주면 된다
# (x+2, y+1), (x-2, y+1), (x+2,y-1), (x-2, y-1)
# (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)
# xList = [a,b,c,d,e,f,g,h]
# yList = [1,2,3,4,5,6,7,8]
#if xList == n[0]:
#  count+=2
# ord(문자)
#하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
#ord('a')를 넣으면 정수 97을 반환합니다.

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1  #1부터 시작하니깐

#나이트가 이동할 수 있는 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]
result = 0
for step in steps:
  next_row = row + step[0]
  next_col = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    result += 1

print(result)
