""" Day 08 - Treetop Tree House """

from itertools import groupby

with open('input.txt', 'r', encoding='utf-8') as f:
  inp = [line[:-1] for line in f.readlines()]

test = [
    '30373',
    '25512',
    '65332',
    '33549',
    '35390'
]

# Part one
h,w = len(inp), len(inp[0])
count = h+(h-1)+(h-1)+(h-2)
for y,t1 in enumerate(inp[1:-1],1):
  for x,t2 in enumerate(t1[1:-1],1):
    t2 = int(t2)
    # print(f'({y},{x}) {t2}:', end=' ')
    # _ = [ print(f'v{inp[i][x]}', end=' ') for i in range(h) ]
    vt = [ int(inp[i][x]) for i in range(h) ]
    vv = [0 if i!=y and t < t2 else 'T' if i==y else 1 for i,t in enumerate(vt)]
    # print(vv, end=' ')
    # print('|', end=' ')
    # _ = [ print(f'h{inp[y][i]}', end=' ') for i in range(w) ]
    ht = [ int(inp[y][i]) for i in range(w) ]
    hh = [0 if i!=x and t < t2 else 'T' if i==x else 1 for i,t in enumerate(ht)]
    # print(hh, end=' ')
    i,j = vv.index('T'), hh.index('T')
    if sum(vv[:i]) == 0 or sum(vv[i+1:]) == 0 or sum(hh[:j]) == 0 or sum(hh[j+1:]) == 0:
      count += 1
    # print()
print('part one:', count)

# Part two
h,w = len(test), len(test[0])
for y,t1 in enumerate(test[1:-1],1):
  for x,t2 in enumerate(t1[1:-1],1):
    t2 = int(t2)
    vdist = [int(test[i][x]) if i!=y else 'T' for i in range(h)]
    hdist = [int(test[y][i]) if i!=x else 'T' for i in range(w)]
    print(f'({y},{x}) {t2}', 'v', vdist, 'h', hdist, end=' | ') 
    i,j = vdist.index('T'), hdist.index('T')
    u = vdist[i-1::-1]
    d = vdist[i+1:]
    l = hdist[j-1::-1]
    r = hdist[j+1:]
    up = sum(1 if a < t2 and a-b != 0 else 0 for a,b in zip(u,u[1:]))+1
    dw = sum(1 if a < t2 and a-b != 0 else 0 for a,b in zip(d,d[1:]))+1
    lt = sum(1 if a < t2 and a-b != 0 else 0 for a,b in zip(l,l[1:]))+1
    rt = sum(1 if a < t2 and a-b != 0 else 0 for a,b in zip(r,r[1:]))+1
    print(f'↑ {up}, ↓ {dw}, ← {lt}, → {rt} == {up*dw*lt*rt}')
