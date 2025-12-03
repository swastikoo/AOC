with open("input.txt", "r") as f:
    joltages = [line.strip() for line in f]

res = 0
for joltage in joltages:
    idx, num1 = 0, joltage[0]
    for i, n in enumerate(joltage):
        if n > num1: num1, idx = n, i

    if idx == len(joltage) - 1:
        num2 = joltage[0]
        for i in range(len(joltage) - 1):
            if joltage[i] > num2: num2 = joltage[i]
        res += int(num2 + num1)
    else:
        num2 = joltage[idx + 1]
        for i in range(idx + 1, len(joltage)):
            if joltage[i] > num2: num2 = joltage[i]
        res += int(num1 + num2)
print(res)