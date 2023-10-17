n = int(input())
array = []
for i in range(n):
  array.append(int(input()))
array.sort()
array.reverse()

print(array)

# 출력 예시 형태를 착각하고 배열을 그대로 출력해버렸다. 이 때문에 list형태로 출력되었고
# sorted()함수 매개변수에 배열과 reverse속성을 넣을 수 있다는 걸 알게 됨

# 풀이
n = int(input())

array = []
for i in range(n):
  array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
  print(i, end=' ')
