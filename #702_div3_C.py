# dp를 이용한 문제풀이
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())

    i = 0
    ans = "NO"
    dp = {}
    while i**3 < x:
        rest = x - i**3
        if rest in dp:
            ans = "YES"
            break
        i += 1
        dp[i**3] = 1

    print(ans)

# 최적화 첫 솔루션
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     x = int(input())

#     i = 1
#     ans = "NO"
#     while i**3 < x:
#         rest = x - i**3
#         if int(round(rest**(1/3)))**3 == rest:
#             ans = "YES"
#             break
#         i += 1

#     print(ans)


# 첫 솔루션
# import sys
# input = sys.stdin.readline
# for _ in range(int(input())):
#     x = int(input())

#     for i in range(1, 10001):
#         if i**3 >= x:
#             p = i-1
#             break
#     valid = False
#     for i in range(1, p+1):
#         rest = x - i**3
#         restp = int(round(rest**(1/3)))
#         if restp**3 == rest:
#             valid = True
#             break

#     if valid:
#         print("YES")
#     else:
#         print("NO")
