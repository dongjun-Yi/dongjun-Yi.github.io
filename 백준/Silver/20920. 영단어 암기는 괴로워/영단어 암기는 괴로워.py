import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# 입력받을 단어들
alp = []
# 단어 개수를 count하기 위한 set
word_list = set()

for _ in range(n):
  word = input().rstrip()
  if len(word) < m:
    continue
  alp.append(word)
  word_list.add(word)

# 단어 개수 count
d = dict()
for x in word_list:
  d[x] = 0

for w in alp:
  d[w] += 1

res = []

for word in d:
  res.append((word, d[word]))

# 1. 자주 나오는 단어는 맨 앞에 배치
# 2. 단어의 길이
# 3. 단어 사전순
# 여기서 맨 마지막 후순위인 단어사전순이 오름차순으로 정렬되어야 되는데 reverse = True조건을 str자료형에 쓸 수
# 없으므로 int 자료형의 첫번째 순위와 두번째 순위에 -연산자로 reverse = True로 되게끔 만들어 실행
res.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for x in res:
  print(x[0])
