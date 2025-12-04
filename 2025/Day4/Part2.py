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
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
                    if 0 <= r + dr < row and 0 <= c + dc < col and grid[r + dr][c + dc] == '@':
                        count += 1
                if count < 4:
                    x = 1
                    grid[r][c] = '.'
                    res += 1
print(res)