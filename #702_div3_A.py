import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())

    arr = list(map(int, input().split()))

    count = 0
    for i in range(1, n):
        sml = min(arr[i-1], arr[i])
        big = max(arr[i-1], arr[i])
        while 2*sml < big:
            sml *= 2
            count += 1
    print(count)
