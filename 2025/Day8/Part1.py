with open("input.txt", "r") as f:
    position = [line.strip().split(",") for line in f]

for i in range(1000):
    position[i].append(i)

distance = []
for i in range(1000):
    for j in range(i + 1, 1000):
        dist = (int(position[i][0]) - int(position[j][0])) ** 2 + (int(position[i][1]) - int(position[j][1])) ** 2 + (int(position[i][2]) - int(position[j][2])) ** 2
        distance.append([dist, position[i][-1], position[j][-1]])
distance.sort()

adj = {}
for i in range(1000):
    if distance[i][1] not in adj:
        adj[distance[i][1]] = []
    if distance[i][2] not in adj:
        adj[distance[i][2]] = []
    adj[distance[i][2]].append(distance[i][1])
    adj[distance[i][1]].append(distance[i][2])

rank, par = {}, {}
for i in range(1000):
    par[i] = i
    rank[i] = 0

def parent(n):
    p = par[n]
    while p != par[p]:
        par[p] = par[par[p]]
        p = par[p]
    return p

def union(u, v):
    pu, pv = parent(u), parent(v)
    if pu == pv:
        return
    if rank[pu] > rank[pv]:
        par[pv] = pu
    elif rank[pu] < rank[pv]:
        par[pu] = pv
    else:
        par[pv] = pu
        rank[pu] += 1

for u in adj:
    for v in adj[u]:
        union(u, v)

count = {}
for n in range(1000):
    root = parent(n)
    count[root] = count.get(root, 0) + 1

compSize = list(count.values())
compSize.sort()
print(compSize[-1] * compSize[-2] * compSize[-3])