import re

lines = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n")

idx = 0
monkeys = []

def turn(monkeys, i):
    orig_items = monkeys[i][0]
    monkeys[i][0] = []
    monkeys[i][-1] += len(orig_items)
    for item in orig_items:
        operation = monkeys[i][1].split(" ")
        operand = operation[-2]
        arg_s = operation[-1]
        arg = 0
        new_level = 0
        if arg_s == "old":
            arg = item
        else:
            arg = int(arg_s)
        if operand == "*":
            new_level = (item * arg) // 3
        else:
            new_level = (item + arg) // 3
        if new_level % monkeys[i][2] == 0:
            next_monkey = monkeys[i][3]
        else:
            next_monkey = monkeys[i][4]
        monkeys[next_monkey][0].append(new_level)

def round(monkeys):
    for m in range(len(monkeys)):
        turn(monkeys, m)

lines = [line.strip("\n") for line in open("p11.txt").readlines()]

while lines:
    starting_items = [int(s) for s in lines[1].split(":")[1].replace(" ", "").split(",")]
    operation = re.sub(r"\s+Operation: ", "", lines[2])
    test = int(re.sub(r"\s+Test: divisible by ", "", lines[3]))
    next_true = int(re.split("\s+", lines[4])[-1])
    next_false = int(re.split("\s+", lines[5])[-1])
    monkeys.append([starting_items, operation, test, next_true, next_false, 0])
    lines = lines[7:]

for i in range(20):
    round(monkeys)
    for m in monkeys:
        print(m[0])

inspected = [monkey[-1] for monkey in monkeys]
inspected.sort()
print(inspected)
print(inspected[-1] * inspected[-2])
