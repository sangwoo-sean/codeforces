from collections import deque

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    minq, maxq = deque([]), deque([])
    minarr, maxarr = [], []

    maxSeen = 1
    for i in range(n):
        same = arr[i] == maxSeen  # max값과 같은값인지 아닌지 판별

        while maxSeen <= arr[i]:  # 안나온값부터 최대값까지 큐에 넣어주기
            minq.append(maxSeen)
            maxq.append(maxSeen)
            maxSeen += 1

        if same:  # 같은값이면 큐에서 적절히 넣어주기
            minarr.append(minq.popleft())
            maxarr.append(maxq.pop())
        else:  # 다른값이면 그값을 바로 넣기
            minarr.append(minq.pop())
            maxarr.append(maxq.pop())

    print(*minarr)
    print(*maxarr)
