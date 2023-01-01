for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    o, e = [], []
    for i in arr:
        if i % 2:
            o.append(i)
        else:
            e.append(i)

    print(*(o+e))
