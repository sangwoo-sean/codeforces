import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    a = n // 2020 # 2020이 몇개나오는지
    b = n % 2020 # 2020 다쓰고 남는수가 a보다 작으면, a의수를 2021로 바꾸면 채울수있음 
    if a >= b:
        print('YES')
    else:
        print("NO")


