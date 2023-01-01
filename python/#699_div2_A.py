from collections import Counter

for _ in range(int(input())):
    x, y = map(int, input().split())
    string = input()
    counter = Counter(string)

    valid = True
    if x >= 0 and y >= 0:
        if counter["R"] < x or counter["U"] < y:
            valid=False
    elif x < 0 and y >= 0:
        if counter["L"] < -x or counter["U"] < y:
            valid=False
    elif x < 0 and y < 0:
        if counter["L"] < -x or counter["D"] < -y:
            valid=False
    else:
        if counter["R"] < x or counter["D"] < -y:
            valid=False

    if valid:
        print("YES")
    else: print("NO")