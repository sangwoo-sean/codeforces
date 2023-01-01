for _ in range(int(input())):
    n = int(input())
    ss = input()
    ms = set()
    for i in range(n):
        if ss[i] not in ms:
            ms.add(ss[i])
        else:
            if ss[i-1] != ss[i]:
                print("NO")
                break
    else:
        print("YES")
