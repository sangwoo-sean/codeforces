from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())

    ans = [i for i in range(ceil(k/2), k)]+[i for i in range(k+1, n+1)]
    print(len(ans))
    if len(ans):
        print(*ans)
    else:
        print()
