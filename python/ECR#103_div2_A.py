from math import ceil
#정답해설
for _ in range(int(input())):
    n, k = map(int, input().split())
    k = ceil(n/k)*k # k가 n 보다 작으면 n보다 큰 k의 배수로 만들어줌 / 아닐시 k는 그대로 (ceil(n/k))가 1이므로
    ans = ceil(k/n) # 각 칸에 k//n 을 채우면서 만약 수가 남는다면 +1을 해줄것
    print(ans)




# my solution

# for _ in range(int(input())):
#     n, k = map(int, input().split())

#     m = k // n
#     r = k % n

#     if n <= k:
#         if r == 0:
#             ans = m
#         else:
#             ans = m + 1
#     else:
#         if n % k == 0:
#             ans = 1
#         else:
#             ans = 2

#     print(ans)
