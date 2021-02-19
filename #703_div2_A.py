# 다른사람 솔루션
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    ans = "YES"
    least = 0
    cal = 0
    for i in range(n):
        least += i
        cal += h[i]
        if least > cal:
            ans = "NO"
            break

    print(ans)


# 첫솔루션
    # for i in range(n-1):
    #     if h[i] > i:
    #         rest = h[i] - i
    #         h[i] -= rest
    #         h[i+1] += rest

    # for i in range(n-1):
    #     if h[i] >= h[i+1]:
    #         ans = "NO"
    #         break
    # print(ans)
