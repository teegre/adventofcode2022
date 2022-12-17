""" Day 07 : No Space Left On Device """

inp = []
with open('input.txt', 'r') as f:
  for line in f.readlines():
    inp.append(line[:-1])

class Directory:
  def __init__(self, dir_name):
    self.parent = None
    self.dir = dir_name
    self.children = []
  def add(self, *objs):
    for obj in objs:
      if isinstance(obj, (Directory, File)):
        obj.parent = self
      self.children.append(obj)
  def get(self, name):
    for child in self.children:
      if isinstance(child, Directory):
        if child.dir == name:
          return child
    return None
  @property
  def size(self):
    return sum(f.size for f in self.children)
  def __iter__(self):
    for item in self.children:
      yield item
      if isinstance(item, Directory):
        for subitem in item:
          yield subitem
  def __str__(self):
    return self.dir
  def __repr__(self):
    return f'dir: {self.dir} (size={self.size})→ {self.children}'

class File:
  def __init__(self, name, size):
    self.parent = None
    self.name = name
    self.size = int(size)
  def __str__(self):
    return self.name
  def __repr__(self):
    return f'file: {self.name} size={self.size}'

root = Directory('/')

inp.pop(0)
current = root
for line in inp:
  if line.startswith('$'): # command
    l = line.split()
    if len(l) == 3:
      _,_,d = l
      if d == '..':
        current = current.parent
      else:
        current = current.get(d)
  elif line.startswith('dir'):
    current.add(Directory(line.split()[1]))
  else:
    s,f = line.split()
    current.add(File(f,int(s)))

# Part one
total = sum(item.size if item.size <= 100000 else 0 for item in root if isinstance(item, Directory))
print('part one:', total)

# Part two
sizes = [d.size for d in root if isinstance(d, Directory) and d.size >= 30000000-(70000000-root.size)]
print('part two:', min(sizes))
