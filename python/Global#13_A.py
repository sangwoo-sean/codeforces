import sys
input = sys.stdin.readline

n, q = map(int, input().split())

arr = list(map(int, input().split()))

ones = arr.count(1)
for _ in range(q):
    t, x = map(int, input().split())

    if t == 1:
        if arr[x-1] == 1:
            arr[x-1] = 0
            ones -= 1
        else:
            arr[x-1] = 1
            ones += 1
    else:
        if ones < x:
            print(0)
        else:
            print(1)
