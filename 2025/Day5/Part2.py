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
for start, end in intervals:
    res += (end - start + 1)
print(res)