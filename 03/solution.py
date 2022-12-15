""" Rucksack Reorganization """
from itertools import chain

# Part one
abc = [chr(c) for c in chain(range(97,123),range(65,91))]
acc = 0

with open('input.txt', 'r') as f:
  for line in f.readlines():
    line = line[:-1]
    p1, p2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    item = { it for it in chain(p1,p2) if it in p1 and it in p2 }.pop()
    acc += abc.index(item)+1
print('part one:', acc)

# Part two
groups = []
group = []
acc = 0
with open('input.txt', 'r') as f:
  for i,line in enumerate(f.readlines(), 1):
    line = line[:-1]
    group.append(line)
    if i%3 == 0:
      groups.append(group)
      group = []

for group in groups:
  p1, p2, p3 = set(group[0]), set(group[1]), set(group[2])
  item = { it for it in chain(p1,p2,p3) if it in p1 and it in p2 and it in p3 }.pop()
  acc += abc.index(item)+1
print('part two:', acc)
