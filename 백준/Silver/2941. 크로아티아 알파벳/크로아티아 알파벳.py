arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=' ]

s = input()
for x in arr:
  s = s.replace(x, 'a')

print(len(s))