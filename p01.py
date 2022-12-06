s = [line.strip() for line in open("p01.txt").readlines()]

def elf_generator(lines):
    cals = 0
    for s in lines:
        if len(s) > 0:
            cals += int(s)
        else:
            yield cals
            cals = 0
    yield cals

elf_cals = [elf for elf in elf_generator(s)]
elf_cals.sort()
print(elf_cals[-3:])
print(sum(elf_cals[-3:]))

