n, k = map(int, input().split())
result = 0

while True:
  #가장 가까운 K의배수를 계산하기 위해 필요한 연산
  target = (n // k) * k
  # result가 뺄 횟수를 계산해줌
  result = n - target
  n = target

  if n < k:  #더이상 나눌수 없을 때 탈출
    break

  result += 1  #나누는 횟수의 count증가
  n //= k  #여기서 실제로 나눔

result += (n - 1)  #남은수에 대해 1씩 빼기 - 그래야 1이 되기 때문에
print(result)
