import re

lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".split("\n")

# lines = [line.strip("\n") for line in open("p05.txt").readlines()]

top = []
lst = []
for line in lines:
    if len(line) == 0:
        top = lst
        lst = []
    else:
        lst.append(line)

moves = lst

top.reverse()
num_stacks = max(int(i) for i in re.split(r"\s+", top[0]) if i)
stacks = [list() for i in range(num_stacks)]

print(num_stacks)

for line in top[1:]:
    for i in range(len(stacks)):
        print(line)
        ch = line[i * 4 + 1]
        if ch != ' ': stacks[i].append(ch)

for st in stacks:
    print(st)

for move in moves:
    (n, frm, to) = re.match(r"move (\d+) from (\d+) to (\d+)", move).groups()
    # problem uses 1 based indexes
    from_idx = int(frm) - 1
    to_idx = int(to) - 1
    # probably a better way to do this
    slice = stacks[from_idx][-int(n):]
    stacks[from_idx] = stacks[from_idx][0:-int(n)]
    for elt in slice: stacks[to_idx].append(elt)

for st in stacks:
    print(st)

print("".join(st[-1] for st in stacks))




