import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    # li = [int(i) for i in input().split()]
    bigs = [0]
    current_max = li[0]
    for i in range(1, n):
        if li[i] > current_max:
            current_max = li[i]
            bigs.append(i)

    bigs = reversed(bigs)
    ans = []
    for start in bigs:
        for j in range(start, n):
            ans.append(li[j])
        n = start
    print(*ans)
