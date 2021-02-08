# A 공격력
# B 체력
# n 몬스터 수
# i번쨰 몬스터는 ai 공격력과 bi 체력

# 체력이 0이하면 죽음
# 마지막몬스터까지 잡고 죽어도 상관없음

import sys
input = sys.stdin.readline

from math import ceil
A, B, n = 3, 17, 1
a = [2]
b = [16]

for _ in range(int(input())):
    A, B, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    mylist = [[a[i], b[i]] for i in range(n)]
    mylist.sort(key=lambda x: x[0])

    win = True
    for i in range(n-1):
        attTime = ceil(mylist[i][1] / A)
        B -= attTime * mylist[i][0]

        if B <= 0:
            win = False
            break
    
    if ceil(mylist[-1][1]/A) > ceil(B/mylist[-1][0]):
        win=False

    if win:
        print("YES")
    else: print("NO")