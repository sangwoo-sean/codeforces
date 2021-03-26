for _ in range(int(input())):
    a = input()
    b = input()
    lena = len(a)
    lenb = len(b)

    comm = 0
    for i in range(lena):
        for j in range(lenb):
            for k in range(min(lena-i, lenb-j)):
                if a[i+k] != b[j+k]:
                    break
                comm = max(comm, k+1)
    ans = lena + lenb - 2*comm
    print(ans)
