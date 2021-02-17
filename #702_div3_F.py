from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    counter = Counter(arr)
    counts = counter.values()
    keys = set(counts)

    result = []
    for i in keys:
        x = 0
        for j in counts:
            if j > i:
                x += j-i
            elif j < i:
                x += j
        result.append(x)

    print(min(result))
