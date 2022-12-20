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
  def move_up(self, dist=1):
    """ Move head up and record tail positions. """
    self.hy += dist
    if self.tx != self.hx:
      for x in range(self.tx, self.hx+1):
        self.tpos.add((self.ty, x))
      self.tx = self.hx
  def move_down(self, dist=1):
    """ Move head down and record tail positions. """
    self.hy -= dist
    if self.tx != self.hx:
      for x in range(self.tx, self.hx+1):
        self.tpos.add((self.ty, x))
      self.tx = self.hx
  def move_right(self, dist=1):
    """ Move head right and record tail positions. """
    self.hx += dist
    if self.ty != self.hy:
      for y in range(self.ty, self.hy+1):
        self.tpos.add((y, self.tx))
      self.ty = self.hy
  def move_left(self, dist=1):
    """ Move head left and record tail positions """
    self.hx -= dist
    if self.ty != self.hy:
      for y in range(self.ty,self.hy+1):
        self.tpos.add((y, self.tx))
      self.ty = self.hy
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
    return f'knots: [head:({self.hy},{self.hx})|tail:({self.ty},{self.ty})]'

knots = Knots()

def move():
  """ Move according to the instructions. """
  for m in test:
    dir,dist = m.split()
    dist = int(dist)
    match dir:
      case 'R':
        knots.move_right(dist)
      case 'L':
        knots.move_left(dist)
      case 'U':
        knots.move_up(dist)
      case 'D':
        knots.move_down(dist)

move()
print('part one:', len(knots.tail_pos))
