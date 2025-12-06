with open("input.txt", "r") as f:
    homework = [line.strip().split() for line in f]

row, col = len(homework), len(homework[0])

print(row, col)
res = 0
for i in range(col):
    addition, product = 0, 1
    if homework[-1][i] == "+":
        for j in range(row - 1):
            addition += int(homework[j][i])
        res += addition
    else:
        for j in range(row - 1):
            product *= int(homework[j][i]) 
        res += product      
print(res)