for _ in range(int(input())):
    n, k1, k2 = map(int, input().split())
    w, b = map(int, input().split())

    wmin = min(k1, k2)
    bmin = min(n-k1, n-k2)
    gap = abs(k1-k2)

    w -= wmin + gap//2
    b -= bmin + gap//2

    if w <= 0 and b <= 0:
        print("YES")
    else:
        print("NO")
