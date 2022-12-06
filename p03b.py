lines = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

lines = [line.strip() for line in open("p03.txt").readlines()]

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0
# how many groups of three?
groups = len(lines) // 3

for i in range(groups):
    first = set(lines[i * 3])
    second = set(lines[i * 3 + 1])
    third = set(lines[i * 3 + 2])
    common = list(first.intersection(second).intersection(third))
    priority = alpha.index(common[0]) + 1
    answer += priority

print(answer)

