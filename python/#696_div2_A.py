# n = 6
# b = "001011"
# n = 1
# b= "0"

# n = 6
# b = "111000"

import sys
input = sys.stdin.readline
# for _ in range(int(input())):
#     n = int(input())
#     b = input().rstrip()

#     a = "1"
#     for i in range(n-1):
#         x = int(b[i]) + int(a[i])

#         if x == 2:
#             if b[i+1] == '1':
#                 a += "0"
#             else:
#                 a += "1"
#         elif x == 1:
#             if b[i+1] == '1':
#                 a += "1"
#             else:
#                 a += "0"
#         else:
#             a += "1"
#     print(a)


for _ in range(int(input())):
    n = int(input())
    b = [int(i) for i in input().rstrip()]
    ans = [None] * n
    ans[0] = 1

    for i in range(1, n):
        ans[i] = 1 #일단 1을 넣어 최대로 만듦

        if ans[i] + b[i] == ans[i-1] + b[i-1]: # 그 결과가 앞자리수의 결과랑 같다면
            ans[i] = 0

    print("".join(str(i) for i in ans))





    # ans = ''
    # s = 3 # 2를 넘는 아무 값
    # for i in b: # b의 하나씩
    #     if (int(i) + 1) != s: # 그 자리수에 1을 더한것이 // 전 자리수의 결과값과 같지 않으면
    #         ans += '1' # 1을 놓음으로써 최대를 만들고
    #         s = int(i) + 1 # 그 자리수의 결과값
    #     else: # 그 자리수에 1을 더한것이 // 전 자리수의 결과값과 같으면
    #         ans += '0' # 1을 놓지 못하므로 0을 놓아 다른 결과값을 만들어야함
    #         s = (int(i)) # 그 자리수의 결과값
    # print(ans)