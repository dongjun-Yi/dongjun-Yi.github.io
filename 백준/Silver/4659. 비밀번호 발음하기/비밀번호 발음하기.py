m = ['a', 'e', 'i', 'u', 'o']

while True:
  # 모음 3개 연속 방지 위한 카운트
  m_cnt = 0
  # 자음 3개 연속 방지 위한 카운트
  n_cnt = 0
  s = input()

  if s == 'end':
    break

  # 1. 모음이 문자열에 없다면 not acceptapble 출력
  for x in s:
    if x in m:
      break
  else:
    print("<" + s + "> is not acceptable.")
    continue

  # 2. 모음이나 자음이 연속으로 3개 올 경우 not acceptable 출력
  for x in s:
    if x in m:
      m_cnt += 1
      n_cnt = 0
      if m_cnt == 3:
        break

    else:
      n_cnt += 1
      m_cnt = 0
      if n_cnt == 3:
        break
  if m_cnt == 3 or n_cnt == 3:
    print("<" + s + "> is not acceptable.")
    continue

  # 같은 문자 2개 오는 경우
  for i in range(len(s) - 1):
    if s[i] == s[i + 1] and s[i] != 'o' and s[i] != 'e':
      print("<" + s + "> is not acceptable.")
      break
  else:
    print("<" + s + "> is acceptable.")
