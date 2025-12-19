with open("input.txt", "r") as f:
    position = [line.strip().split(",") for line in f]

i_to_pos = {}
for i in range(1000):
    position[i].append(i)
    i_to_pos[i] = position[i]

distance = []
for i in range(1000):
    for j in range(i + 1, 1000):
        dist = (int(position[i][0]) - int(position[j][0])) ** 2 + (int(position[i][1]) - int(position[j][1])) ** 2 + (int(position[i][2]) - int(position[j][2])) ** 2
        distance.append([dist, position[i][-1], position[j][-1]])
distance.sort()

par, rank = {}, {}

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
    elif rank[pv] > rank[pu]:
        par[pu] = pv
    else:
        par[pu] = pv
        rank[pv] += 1

for i in range(len(distance)):
    if parent(distance[i][1]) != parent(distance[i][2]):
        res = int(i_to_pos[distance[i][1]][0]) * int(i_to_pos[distance[i][2]][0])
        union(distance[i][1], distance[i][2])
print(res)
