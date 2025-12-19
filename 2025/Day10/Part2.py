with open("temp.txt", "r") as f:
    input = [line.strip() for line in f]

light, wire, joltage = [], [], []
for arr in input:
    i = 1
    while arr[i] != "]":
        i += 1
    i += 1
    temp = []
    wire.append([])
    while arr[i] != "{":
        if arr[i] == ")":
            wire[-1].append(temp)
            temp = []
        elif arr[i] != " " and arr[i] != "(" and arr[i] != ",":
            temp.append(int(arr[i]))
        i += 1
    i += 1
    temp = ""
    while arr[i] != "}":
        temp += arr[i]
        i += 1
    joltage.append(temp.split(","))

print(wire)
print(joltage)