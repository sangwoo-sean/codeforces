for _ in range(int(input())):
    a, b = map(int, input().split())

    ans = 0
    # 일반항 : a & b = k(k+2) ~ k(n+1) & (k+1) ~ n 항
    for k in range(1, 31624):
        x = a//k - 1
        y = b

        result = 0
        if k+1 <= b and k*(k+2) <= a:
            if x < y:  # n = x
                result = x - k
            else:  # n = y
                result = y - k
        else:
            break

        ans += result

    print(ans)
