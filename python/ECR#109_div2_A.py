from math import gcd

for _ in range(int(input())):
    n = int(input())
    print(100//gcd(n, 100-n))
