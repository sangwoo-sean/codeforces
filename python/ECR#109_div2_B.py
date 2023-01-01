for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    f = arr[0]
    l = arr[-1]
    if arr == sorted(arr):
        print(0)
        continue

    if f == n and l == 1:
        print(3)
    elif f != 1 and l != n:
        print(2)
    else:
        print(1)
