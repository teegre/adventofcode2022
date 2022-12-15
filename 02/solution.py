""" -- part one --- """

# Column 1: opponent | Column 2: player
#
# A == X == Rock     (1 pt)
# B == Y == Paper    (2 pts)
# C == Z == Scissors (6 pts)
#
# Win: 6 pts
# Draw: 3 pts
# Lose: 0 pts

rps2 = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
rps1 = { 'X': 'Y', 'Y': 'Z', 'Z': 'X' }
pts = { 'X': 1, 'Y': 2, 'Z': 3 }
scores = []
with open('input.txt', 'r') as f:
  inp = [line[:-1] for line in f.readlines()]
for line in inp:
  p1,p2 = line.split()
  p1 = rps2[p1]
  score = 3 if p1 == p2 else 6 if rps1[p1] == p2 else 0
  score += pts[p2]
  scores.append(score)
print('part one:', sum(scores))
