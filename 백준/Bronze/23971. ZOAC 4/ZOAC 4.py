h, w, n, m = map(int, input().split())
import math

a = math.ceil(h / (n + 1))  # 세로에 몇 명이 앉는지를 계산합니다
b = math.ceil(w / (m + 1))  # 가로에 몇 명이 앉는지를 계산합니다
answer = a * b
print(answer)