""" Rucksack Reorganization """

from itertools import chain
abc = [chr(c) for c in chain(range(97,123),range(65,91))]
acc = 0

with open('input.txt', 'r') as f:
  for line in f.readlines():
    line = line[:-1]
    p1, p2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    item = { it for it in chain(p1,p2) if it in p1 and it in p2 }.pop()
    acc += abc.index(item)+1
print('part one:', acc)
