for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(n//2)
    for i in range(0, n-1, 2):
        print(i+1, i+2, min(arr[i], arr[i+1]), int(1e9) + 7)
