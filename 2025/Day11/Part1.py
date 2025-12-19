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
def func(node):
    if node == "out":
       return 1
    if node in dp:
        return dp[node]
    paths = 0
    for neighbour in hashMap[node]:
       paths += func(neighbour)
    dp[node] = paths
    return paths

print(func("you"))