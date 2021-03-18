def solve(n):
    if n % 2 == 1:
        ans = [n//2, n//2, 1]
    else:
        if (n//2) % 2 == 0:
            ans = [n//2, n//4, n//4]
        else:
            ans = [n//2-1, n//2-1, 2]
    return ans


for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = solve(n-(k-3)) + [1]*(k-3)
    print(*ans)
