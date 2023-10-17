import sys

input = sys.stdin.readline

word1 = input().strip()
word2 = input().strip()

dy = [0] * len(word2)

for i in range(len(word1)):
  cnt = 0
  for j in range(len(word2)):
    if cnt < dy[j]:
      cnt = dy[j]

    elif word1[i] == word2[j]:
      dy[j] = cnt + 1

print(max(dy))
