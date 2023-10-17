x,y = map(int, input().split())

sum = 0
for i in range(1, x):
  if i == 1 or i==3 or i==5 or i == 7 or i==8 or i==10 or i==12:
    sum += 31
  elif i == 4 or i==6 or i==9 or i==11:
    sum+=30
  elif i==2:
    sum +=28

sum +=y

res = sum %7
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

print(day[res])