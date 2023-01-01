import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    heros = list(map(int, input().split()))

    heros.sort()

    small = heros[0]
    count = heros.count(small)

    print(n - count)
