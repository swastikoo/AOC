with open("input.txt", "r") as f: grid = [line.strip() for line in f]
rows, cols = len(grid), len(grid[0])
for i in range(cols):
    if grid[0][i] == "S": j = i
dp = {}
def find(i, j):
    if j < 0 or j == cols: return 0
    while i < rows and grid[i][j] != "^": i += 1
    if i == rows: return 1
    if (i, j) in dp: return dp[(i, j)]
    dp[(i, j)] = find(i, j - 1) + find(i, j + 1)
    return dp[(i, j)]
print(find(0, j))