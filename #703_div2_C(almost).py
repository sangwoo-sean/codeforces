import sys
input = sys.stdin.readline
n = int(input())


def ask(l, r):
    print("?", l, r)
    sys.stdout.flush()
    return int(input())


l = 1
r = n
while l < r-1:
    mid = (l+r)//2
    res1 = ask(l, r)

    if res1 < mid:  # 중간보다 왼쪽에 있으면
        if ask(l, mid) == res1:
            r = mid
        else:
            l = mid
    else:  # 중간보다 오른쪽이면
        if ask(mid, r) == res1:
            l = mid
        else:
            r = mid

if ask(l, r) == l:
    ans = r
else:
    ans = l

print("!", ans)
