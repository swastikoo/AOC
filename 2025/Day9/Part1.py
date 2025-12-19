with open("input.txt", "r") as f:
    points = [line.strip().split(",") for line in f]
maxArea = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        y1, y2 = int(points[j][0]), int(points[i][0])
        x1, x2 = int(points[j][1]), int(points[i][1])
        a = abs(x1 - x2) + 1
        b = abs(y1 - y2) + 1
        maxArea = max(maxArea, a * b)
print(maxArea)