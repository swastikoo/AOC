from functools import lru_cache

with open("input.txt", "r") as f:
    joltages = [line.strip() for line in f]

@lru_cache(None)
def findMax(i, k):
    if k == 0:
        return ''
    if i == n:
        return None
    if n - i < k:
        return None
    a = findMax(i + 1, k)
    b = findMax(i + 1, k - 1)
    c = None
    if b is not None:
        c = joltage[i] + b
    if a is None:
        return c
    if c is None:
        return a
    return max(a, c)

res = 0
for joltage in joltages:
    n = len(joltage)
    findMax.cache_clear()
    res += int(findMax(0, 12))
print(res)