n = str(input())

ch = [0 * i for i in range(9)]

for x in n:
  if int(x) == 9:
    ch[5] +=1
  else:
    ch[int(x)-1] +=1


ch[5] = (ch[5]+1)//2
print(max(ch))