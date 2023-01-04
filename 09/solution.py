"ini"" Day 09 - Rope Bridge """

with open('input.txt', 'r', encoding='utf-8') as f:
  inp = [ l[:-1] for l in f.readlines() ]

test = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']

test_pos = [
    (0,0), (0,1), (0,2), (0,3),
    (1,4),
    (2,1), (2,2), (2,3), (2,4),
    (3,3), (3,4),
    (4,2), (4,3)
]

test_positions = [
    (0,0), (0,0), (0,0), (0,0),
    (1,1),
    (2,2), (2,3), (2,2), (2,1), (2,1)
]

test2 = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']

test2_pos = [
    (-5,-2),(-5,-1),(-5,0),(-5,1),(-5,2),(-5,3),(-5,4),(-5,5),
    (-4,-3),(-4,6),
    (-3,-4),(-3,7),
    (-2,-5),(-2,8),
    (-1,-6),(-1,9),
    (0,0),(0,-7),(0,10),
    (1,-8),(1,1),(1,9),
    (2,-9),(2,2),(2,8),
    (3,-10),(3,1),(3,7),
    (4,-11),(4,2),(4,6),
    (5,-11),(5,3),(5,4),(5,5),
    (6,-11)
]

test2_pos.sort()

class Knot:
  """ A knot """
  def __init__(self, y=0, x=0, name='H'):
    self.y = y
    self.x = x
    self.name = name
    self.parent = None
    self.child = None
    self.pos = {(y, x)}

  def add(self, child):
    """ Add a child knot """
    self[-1].child = child
    child.parent = self[-2]

  def right(self, dist=1):
    """ Move knot to the right """
    # print(f'>> R{dist}', self)
    for _ in range(dist):
      self.x += 1
      if not self.child:
        self.pos.add((self.y, self.x))
        continue
      if abs(self.y - self.child.y) == 2:
        # print(self, '→', self.child, 'x+', end='')
        if self.child.x == 0:
          self.child.x = 1
        else:
          self.child.x = self.x
        if self.y > self.child.y:
          # print('U')
          self.child.up()
        elif self.y < self.child.y:
          # print('D')
          self.child.down()
      elif self.x - self.child.x == 2:
        # print(self, '→', self.child, 'y+R')
        self.child.y = self.y
        self.child.right()
    # print(f'R{dist}', self, '<<')

  def left(self, dist=1):
    """ Move knot to the left """
    # print(f'>> L{dist}', self)
    for _ in range(dist):
      self.x -= 1
      if not self.child:
        self.pos.add((self.y, self.x))
        continue
      if abs(self.y - self.child.y) == 2:
        if self.child.x == 0:
          self.child.x = -1
        else:
          self.child.x = self.x
        if self.y > self.child.y:
          self.child.up()
        elif self.y < self.child.y:
          self.child.down()
      if self.child.x - self.x == 2:
        self.child.y = self.y
        self.child.left()
    # print(f'L{dist}', self, '<<')

  def up(self, dist=1):
    """ Move knot up """
    # print(f'>> U{dist}', self)
    for _ in range(dist):
      self.y += 1
      if not self.child:
        self.pos.add((self.y, self.x))
        continue
      if abs(self.x - self.child.x) == 2:
        # print(self, '→', self.child, 'y+', end='')
        if self.child.y == 0:
          self.child.y = 1
        else:
          self.child.y = self.y
        if self.x > self.child.x:
          # print('R')
          self.child.right()
        elif self.x < self.child.x:
          # print('L')
          self.child.left()
      if self.y - self.child.y == 2:
        # print(self, '→', self.child, 'x+U')
        self.child.x = self.x
        self.child.up()
    # print(f'U{dist}', self, '<<')

  def down(self, dist=1):
    """ Move knot down """
    # print(f'>> D{dist}', self)
    for _ in range(dist):
      self.y -= 1
      if not self.child:
        self.pos.add((self.y, self.x))
        continue
      if abs(self.x - self.child.x) == 2:
        if self.child.y == 0:
          self.child.y = -1
        else:
          self.child.y = self.y
        if self.x > self.child.x:
          self.child.right()
        elif self.x < self.child.x:
          self.child.left()
      if self.child.y - self.y == 2:
        self.child.x = self.x
        self.child.down()
    # print(f'D{dist}', self, '<<')

  def reset(self):
    """ Reset knot and its children coordinates """
    self.y, self.x = 0, 0
    self.pos = {(0,0)}
    if self.child:
      self.child.reset()

  @property
  def knots(self):
    """ List of knots """
    ch = []
    ch.append(self)
    if self.child:
      ch.extend(self.child.knots)
    return ch

  @property
  def root(self):
    """ Root knot """
    if self.parent:
      return self.parent.root
    return self

  @property
  def index(self):
    """ Knot index """
    return self.root.knots.index(self)

  @property
  def last(self):
    """ Last node """
    return self[-1]

  @property
  def coord(self):
    """ Knot coordinates as a tuple """
    return self.y, self.x

  @property
  def r_knots(self):
    """ Reversed list of knots """
    return list(reversed(self.knots))

  @property
  def positions(self):
    """ Return a sorted list of recorded tail positions """
    tpos = list(self[-1].pos)
    tpos.sort()
    return tpos

  @property
  def min(self):
    """
    Return knot with coordinates higher than (0,0) if any
    or return first child of root knot otherwise
    """
    min_k = min(self)
    if min_k.coord == (0,0):
      for k in reversed(self):
        if k.coord > min_k.coord:
          return k
    return min_k.child if min_k.child else min_k

  def __getitem__(self, index):
    return self.root.knots[index]

  def __iter__(self):
    knots = self.knots
    for k in knots:
      yield k

  def __len__(self):
    return len(self.knots)

  def __lt__(self, other):
    return self.coord < other.coord

  def __gt__(self, other):
    return self.coord > other.coord

  def __str__(self):
    return f'{self.name}: ({self.y},{self.x})'

  def __repr__(self):
    return f'{self.name}: ({self.y},{self.x})'

def make_rope(length=2):
  the_rope = Knot()
  for i in range(1, length):
    the_rope.add(Knot(name=str(i)))
  return the_rope

rope = make_rope()

def move():
  """ Move according to the instructions. """
  for m in inp:
    d,dist = m.split()
    dist = int(dist)
    match d:
      case 'R':
        rope.right(dist)
      case 'L':
        rope.left(dist)
      case 'U':
        rope.up(dist)
      case 'D':
        rope.down(dist)

move()
print('part one:', len(rope.positions))

rope = make_rope(10)

def move10():
  for m in test2:
    d,dist = m.split()
    dist =  int(dist)
    match d:
      case 'R':
        rope.right(dist)
      case 'L':
        rope.left(dist)
      case 'U':
        rope.up(dist)
      case 'D':
        rope.down(dist)

def restore():
  rope.reset()
  rope[0].y, rope[0].x = 3, 4
  rope[1].y, rope[1].x = 2, 4
  rope[2].y, rope[2].x = 1, 3
  rope[3].y, rope[3].x = 1, 2
  rope[4].y, rope[4].x = 1, 1

# restore()
move10()
print('part two:', len(rope.positions))
