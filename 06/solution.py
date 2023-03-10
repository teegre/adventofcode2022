""" Day 06 - Tuning Trouble """

# Part one

test = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'

with open('input.txt', 'r') as f:
  inp = f.read()[:-1]

for i in range(len(inp)):
  if len(set(inp[i:i+4])) == 4:
    print('part one:', i+4)
    break

# Part two
start = i+5
for i in range(start,len(inp)):
  if len(set(inp[i:i+14])) == 14:
    print('part two:', i+14)
    break
