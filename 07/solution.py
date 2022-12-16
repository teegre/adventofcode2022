""" Day 07 : No Space Left On Device """

# Part one

inp = []
with open('input.txt', 'r') as f:
  for line in f.readlines():
    inp.append(line[:-1])

test = ['$ cd /','$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

class Tree:
  def __init__(self, root):
    self.root = root
    self.children = []
    self.nodes = []
  def add(self, obj):
    self.children.append(obj)
  def get_all_nodes(self):
    self.nodes.append(self.root)
    for child in self.children:
      self.nodes.append(child.data)
      if child.get_child_nodes(self.nodes):
        child.get_child_nodes(self.nodes)
  def __str__(self):
    return self.root
  def __repr__(self):
    return f'tree: {self.root} → {self.children}'

class Node:
  def __init__(self, data):
    self.data = data
    self.children = []
  def add(self, obj):
    self.children.append(obj)
  def get_child_nodes(self, tree):
    for child in self.children:
      if child.children(tree):
        tree.append(child.data)
      else:
        tree.append(child.data)
  def __str__(self):
    return self.data
  def __repr__(self):
    return f'node: {self.data} → {self.children}'

tree = Tree('/')

for line in test:
  if line.startswith('$ cd'):
    _,_,dir = line.split()
    tree[dir] = {'.': []}

