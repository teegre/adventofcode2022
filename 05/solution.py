stacks = {
    #   TOP >>>>>>>>>>>>>>>>>>>> BOTTOM
    1: ['S','L','F','Z','D','B','R','H'],
    2: ['R','Z','M','B','T'],
    3: ['S','N','H','C','L','Z'],
    4: ['J','F','C','S'],
    5: ['B','Z','R','W','H','G','P'],
    6: ['T','M','N','D','G','Z','J','V'],
    7: ['Q','P','S','F','W','N','L','G'],
    8: ['R','Z','M'],
    9: ['T','R','V','G','L','C','M']
}

with open('input.txt', 'r') as f:
  procedure = [[int(w) for w in line.split() if w.isdigit()] for line in f.readlines()]

for op in procedure:
  cnt, src, dst = op
  while cnt > 0:
    stacks[dst].insert(0,stacks[src].pop(0))
    cnt -= 1
print('part one:', ''.join(crate[0] for crate in stacks.values()))
