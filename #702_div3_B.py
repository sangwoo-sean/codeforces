from math import ceil
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    cs = [0, 0, 0]
    for i in arr:
        cs[i % 3] += 1

    ans = 0
    sm = sum(cs)
    mean = ceil(sm / 3)  # 맞춰야되는 수
    i = 0
    while not cs[0] == cs[1] == cs[2]:
        if cs.count(mean) == 2:
            ans += mean - min(cs)
            break

        if cs[i] > mean:
            gap = cs[i]-mean
            ans += gap
            cs[i] -= gap
            cs[(i+1) % 3] += gap

        i = (i+1) % 3

    print(ans)


# 첫솔루션
# from math import ceil
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))

#     c0, c1, c2 = 0, 0, 0

#     for i in arr:
#         if i % 3 == 0:
#             c0 += 1
#         elif i % 3 == 1:
#             c1 += 1
#         else:
#             c2 += 1

#     cs = [c0, c1, c2]
#     ans = 0
#     sm = sum(cs)
#     mean = ceil(sm / 3)  # 맞춰야되는 수
#     i = 0
#     while not cs[0] == cs[1] == cs[2]:
#         if cs.count(mean) == 2:
#             ans += mean - min(cs)
#             break

#         if cs[i] > mean:
#             gap = cs[i]-mean
#             ans += gap
#             cs[i] -= gap
#             cs[(i+1) % 3] += gap

#         i = (i+1) % 3

#     print(ans)
