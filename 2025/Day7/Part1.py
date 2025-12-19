with open("input.txt", "r") as f: grid = [line.strip() for line in f]

rows, cols = len(grid), len(grid[0])
laser = set()

for i in range(cols):
    if grid[0][i] == "S": laser.add(i)

split = 0
for i in range(1, rows):
    for j in range(cols):
        if grid[i][j] == "^" and j in laser:
            split += 1
            if j - 1 >= 0 and j - 1 not in laser: laser.add(j - 1)
            if j + 1 < cols and j + 1 not in laser: laser.add(j + 1)
            laser.remove(j)
print(split)
