alphabet = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

input_data = input()

result = 0

for i in input_data:
  for j in alphabet:
    if i in j:
      result += alphabet.index(j) + 3

print(result)
