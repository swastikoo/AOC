with open("input.txt", "r") as f:
    arr = [line.strip().split(":") for line in f]

hashMap = {}
for i, v in arr:
    if i not in hashMap:
        hashMap[i] = []
    k = 1
    temp = ""
    v += " "
    while k < len(v):
        if v[k] == " ":
            hashMap[i].append(temp)
            temp = ""
        else:
            temp += v[k]
        k += 1

dp = {}
def func(node, a, b):
    if node == "out":
        if a and b:
            return (1, a, b)
        return (0, a, b)
    if (node, a, b) in dp:
        return (dp[(node, a, b)], a, b)
    if node == "fft": a = 1
    if node == "dac": b = 1
    paths = 0
    for neighbour in hashMap[node]:
       x, a, b = func(neighbour, a, b)
       paths += x
    dp[(node, a, b)] = paths
    if node == "fft": a = 0
    if node == "dac": b = 0
    return (paths, a, b)

print(func("svr", 0, 0)[0])

