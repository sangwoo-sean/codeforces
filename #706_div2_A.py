for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    i = 0
    if n % 2 == 0:
        l = n-1
    else:
        l = n
    while i < l//2:
        if s[i] == s[n-1-i]:
            i += 1
            continue
        break

    ans = "NO"
    if k <= i:
        ans = "YES"
    print(ans)
