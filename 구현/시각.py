# 내 코드 : 시간을 문자열로 바꾸는거까지 생각했는데 in문법으로 3이 포함되어있는지 확인하는거를 생각 못했다. 
# 이게 그래서 완전탐색이라고 한다.
n = int(input())

#1의 자리
for i in range(60):
  if str(i).


#문제 풀이
h= int(input())

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j)+str(k):
        count +=1

print(count)