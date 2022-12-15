""" Rock Paper Scissors """

# -- part one --
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

# -- part two --
# X lose
# Y draw
# Z win

scores = []
for line in inp:
  p1,p2 = line.split()
  p1 = rps2[p1]
  match p2:
    case 'X': # lose
      g = list(rps1.keys())[list(rps1.values()).index(p1)]
      score = pts[g]
      # scores.append((p1, p2, g, score))
    case 'Y': # draw
      score = 3 + pts[p1]
      # scores.append((p1, p2, p1, score))
    case 'Z': # win
      score = 6 + pts[rps1[p1]]
      # scores.append((p1, p2, rps1[p1], score))
  scores.append(score)
print('part two:', sum(scores))
