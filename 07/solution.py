""" Day 07 : No Space Left On Device """

# Part one

inp = []
with open('input.txt', 'r') as f:
  for line in f.readlines():
    inp.append(line[:-1])

test = ['$ cd /','$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

class Tree:
  def __init__(self, dir_name):
    self.parent = None
    self.dir = dir_name
    self.children = []
  def add(self, *objs):
    for obj in objs:
      if isinstance(obj, (Tree, File)):
        obj.parent = self
      self.children.append(obj)
  def get(self, name):
    for child in self.children:
      if isinstance(child, Tree):
        if child.dir == name:
          return child
    return None
  def __str__(self):
    return self.dir
  def __repr__(self):
    return f'tree: {self.dir} → {self.children}'

class File:
  def __init__(self, name, size):
    self.parent = None
    self.name = name
    self.size = size
  def __str__(self):
    return self.name
  def __repr__(self):
    return f'file: {self.name} size={self.size}'

root = Tree('/')

test.pop(0)
current = root
for line in test:
  if line.startswith('$'): # command
    l = line.split()
    if len(l) == 3:
      _,_,d = l
      if d == '..':
        current = current.parent
      else:
        current = current.get(d)
  elif line.startswith('dir'):
    current.add(Tree(line.split()[1]))
  else:
    s,f = line.split()
    current.add(File(f,int(s)))

