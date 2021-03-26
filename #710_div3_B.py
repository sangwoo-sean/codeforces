for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())

    stars = []
    for i in range(n):
        if s[i] == "*":
            stars.append(i)

    s[stars[0]] = "x"
    s[stars[-1]] = "x"
    i = 0
    j = 1
    while j < len(stars)-1:
        if stars[j] - stars[i] < k:
            if stars[j+1] - stars[i] <= k:
                j += 1
                continue
        s[stars[j]] = "x"
        i = j
        j = i+1

    print(s.count('x'))
