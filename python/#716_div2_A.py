for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = "NO"
    for i in range(n):
        if int(arr[i]**0.5)**2 != arr[i]:
            ans = "YES"
            break

    print(ans)
