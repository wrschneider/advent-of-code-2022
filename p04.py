lines = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")

lines = [line.strip() for line in open("p04.txt").readlines()]

def overlap(r1, r2):
    return (
        (r1[0] >= r2[0] and r1[0] <= r2[1])
        or
        (r2[0] >= r1[0] and r2[0] <= r1[1])
        or
        (r1[0] >= r2[0] and r1[1] <= r2[1])
        or
        (r2[0] >= r1[0] and r2[1] <= r1[1])
    )


def fully_contained(r1, r2):
    return (
        (r1[0] >= r2[0] and r1[1] <= r2[1])
        or
        (r2[0] >= r1[0] and r2[1] <= r1[1])
    )

ctr = 0
for line in lines:
    s = line.split(",")
    rs = [[int(n) for n in s2.split("-")] for s2 in s]
    # if fully_contained(rs[0], rs[1]):
    if overlap(rs[0], rs[1]):
        ctr += 1
print(ctr)




