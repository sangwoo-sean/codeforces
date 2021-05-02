for _ in range(int(input())):
    n, m, k = map(int, input().split())
    if k == n*m-1:
        print("YES")
    else:
        print("NO")
