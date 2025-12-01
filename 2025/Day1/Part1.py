with open("input.txt", "r") as f:
    codes = [line.strip() for line in f]
res = 0
num = 50
for n in codes:
    if n[0] == 'L': num = (num - int(n[1:])) % 100
    else: num = (num + int(n[1:])) % 100
    if not num: res += 1
print(res)