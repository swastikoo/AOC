with open("input.txt", "r") as f:
    input = [line.strip() for line in f]

light, wire, joltage = [], [], []
for arr in input:
    temp = []
    i = 1
    while arr[i] != "]":
        if arr[i] == '.': temp.append(0)
        else: temp.append(1)
        i += 1
    light.append(temp)

    i += 1
    temp = []
    wire.append([])
    while arr[i] != "{":
        if arr[i] == ")":
            wire[-1].append(temp)
            temp = []
        elif arr[i] != " " and arr[i] != "(" and arr[i] != ",":
            temp.append(int(arr[i]))
        i += 1

def func(i, count, curr):
    if i == len(arr):
        if curr == res:
            return count
        return float("inf")
    best = func(i + 1, count, curr)
    for j in arr[i]:
        curr[j] ^= 1
    best = min(best, func(i + 1, count + 1, curr))
    for j in arr[i]:
        curr[j] ^= 1
    return best

total = 0
for i in range(len(light)):
    res = light[i]
    arr = wire[i]
    total += func(0, 0, [0] * len(res))
print(total)