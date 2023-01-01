
for _ in range(int(input())):
    a, b = map(int, input().split())
    A = a^b
    bin_a = bin(a)[2:]
    bin_b = bin(b)[2:]

    gap = len(bin_b)-len(bin_a)
    for i in range(gap):
        bin_a = "0"+bin_a

    valid = False
    for i in range(len(bin_b)):
        if bin_a[i] == '1' and bin_b[i] == '1':
            valid = True
            break
    if a == 1 and b == 1:
        valid = False

    if valid:
        print("Yes")
    else:
        print("No")