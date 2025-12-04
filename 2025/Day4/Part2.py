with open("input.txt", "r") as f:
    grid = [list(line.strip()) for line in f]

res, row, col = 0, len(grid), len(grid[0])

x = 1
while x:
    x = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == '@':
                count = 0
                if r - 1 > -1 and grid[r - 1][c] == '@':
                    count += 1
                if r - 1 > -1 and c - 1 > -1 and grid[r - 1][c - 1] == '@':
                    count += 1
                if c - 1 > -1 and grid[r][c - 1] == '@':
                    count += 1
                if r + 1 < row and grid[r + 1][c] == '@':
                    count += 1
                if r + 1 < row and c - 1 > -1 and grid[r + 1][c - 1] == '@':
                    count += 1
                if r - 1 > -1 and c + 1 < col and grid[r - 1][c + 1] == '@':
                    count += 1
                if c + 1 < col and grid[r][c + 1] =='@':
                    count += 1
                if r + 1 < row and c + 1 < col and grid[r + 1][c + 1] == '@':
                    count += 1
                if count < 4:
                    x = 1
                    grid[r][c] = '.'
                    res += 1
print(res)