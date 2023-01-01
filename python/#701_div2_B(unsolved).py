from sys import stdin
input = stdin.readline

n, q, k = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    l, r = map(int, input().split())

    # 1~k 까지 두번세는데(올라가는거 한번, 내려가는거 한번) 1~arr[l-1] 까지 한번 안세고, arr[r-1]~k 까지 한번 안세고, l~r까지 각 점들의 개수만큼은 두번다 안셈
    answer = 2*k-2*(r-l+1) - (arr[l-1]-1) - (k-arr[r-1])
    print(answer)
