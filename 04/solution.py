""" Day 04 - Camp Cleanup """

# Part one
acc = 0
acc2 = 0
inp = []
inrange = lambda a,b,c,d: set(range(a,b+1)).issubset(range(c,d+1)) or set(range(c,d+1)).issubset(range(a,b+1))
intersect = lambda a,b,c,d: len(set(range(a,b+1)).intersection(set(range(c,d+1)))) > 0
with open('input.txt', 'r') as f:
  for line in f.readlines():
    line = line[:-1]
    p1, p2 = line.split(',')
    r11, r12 = p1.split('-')
    r21, r22 = p2.split('-')
    r = [int(r11),int(r12),int(r21),int(r22)]
    if inrange(*r):
      acc += 1
    if intersect(*r):
      acc2 += 1
print('part one:', acc)
print('part two:', acc2)
