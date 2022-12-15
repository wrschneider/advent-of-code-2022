lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")

lines = [line.strip("\n") for line in open("p14.txt").readlines()]

grid = []

def parse_line(line):
    return [tuple(int(s) for s in point.split(",")) for point in line.split(" -> ")]

parsed = [parse_line(line) for line in lines]

min_x = min(min(pt[0] for pt in line) for line in parsed)
max_x = max(max(pt[0] for pt in line) for line in parsed)
min_y = 0
max_y = max(max(pt[1] for pt in line) for line in parsed)

print(min_x, max_x, min_y, max_y)

grid = [["."] * (max_x + 1) for i in range(max_y + 1)]
for row in parsed:
    for i in range(len(row) - 1):
        p1 = row[i]
        p2 = row[i + 1]
        print(p1, p2)
        if p1[0] == p2[0]: # vertical
            # flip 
            for j in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
                grid[j][p1[0]] = "#"
        else: # horizontal
            # flip 
            for j in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
                grid[p1[1]][j] = "#"

for r in grid:
    print("".join(r[min_x:]))

def simulate(grid):
    sand = (500, 0)
    while True:
        if sand[0] > max_x or sand[0] < min_x or sand[1] > max_y:
            # no more lines to stop
            return True
        below = grid[sand[1] + 1][sand[0]]
        if below == ".": 
            sand = (sand[0], sand[1] + 1)
            continue
        below_left = grid[sand[1] + 1][sand[0] - 1]
        if below_left == ".":
            sand = (sand[0] - 1, sand[1] + 1)
            continue
        below_right = grid[sand[1] + 1][sand[0] + 1]
        if below_right == ".":
            sand = (sand[0] + 1, sand[1] + 1)
            continue
        # can't move anymore
        # sand at rest
        grid[sand[1]][sand[0]] = "o"
        return False

i = 0
while True:
    result = simulate(grid)
    # print(i)
    # for r in grid:
    #    print("".join(r[min_x:]))
    if result:
        break
    i += 1

print(i)
