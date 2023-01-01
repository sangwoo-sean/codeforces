from math import ceil
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())

    if n % 2 == 0:
        ans = k % n
    else:
        ans = (k + ceil(k / (n//2))-1) % n

    if ans == 0:
        print(n)
    else:
        print(ans)
