from functools import cmp_to_key

lines = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".split("\n")

lines = [line.strip("\n") for line in open("p13.txt").readlines()]

def compare(left, right):
    for i in range(len(left)):
        if i >= len(right):
            return False
        l = left[i]
        r = right[i]
        if type(l) == int and type(r) == int:
            if l < r: return True
            elif l > r: return False
            else: continue
        if type(l) == int: l = [l]
        if type(r) == int: r = [r]
        return compare(l, r) # recurse

    # left ran out first
    return True

def comparator(left, right):
    if compare(left, right): return -1
    else: return +1

packets = [eval(line) for line in lines if line]

total = 0
index = 1
while lines:
    left = eval(lines[0])
    right = eval(lines[1])
    if compare(left, right):
        total += index
    
    lines = lines[3:]
    index += 1

print(total)

# part b
packets.append([[2]])
packets.append([[6]])
packets2 = sorted(packets, key=cmp_to_key(comparator))
print(packets2)

i1 = packets2.index([[2]]) + 1
i2 = packets2.index([[6]]) + 1
print(i1 * i2)