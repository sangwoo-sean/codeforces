import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = float(input())
    valid = True

    check = []
    for i in range(47):
        check.append(2**i)
    
    if n in check:
        valid = False

    if valid:
        print("YES")
    else:
        print("NO")