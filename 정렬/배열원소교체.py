n, k = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort()
listB = sorted(listB, reverse=True)

for i in range(k):
  listA[i], listB[i] = listB[i], listA[i]

sum =0 
for i in range(n):
  sum +=listA[i]

print(sum)
# 내 생각은 listA에서는 오름차순으로, listB는 내림차순으로 정렬해서 k번만큼 반복해서
# 순서대로 바꾸면 listA에 최대값으로만 구성될 줄 알았다.
# 근데 listA의 요소 중 listB의 요소보다 큰 값이 있을 수 있기 때문에 listB가 listA보다
# 클떄 바꿔줘야 listA에만 최대 값으로 구성된다. 


# 풀이

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else:
    break