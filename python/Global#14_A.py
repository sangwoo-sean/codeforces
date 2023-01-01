for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr) == x:
        print("NO")
        continue
    print("YES")
    s = 0
    for i in range(n):
        s += arr[i]
        if s == x:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(*arr)
