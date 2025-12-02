labels = []

with open("input.txt", "r") as f:
    line = f.read().strip()
    ranges = line.split(",")

    for nums in ranges:
        start, end = nums.split("-")
        labels.append([int(start), int(end)])

res = 0
for n, m in labels:
    for i in range(n, m + 1):
        currStr = str(i)
        for k in range(1, len(currStr) // 2 + 1):
            p = currStr[:k]
            flag = 1
            for j in range(0 ,len(currStr), k):
                q = currStr[j:j+k]
                if p != q:
                    flag = 0
                    break
            if flag:
                res += i
                break
print(res)