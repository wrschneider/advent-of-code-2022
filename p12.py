import networkx as nx

lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

lines = [line.strip("\n") for line in open("p12.txt").readlines()]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]
start = None
end = None

g = nx.DiGraph()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        ch = lines[i][j]
        if ch == "S": 
            start = (i,j)
            ch = "a"
        if ch == "E": 
            end = (i,j)
            ch = "z"
        for d in dirs:
            i2 = i + d[0]
            j2 = j + d[1] 
            if (i2 >= 0 and j2 >= 0 and i2 < len(lines) and j2 < len(lines[i])):
                 ch2 = lines[i2][j2]
                 if ch2 == "S": ch2 = "a"
                 elif ch2 == "E": ch2 = "z"
            
                 if (ord(ch) - ord(ch2) >= -1):
                    # print(i, j, ch, i2, j2, ch2)
                    g.add_edge((i,j), (i2,j2), weight=1)

path = nx.shortest_path(g, start, end)
# print(path)
print(len(path) - 1)

sources = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S" or lines[i][j] == "a":
            sources.append((i,j))

paths = nx.multi_source_dijkstra(g, sources, end)
# print(paths)
print(paths[0])

