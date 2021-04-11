for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    s = sum(arr[:-2])
    if s == arr[-2]:
        print(*arr[:-2])
        continue

    s += arr[-2]
    ans = [-1]
    for i in range(n+1):
        if s - arr[i] == arr[-1]:
            ans = arr[:i]+arr[i+1:-1]
            break
    print(*ans)
