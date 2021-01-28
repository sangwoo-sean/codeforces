# 홀수가 하나도없으면 불가능

# 짝수가 있으면 짝수갯수만큼

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    mylist = list(map(int, input().split()))

    count = 0
    valid = False
    
    for i in mylist:
        if i % 2 == 0:
            count += 1
        if not valid and i%2 == 1:
            valid = True
    if valid:
        print(count)
    else:
        print(-1)
    