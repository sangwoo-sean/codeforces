import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0]*n

    def solve(start, end):
        if start == end:
            return

        current = arr[start:end]
        mxidx = current.index(max(current))
        left = [start, start + mxidx]
        right = [start + mxidx+1, end]
        for i in range(start, end):
            if i == start + mxidx:
                continue
            ans[i] += 1

        solve(left[0], left[1])
        solve(right[0], right[1])

    solve(0, n)
    print(" ".join(str(i) for i in ans))
