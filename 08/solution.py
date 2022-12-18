""" Day 08 - Treetop Tree House """

with open('input.txt', 'r', encoding='utf-8') as f:
  inp = [line[:-1] for line in f.readlines()]

test = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390'
]

h,w = len(test), len(test[0])
trees = []
for y,t1 in enumerate(test[1:-1],1):
  for x,t2 in enumerate(t1[1:-1],1):
    print(y,x,t2,':', end=' ')
    for i in range(h):
      if i == y:
        continue
      print(test[i][x], ';',end='')
      if test[i][x] < t2:
        trees.append(t2)
        break
    for i in range(w):
      if i == x:
        continue
      print(test[y][i], ';',end='')
      if test[y][i] < t2:
        trees.append(t2)
        break
    print()
