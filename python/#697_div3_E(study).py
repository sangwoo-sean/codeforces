import sys
input = sys.stdin.readline

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)

def nCk(n, k):
    return fact(n) // (fact(k) * fact(n-k))

for _ in range(int(input())):
    n, k = map(int, input().split())
    mylist = list(map(int, input().split()))

    mylist.sort(reverse=True)
    worst = mylist[k-1]
    count = mylist.count(worst)
    picked = 0
    for i in mylist:
        if i == worst:
            break
        picked += 1
    topick = k - picked
    ans = nCk(count, topick)
    print(ans % 1000000007)