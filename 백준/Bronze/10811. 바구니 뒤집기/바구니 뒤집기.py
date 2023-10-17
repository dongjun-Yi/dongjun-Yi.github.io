n,m = map(int, input().split())

array = []

for i in range(n+1):
  array.append(i)

for i in range(m):
  r_array = []
  a,b= map(int, input().split())
  for j in range(a,b+1):
    r_array.append(array[j])
  r_array = r_array[::-1]
  
  index= 0 
  for j in range(a,b+1):
    array[j] = r_array[index]
    index +=1

for i in range(1, n+1):
  print(array[i], end=" ")