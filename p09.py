lines = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

lines = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")

lines = [line.strip("\n") for line in open("p09.txt").readlines()]

def sign(x):
    if x == 0: return 0
    elif x > 0: return 1
    else: return -1

def execute_step(rope, dir):
    # move head
    (hx, hy) = rope[0]
    if dir == 'U': h = (hx, hy + 1)
    elif dir == 'D': h = (hx, hy - 1)
    elif dir == 'L': h = (hx - 1, hy)
    elif dir == 'R': h = (hx + 1, hy)
    rope[0] = h

    # move each knot one at a time
    for i in range(1, len(rope)):
        (hx, hy) = rope[i - 1]
        (tx, ty) = rope[i]
        if abs(hx - tx) > 1 and abs(hy - ty) > 1:
            # Sample data worked without this case!
            rope[i] = (hx + sign(tx - hx), hy + sign(ty - hy))
        elif abs(hy - ty) > 1:
            rope[i] = (hx, hy + sign(ty - hy))
        elif abs(hx - tx) > 1:
            rope[i] = (hx + sign(tx - hx), hy)

def execute_line(s, rope, visited: set):
    (dir, n) = s.split(" ")
    for i in range(int(n)):
        execute_step(rope, dir)
        visited.add(rope[-1])

rope_len = 10
rope = [(0, 0)] * rope_len

visited = set()
visited.add((0,0))
for line in lines:
    execute_line(line, rope, visited)

print (len(visited))