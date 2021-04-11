from collections import Counter

for _ in range(int(input())):
    zero, one = map(int, input().split())
    s = list(input())
    c = Counter(s)
    zero -= c["0"]
    one -= c["1"]
    if zero < 0 or one < 0:
        print(-1)
        continue

    n = len(s)
    fail = False
    for i in range(n):
        if s[i] == "?":
            s[i] = s[n-1-i]
            if s[i] == '0':
                zero -= 1
            elif s[i] == '1':
                one -= 1
        elif s[n-1-i] != '?' and s[i] != s[n-1-i]:
            fail = True

    if fail or zero < 0 or one < 0:
        print(-1)
        continue

    for i in range(n):
        if i == n // 2 and n % 2:
            continue
        if s[i] == '?':
            if zero > 1:
                s[i] = '0'
                s[n-1-i] = '0'
                zero -= 2
            else:
                s[i] = '1'
                s[n-1-i] = '1'
                one -= 2
    if s[n//2] == '?':
        if zero > 0:
            s[n // 2] = '0'
            zero -= 1
        else:
            s[n // 2] = '1'
            one -= 1

    if zero != 0 or one != 0:
        print(-1)
    else:
        print("".join(s))
