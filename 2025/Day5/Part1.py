with open("input1.txt", "r") as f:
    ranges = [line.strip() for line in f]
    interval_temp = []
    for n in ranges:
        a, b = n.split("-")
        interval_temp.append([int(a), int(b)])

with open("input2.txt", "r") as f:
    values = [int(line.strip()) for line in f]

interval_temp.sort()
intervals = []
intervals.append([interval_temp[0][0], interval_temp[0][1]])
for start, end in interval_temp:
    if start <= intervals[-1][1]:
        intervals[-1][1] = max(intervals[-1][1], end)
    else:
        intervals.append([start, end])

res = 0
for i in values:
    if i < intervals[0][0] or i > intervals[-1][1]:
        continue
    L = 0
    R = len(intervals) - 1
    while L <= R:
        mid = (L + R) // 2
        if i < intervals[mid][0]:
            R = mid - 1
        elif i > intervals[mid][1]:
            L = mid + 1
        else:
            res += 1
            break
print(res)