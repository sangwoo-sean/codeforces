import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())

    t = n*(n-1)//2

    scores = [0]*n

    zeros = t % n
    ones = t // n
    k = n-1

    for i in range(n-1, 0, -1):
        for j in range(i):
            if n % 2 == 0 and i % 2 == 1 and j == 0:
                print(0, end=" ")
                continue
            if j % 2 == 0:
                print(1, end=" ")
            else:
                print(-1, end=" ")

    print()


# 홀수일때
# 0 1 2 3 4 5
# 1 x w l w l
# 2 w x w l w
# 3 l w x w l
# 4 w l w x w
# 5 l w x w x

# 짝수일때
# 0 1 2 3 4 5 6
# 1 x t w l w l
# 2 t x l w l w
# 3 w l x t w l
# 4 l w t x l w
# 5 w l w l x t
# 6 l w l w t x
