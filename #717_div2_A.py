for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    i = 0
    while k > 0 and i < n-1:
        temp = min(arr[i], k)
        arr[-1] += temp
        arr[i] -= temp
        k -= temp
        i += 1

    print(*arr)
