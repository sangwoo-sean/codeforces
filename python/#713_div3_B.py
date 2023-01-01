for _ in range(int(input())):
    n = int(input())
    MAP = []
    stars = []
    for r in range(n):
        line = list(input())
        for c in range(n):
            if line[c] == "*":
                stars.append([r, c])
        MAP.append(line)

    r1, c1 = stars[0][0], stars[0][1]
    r2, c2 = stars[1][0], stars[1][1]
    if c1 == c2:
        MAP[r1][c1-1] = "*"
        MAP[r2][c2-1] = "*"
    elif r1 == r2:
        MAP[r1-1][c1] = "*"
        MAP[r2-1][c2] = "*"
    else:
        MAP[r1][c2] = "*"
        MAP[r2][c1] = "*"

    for i in MAP:
        print("".join(j for j in i for i in MAP))
