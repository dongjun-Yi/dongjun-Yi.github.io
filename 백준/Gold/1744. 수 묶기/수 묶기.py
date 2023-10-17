n = int(input())

minus= []
plus =[]
sum = 0
for _ in range(n):
  num = int(input())
  if num <= 0:
    minus.append(num)
  elif num >1:
    plus.append(num)
  else:
    sum +=num
  
plus.sort(reverse= True)
minus.sort()



for i in range(0,len(plus),2):
  if i == len(plus)-1:
    sum += plus[i]
  else:
    sum +=plus[i] * plus[i+1]

for i in range(0,len(minus),2):
  if i == len(minus) - 1:
    sum += minus[i]
  else:
    sum +=minus[i] * minus[i+1]
  
print(sum)