import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    x = [0 for _ in range(n*2+1)]  # a[i]-i가 같은애들끼리 묶어서 갯수 카운팅, 음수인경우도 있기때문에 *2

    ans = 0
    for i in range(n):
        x[arr[i]-i] += 1
    for i in x:
        ans += i*(i-1)//2
    print(ans)
