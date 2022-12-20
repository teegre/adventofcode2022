""" Day 09 - Rope Bridge """

with open('input.txt', 'r', encoding='utf-8') as f:
  inp = [ l[:-1] for l in f.readlines() ]

test = [ 'R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2' ]

class Knots:
  def __init__(self, heady=0, headx=0, taily=0, tailx=0):
    self.hy = heady
    self.hx = headx
    self.ty = taily
    self.tx = tailx
    self.tpos = set()
  def move_up(self):
    self.hy += 1
    if self.tx != self.hx:
      self.tx = self.hx
      self.tpos.add((self.ty, self.tx))
  @property
  def pos(self):
    return self.hy, self.hx, self.ty, self.tx
  def __str__(self):
    return f'{self.pos}'
  def __repr__(self):
    return f'knots: {self.pos}'
