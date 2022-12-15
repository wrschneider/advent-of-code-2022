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

row_of_interest = 2000000
no_beacons = set()
for s in sensors:
    distance = abs(s[2] - s[0]) + abs(s[3] - s[1])
    plus_or_minus_x = distance - abs(s[1] - row_of_interest)
    if plus_or_minus_x >= 0:
        for i in range(plus_or_minus_x + 1):
            if (s[0] + i, row_of_interest) != (s[2], s[3]):
                no_beacons.add(s[0] + i)
            if (s[0] - i, row_of_interest) != (s[2], s[3]):
                no_beacons.add(s[0] - i)

# print(sorted(list(no_beacons)))

print(len(no_beacons))


