n = 4
a = [5, 2, 7, 3]
n = 2
a = [7, 8]


import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    bob = 0
    alice = 0

    a.sort()
    turn=0
    i = n-1
    while turn < n:
        if turn % 2 == 0: #alice
            if a[i] % 2 == 0: # 짝수면
                alice += a[i]
                i -= 1
            
            else: # 홀수면
                i -= 1

            turn += 1
            continue
        if turn % 2 == 1:#bob
            if a[i] % 2 == 1:
                bob += a[i]
                i -= 1
            else:
                i -= 1
            turn += 1
            
    if bob < alice:
        print("Alice")
    elif bob > alice:
        print('Bob')
    else:
        print("Tie")