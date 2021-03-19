for _ in range(int(input())):
    s = input()
    zero, one = [], []

    for i, x in enumerate(s):
        if x == "0":
            zero.append(i)
        else:
            one.append(i)

    oneone = s.find("11")
    zz = s[oneone:].find("00")
    if zz > 0:
        print("NO")
    else:
        print("YES")
