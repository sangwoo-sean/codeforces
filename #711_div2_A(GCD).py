# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a

from math import gcd

for _ in range(int(input())):
    n = int(input())
    sum_n = sum([int(i) for i in str(n)])

    while gcd(n, sum_n) == 1:
        n += 1
        sum_n = sum([int(i) for i in str(n)])
    print(n)
