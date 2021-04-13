import sys
input = sys.stdin.readline
MOD = 1000000007
dp = [1 for _ in range(200011)]
for i in range(10, 200011):  # 0을 i번 연산한 값의 자릿수 구하기
    dp[i] = (dp[i-10]+dp[i-9]) % MOD

for i in range(25):
    print(dp[i], end=" ")

for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = 0
    while n:
        ans += dp[m + n % 10]
        n //= 10
        ans %= MOD
    print(ans)
