with open("input.txt", "r") as f:
    homework = [line.strip() for line in f]

operator = homework[-1].split()
res = 0
x = len(homework[0]) - 1

for i in range(len(operator) - 1, -1, -1):
    num = 0
    if operator[i] == "+":
        while num != "" and x >= 0:
            num = ""
            for j in range(4):
                if homework[j][x] != " ":
                    num += homework[j][x]
            x -= 1
            if num != "":
                res += int(num)

    else:
        prod = 1
        while num != "" and x >= 0:
            num = ""
            for j in range(4):
                if homework[j][x] != " ":
                    num += homework[j][x]
            x -= 1
            if num != "":
                prod *= int(num)
        res += prod  

print(res)