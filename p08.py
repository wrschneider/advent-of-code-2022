lines = """30373
25512
65332
33549
35390""".split("\n")

lines = [line.strip("\n") for line in open("p08.txt").readlines()]

grid = [[int(s) for s in line] for line in lines]
h = len(grid)
w = len(grid[0])
rotated = [[grid[j][i] for j in range(h)] for i in range(w)]

def is_visible(r, c):
    val = grid[r][c]
    row = grid[r]
    col = rotated[c]
    return (val > max(row[0:c] or [-1]) or val > max(row[c+1:] or [-1])
        or val > max(col[0:r] or [-1]) or val > max(col[r+1:] or [-1])
    )

def scenic_score(r, c):
    val = grid[r][c]
    row = grid[r]
    col = rotated[c]

    left = 0
    right = 0
    up = 0
    down = 0
    for i in range(c - 1, -1, -1):
        left += 1
        if row[i] >= val: break
    for i in range(c + 1, len(row)):
        right += 1
        if row[i] >= val: break
    for i in range(r - 1, -1, -1):
        up += 1
        if col[i] >= val: break
    for i in range(r + 1, len(col)):
        down += 1
        if col[i] >= val: break
    return left * right * up * down

ctr = 0
max_scenic = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if is_visible(i, j): ctr += 1
        score = scenic_score(i, j)
        if score > max_scenic: max_scenic = score

print(ctr)
print(max_scenic)


