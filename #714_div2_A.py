from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())

    if k > ceil(n/2)-1:
        print(-1)
        continue

    ans = [1]
    count = k
    print(count)
    i = 1
    while count > 0:
        ans.append(i+k+1)
        ans.append(i+1)
        count = -1
        i += 1
        print(count, i)
    ans += [j for j in range(i+k+1, n+1)]
    print(*ans)