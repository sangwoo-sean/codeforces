from math import log2
for _ in range(int(input())):
    n = int(input())
    print(2**int(log2(n))-1)
