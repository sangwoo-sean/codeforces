import sys
input = sys.stdin.readline
n = int(input())

mylist = [100000]*(n+1)

stack = 0
start = 1
end = n

while start < end:

    mid = (start + end)//2

    print("?", mid)
    sys.stdout.flush()
    mylist[mid] = int(input())
    print("?", mid+1)
    sys.stdout.flush()
    mylist[mid+1] = int(input())

    if mylist[mid] < mylist[mid+1]:
        end = mid
    else:
        start = mid + 1
print("!", start)