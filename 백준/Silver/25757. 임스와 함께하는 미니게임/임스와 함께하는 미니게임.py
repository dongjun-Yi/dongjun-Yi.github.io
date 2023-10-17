n, game = input().split()

game_num = {'Y': 2, 'F' : 3, 'O' : 4}
ch = set()
cnt = 0
res = []
for _ in range(int(n)):
  s = input()
  if s in ch:
    continue
  ch.add(s)
  res.append(s)
  
  if len(res) == (game_num[game] -1):
    cnt +=1
    res.clear()

print(cnt)