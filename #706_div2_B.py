import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    ans = len(set(s))
    if not k:
        print(ans)
        continue

    s.sort()
    s_max = s[-1]
    s_mex = n
    for i in range(n):
        if i != s[i]:
            s_mex = i
            break

    if s_mex > s_max:
        ans += k
    else:
        if math.ceil((s_max + s_mex)/2) not in s:
            ans += 1
    print(ans)
