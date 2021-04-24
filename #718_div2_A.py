for _ in range(int(input())):
    n = int(input())
    x = int(n/2050)
    if not (x*2050 == n):
        print(-1)
        continue
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10

    print(ans)
