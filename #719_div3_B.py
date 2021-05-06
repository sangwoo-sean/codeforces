import sys
input = sys.stdin.readline


# another sol
for _ in range(int(input())):
    n = int(input())
    s = 1
    ans = 0
    while n >= s:
        ans += min(9, n//s)
        s = s*10 + 1
    print(ans)


# my sol
# for _ in range(int(input())):
#     n = int(input())

#     z = 0
#     count = 0
#     run = True
#     while run:
#         for i in range(1, 10):
#             for j in range(z):
#                 i = i*10 + i % 10
#             if n < i:
#                 run = False
#                 break
#             count += 1
#         z += 1

#     print(count)
