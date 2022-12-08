lines = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")

lines = [line.strip("\n") for line in open("p07.txt").readlines()]

pwd = ()
sizes = dict()
recursive_sizes = {tuple(): 0}

for line in lines:
    if line == "$ ls":
        # start listing
        sizes[pwd] = 0
    elif line.startswith("$ cd"):
        dir = line[5:]
        if dir == "/": pwd = ()
        elif dir == "..": pwd = pwd[0:-1]
        else:
            pwd = pwd + (dir,)
            if pwd not in recursive_sizes:
                recursive_sizes[pwd] = 0

    else: # not command, must be in listing
        (sz, name) = line.split(" ")
        if sz == "dir": pass
        else: 
            sizes[pwd] += int(sz)
            for i in range(len(pwd) + 1):
                recursive_sizes[pwd[0:i]] += int(sz)

for sz in sizes.keys(): print(sz, sizes[sz])
tot = 0

free_space = 70000000 - recursive_sizes[tuple()]
needed_space = 30000000 - free_space

for sz in recursive_sizes.keys():
    print(sz, recursive_sizes[sz])
    if recursive_sizes[sz] <= 100000: tot += recursive_sizes[sz]

print(tot) # part 1
sz = min(v for v in recursive_sizes.values() if v >= needed_space)
print(sz) # part 2
    


    
