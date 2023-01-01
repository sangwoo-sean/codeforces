from math import factorial
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    bit = arr[0]
    for i in arr[1:]:
        bit = bit & i
    count = arr.count(bit)
    ans = count*(count-1)*factorial(count-2) % (1e9+7)
    print(ans)
