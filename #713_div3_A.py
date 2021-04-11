for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    c = set(arr)
    for i in c:
        if arr.count(i) == 1:
            print(arr.index(i)+1)
