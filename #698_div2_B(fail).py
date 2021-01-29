q, d = 3, 7
qs = [24, 25, 27]

for _ in range(int(input())):
    q, d = map(int, input().split())
    qs = list(map(int, input().split()))

    for aq in qs:
        valid = False

        while aq > 0:
            if str(d) in str(aq):
                valid = True
                break
            aq -= d
            
        if valid:print("YES")
        else:print("NO")