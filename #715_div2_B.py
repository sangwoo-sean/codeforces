for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    ans = "YES"
    for i in s:
        if i == 'T':
            c += 1
        else:
            c -= 1

        if c > n//3 or c < 0:
            ans = "NO"
            break
    if c != n//3:
        ans = 'NO'
    print(ans)
