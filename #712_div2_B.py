for i in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    ans = "YES"
    su = 0
    same = None
    for x, y in zip(a, b):
        if su == 0:
            same = x == y
        if x == "0":
            su -= 1
        else:
            su += 1

        if same != (x == y):
            ans = "NO"
            break
    if su != 0 and not same:
        ans = "NO"
    print(ans)
