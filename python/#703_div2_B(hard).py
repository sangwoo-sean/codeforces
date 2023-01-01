import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())

    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    if n % 2 == 1:  # 홀수개인경우, 하나의 점만 존재
        ans = 1
    else:  # 짝수개인 경우, 중간값 사이에있는 모든 값들이 가능
        xs.sort()
        ys.sort()
        ans = (xs[n//2] - xs[n//2 - 1] + 1) * (ys[n//2] - ys[n//2 - 1] + 1)

    print(ans)
