# 정렬되지 않은 원소 중 가장 작은 값을 골라 앞쪽으로 순서대로 바꾸는 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min = i
  for j in range(i + 1, len(array)):
    if array[min] > array[j]:
      min = j

  array[i], array[min] = array[min], array[i]
print(array)
