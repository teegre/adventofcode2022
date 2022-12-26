""" Day 09 - Rope Bridge """

with open('input.txt', 'r', encoding='utf-8') as f:
  inp = [ l[:-1] for l in f.readlines() ]

test = [ 'R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2' ]

class Knots:
  """ A moving head and a tail. """
  def __init__(self, heady=0, headx=0, taily=0, tailx=0):
    self.hy = heady
    self.hx = headx
    self.ty = taily
    self.tx = tailx
    self.tpos = { (self.ty,self.tx) }
  def right(self, dist=1):
    for _ in range(1, dist+1):
      self.hx += 1
      if self.hx - self.tx == 2:
        self.tx += 1
        self.ty = self.hy
        self.tpos.add((self.ty, self.tx))
  def left(self, dist=1):
    for _ in range(1, dist+1):
      self.hx -= 1
      if self.tx - self.hx == 2:
        self.tx -= 1
        self.ty = self.hy
        self.tpos.add((self.ty, self.tx))
  def up(self, dist=1):
    for _ in range(1, dist+1):
      self.hy += 1
      if self.hy - self.ty == 2:
        self.ty += 1
        self.tx = self.hx
        self.tpos.add((self.ty, self.tx))
  def down(self, dist=1):
    for _ in range(1, dist+1):
      self.hy -= 1
      if self.ty - self.hy == 2:
        self.ty -= 1
        self.tx = self.hx
        self.tpos.add((self.ty, self.tx))
  @property
  def pos(self):
    """ Return current position. """
    return self.hy, self.hx, self.ty, self.tx
  @property
  def tail_pos(self):
    """ Return a sorted list of recorded tail positions """
    tpos = list(self.tpos)
    tpos.sort()
    return tpos
  def __str__(self):
    return f'head: y={self.hy} x={self.hx} | tail: y={self.ty} x={self.tx}'
  def __repr__(self):
    return f'knots: [tail:({self.ty},{self.tx}) | head:({self.hy},{self.hx})]'

knots = Knots()

def move():
  """ Move according to the instructions. """
  for m in inp:
    dir,dist = m.split()
    dist = int(dist)
    match dir:
      case 'R':
        knots.right(dist)
      case 'L':
        knots.left(dist)
      case 'U':
        knots.up(dist)
      case 'D':
        knots.down(dist)

move()
print('part one:', len(knots.tail_pos))
