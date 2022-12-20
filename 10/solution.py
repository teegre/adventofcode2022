""" Day 10: Cathode-Ray Tube """

from copy import deepcopy

test = [
    'addx 15', 'addx -11', 'addx 6', 'addx -3', 'addx 5',
    'addx -1', 'addx -8', 'addx 13', 'addx 4', 'noop',
    'addx -1', 'addx 5', 'addx -1', 'addx 5', 'addx -1',
    'addx 5', 'addx -1', 'addx 5', 'addx -1', 'addx -35',
    'addx 1', 'addx 24', 'addx -19', 'addx 1', 'addx 16',
    'addx -11', 'noop', 'noop', 'addx 21', 'addx -15',
    'noop', 'noop', 'addx -3', 'addx 9', 'addx 1',
    'addx -3', 'addx 8', 'addx 1', 'addx 5', 'noop',
    'noop', 'noop', 'noop', 'noop', 'addx -36',
    'noop', 'addx 1', 'addx 7', 'noop', 'noop',
    'noop', 'addx 2', 'addx 6', 'noop', 'noop',
    'noop', 'noop', 'noop', 'addx 1', 'noop',
    'noop', 'addx 7', 'addx 1', 'noop', 'addx -13',
    'addx 13', 'addx 7', 'noop', 'addx 1', 'addx -33',
    'noop', 'noop', 'noop', 'addx 2', 'noop',
    'noop', 'noop', 'addx 8', 'noop', 'addx -1',
    'addx 2', 'addx 1', 'noop', 'addx 17', 'addx -9',
    'addx 1', 'addx 1', 'addx -3', 'addx 11', 'noop',
    'noop', 'addx 1', 'noop', 'addx 1', 'noop',
    'noop', 'addx -13', 'addx -19', 'addx 1', 'addx 3',
    'addx 26', 'addx -30', 'addx 12', 'addx -1', 'addx 3',
    'addx 1', 'noop', 'noop', 'noop', 'addx -9',
    'addx 18', 'addx 1', 'addx 2', 'noop', 'noop',
    'addx 9', 'noop', 'noop', 'noop', 'addx -1',
    'addx 2', 'addx -37', 'addx 1', 'addx 3', 'noop',
    'addx 15', 'addx -21', 'addx 22', 'addx -6', 'addx 1',
    'noop', 'addx 2', 'addx 1', 'noop', 'addx -10',
    'noop', 'noop', 'addx 20', 'addx 1', 'addx 2',
    'addx 2', 'addx -6', 'addx -11', 'noop', 'noop',
    'noop',
]

class CPU:
  """ A CPU simulator... """
  def __init__(self, instructions):
    self.cycle = 1
    self.register = 1
    self.instructions_copy = instructions
    self.instructions = deepcopy(self.instructions_copy)
    self.wait = {} # {target_cycle: (func, value)}
  def addx(self, value): # Takes 2 cycles to complete.
    """ Add value to register. """
    self.register += int(value)
    # print(f'addx @ cycle {self.cycle} with value {value}')
  def noop(self, value=None): # Takes 1 cycle to complete.
    """ Does nothing. """
    # print(f'noop @ cycle {self.cycle}')
  def forward(self):
    """ 1 cycle + read next instuction + execute awaiting instruction. """
    if not self.wait and not self.instructions:
      # Nothing to do.
      self.cycle += 1
      return
    # Execute awaiting command if any...
    command = self.wait.pop(self.cycle, None)
    if command:
      cmd, value = command
    else:
      cmd, value = None, None
    if cmd:
      cmd(value)
    # Get instruction if any...
    try:
      instruction = self.instructions.pop(0).split()
    except IndexError:
      instruction = [None]
    if len(instruction) == 2:
      cmd, value = instruction
    else:
      cmd = instruction[0]
      value = None
    if cmd == 'noop':
      self.noop(value)
    # Add awaiting command.
    elif cmd == 'addx':
      next_inst = min(self.wait.keys()) if self.wait else 0
      self.wait[self.cycle+next_inst+2] = (self.addx, value)
    self.cycle += 1
  def jump(self, to_cycle):
    """ Jump to cycle """
    if to_cycle <= self.cycle:
      self.reset()
    while self.cycle < to_cycle:
      self.forward()
  @property
  def signal_strength(self):
    """ Cycle number multiplied by the value of the register. """
    return self.cycle * self.register
  def reset(self):
    """ Reset CPU """
    self.cycle = 1
    self.register = 1
    self.wait = {}
    self.instructions = deepcopy(self.instructions_copy)
  @property
  def state(self):
    """ Display CPU state """
    if self.instructions:
      inst = self.instructions[0]
    else:
      inst = 'na'
    if self.wait:
      item = next(iter(self.wait.items()))
      cmd, value = item[1][0].__name__, item[1][1]
      due = item[0]
    else:
      cmd, value, due = 'na','na','na'
    return f'cycle={self.cycle-1} reg={self.register} next={inst} awaiting={cmd}({value})→{due}'
  def __repr__(self):
    return f'cpu: cycle={self.cycle-1} reg={self.register} inst={len(self.instructions)} aw={len(self.wait)}'

cycle = 20
max_cycle = 221
cpu = CPU(test)
while cpu.cycle <= max_cycle:
  cpu.forward()
  if cpu.cycle-1 == cycle:
    cycle += 40
    print(cpu.state, cpu.signal_strength)
