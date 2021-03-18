for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    narr = [0 for _ in range(m)]
    for i in arr:
        narr[i % m] += 1

    ans = 0

    if narr[0]:
        ans += 1
        narr[0] = 0

    if m % 2 == 0 and narr[m//2]:
        ans += 1
        narr[m//2] = 0

    for i in range(1, m//2+1):
        if narr[i] and narr[m-i]:
            if narr[i] > narr[m-i]:
                narr[i] -= narr[m-i]+1
                narr[m-i] = 0
            elif narr[i] < narr[m-i]:
                narr[m-i] -= narr[i]+1
                narr[i] = 0
            else:
                narr[m-i] = 0
                narr[i] = 0
            ans += 1

    print(ans + sum(narr))
