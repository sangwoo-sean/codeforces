from math import ceil
for _ in range(int(input())):
    r, b, d = map(int, input().split())
    if r > b:
        r, b = b, r
    n = ceil(b / r) - 1
    if d < n:
        print("NO")
    else:
        print("YES")
