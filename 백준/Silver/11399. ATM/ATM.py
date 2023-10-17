# 이 문제는 걸리는 시간이 최소인 사람을 앞에 보내서 최대합이 가장 작게 만드는게 중요하다. 그래서 정렬 후 답을 출력하면 된더.

n = int(input())
arr = list(map(int, input().split()))

arr.sort()


for i in range(1, len(arr)):
  arr[i] += arr[i-1]

print(sum(arr))