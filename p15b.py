import re

lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")

lines = [line.strip("\n") for line in open("p15.txt").readlines()]

pattern = r"Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)"
sensors = [tuple(int(s) for s in re.match(pattern, line).groups()) for line in lines]

eliminated_ranges = []
max_x = 4000000 + 1
for i in range(0, max_x):
    eliminated_ranges.append([])

# this is slow - could probably handle 2d ranges via change of coordinates
# but faster to run than to figure it out :-)
for s in sensors:
    distance = abs(s[2] - s[0]) + abs(s[3] - s[1])
    for row in range(max(0, s[1] - distance), min(s[1] + distance, max_x)):
        if row % 1000 == 0: print(s, distance, row)
        delta_x = distance - abs(s[1] - row)
        eliminated_ranges[row].append((max(0, s[0] - delta_x), min(max_x, s[0] + delta_x)))

found = False
for i in range(len(eliminated_ranges)):
    if i % 1000: print (i)
    if found: break
    row = eliminated_ranges[i]
    row.sort()
#    print(row)
    rng = row[0]
    for j in range(1, len(row)):
        if row[j][0] > rng[1] + 1: # fully-closed/inclusive ranges
            print(rng[1] + 1, i)
            print((rng[1] + 1) * (max_x - 1) , i)
            found = True
            break
        if row[j][1] > rng[1]:
            rng = (rng[0], row[j][1])

