n = int(input())

standard = list(input())
answer = 0

for i in range(n - 1):
  cnt = 0
  compare = standard[:]
  word = input()

  for w in word:
    if w in compare:
      compare.remove(w)
    else:
      cnt += 1

  if cnt < 2 and len(compare) < 2:
    answer += 1

print(answer)
