for _ in range(int(input())):
    p, a, b, c = map(int, input().split())

    if p % a == 0 or p % b == 0 or p % c == 0:
        print(0)
        continue

    a = a - (p % a)
    b = b - (p % b)
    c = c - (p % c)

    # 이렇게하면 위의 조건문을 없앨수있음
    # a = a-(p % a) % a
    # b = b-(p % b) % b
    # c = c-(p % c) % c

    print(min(a, b, c))
