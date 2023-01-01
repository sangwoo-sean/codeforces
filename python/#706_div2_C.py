import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())

    miners = []
    diamonds = []
    for _ in range(2*n):
        x, y = map(int, input().split())
        if x == 0:
            miners.append(abs(y))
        elif y == 0:
            diamonds.append(abs(x))

    miners.sort()
    diamonds.sort()
    ans = 0
    for i in range(n):
        ans += (miners[i]**2 + diamonds[i]**2)**0.5

    print(ans)
