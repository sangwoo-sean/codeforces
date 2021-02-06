for _ in range(int(input())):
    n, k = map(int, input().split())
    mylist = list(map(int, input().split()))
    k = min(k, 20000)

    for i in range(k):
        l = -2
        for j in range(n-1):
            if mylist[j] < mylist[j+1]:
                l = j
                break
        
        if l >= 0:
            mylist[l] += 1
    
    print(l+1)