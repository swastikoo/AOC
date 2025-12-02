labels = []

with open("input.txt", "r") as f:
    line = f.read().strip()
    ranges = line.split(",")

    for nums in ranges:
        start, end = nums.split("-")
        labels.append([int(start), int(end)])

print(labels)
res = 0
for n, m in labels:
    for i in range(n, m + 1):
        currStr = str(i)
        if len(currStr) % 2 == 0:
            j = len(currStr) // 2 - 1
            k = len(currStr) - 1
            while j >= 0 and currStr[j] == currStr[k]:
                j, k = j - 1, k - 1
            if j == -1:
                res += i
print(res)