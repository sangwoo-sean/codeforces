n, k = 4, 3


import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())

    a = [i for i in range(1, k+1)]
    for i in range(k-1, 0, -1):
        if len(a) < n:
            a.append(i)
        else:
            break

    answer = []
    for i in range(k, k-(n-k)-1, -1):
        answer.append(i)
    rest = []
    for i in range(1, min(answer)):
        rest.append(i)
    answer = rest + answer
    print(" ".join(str(i) for i in answer))