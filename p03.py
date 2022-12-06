lines = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")

lines = [line.strip() for line in open("p03.txt").readlines()]

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0
for line in lines:
    half = len(line) // 2
    first = set(line[0:half])
    second = set(line[half:])
    common = list(first.intersection(second))
    priority = alpha.index(common[0]) + 1
    answer += priority

print(answer)

