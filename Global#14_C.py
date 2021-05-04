import heapq
for _ in range(int(input())):
    n, m, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = []

    tower = [(0, i) for i in range(1, m+1)]

    for i in arr:
        stack, idx = heapq.heappop(tower)
        ans.append(idx)
        heapq.heappush(tower, (stack+i, idx))

    print("YES")
    print(*ans)
