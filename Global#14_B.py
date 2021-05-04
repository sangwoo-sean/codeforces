for _ in range(int(input())):
    n = int(input())

    if (n/2)**0.5 == int((n/2)**0.5) or (n/4)**0.5 == int((n/4)**0.5):
        print("YES")
    else:
        print("NO")
