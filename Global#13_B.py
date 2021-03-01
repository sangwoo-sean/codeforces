for _ in range(int(input())):
    n, u, v = map(int, input().split())

    obs = list(map(int, input().split()))

    first_e = obs[0]

    if obs.count(first_e) == n:
        ans = min(u + v, 2*v)
    else:
        ans = min(u, v)

    for i in range(n-1):
        gap = abs(obs[i+1] - obs[i])
        if gap > 1:
            ans = 0
            break
    print(ans)
