# 최적화
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    get = list(map(int, input().split()))
    tokens = [(get[i], i) for i in range(n)]

    srt = sorted(tokens)
    cal = 0
    lose_until = -1
    for i in range(n-1):
        cal += srt[i][0]
        if cal < srt[i+1][0]:
            lose_until = i

    ans = srt[lose_until+1:]
    leng = len(ans)
    e = []
    for i in range(leng):
        e.append(ans[i][1]+1)
    print(leng)
    e.sort()
    print(*e)


# 첫 솔루션
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     n = int(input())
#     get = list(map(int, input().split()))
#     tokens = [(get[i], i) for i in range(n)]

#     srt = sorted(tokens)
#     i = 0
#     x = 0
#     front = 0
#     while i < n:
#         num = srt[i][0]
#         howmany = 1
#         for k in range(i+1, n):
#             if num == srt[k][0]:
#                 howmany += 1
#             else:
#                 break

#         if i+howmany < n and front + num*howmany < srt[i+howmany][0]:
#             x = srt[i][0]

#         front += num*howmany
#         i += howmany

#     ans = []
#     for i in range(n):
#         if tokens[i][0] > x:
#             ans.append(tokens[i][1]+1)
#     print(len(ans))
#     print(*ans)
