from collections import deque
from math import floor


def op1(a, b):
    a = floor(a/b)
    return a, b


def op2(a, b):
    b = b+1
    return a, b


def solve():
    while q:
        x, y, n = q.popleft()

        x1, y1 = op1(x, y)
        x2, y2 = op2(x, y)
        q.append([x1, y1, n+1])
        q.append([x2, y2, n+1])
        if x1 == 0 or x2 == 0:
            return


for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append([a, b, 0])

    solve()
    print(q[-1][2])
