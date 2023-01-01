for _ in range(int(input())):
    a, b = map(int, input().split())
    if b == 1:
        print("NO")
        continue
    print("YES")
    print(a, a*b, a*(b+1))
