with open("input.txt", "r") as f:
    codes = [line.strip() for line in f]

num, res = 50, 0
for code in codes:
    r = int(code[1:])
    last = r % 100
    prev = num
    if code[0] == 'L':
        num -= last
        if prev > 0 and num <= 0:
            res += 1
    else:
        num += last
        if prev < 100 and num >= 100:
            res += 1    
    num %= 100
    r -= last
    if r > 0:
        res += r // 100
print(res)