calories = []
with open('./input.txt') as f:
  acc = 0
  for line in f.readlines():
    l = int(line[:-1]) if line != '\n' else -1
    if l == -1:
      calories.append(acc)
      acc = 0
    else:
      acc += l
print(max(calories))
