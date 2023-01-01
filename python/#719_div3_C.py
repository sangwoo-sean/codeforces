for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(-1)
        continue

    nums = [i for i in range(1, n**2+1, 2)] + [i for i in range(2, n**2+1, 2)]
    i = 0
    for r in range(n):
        for c in range(n):
            print(nums[i], end=" ")
            i += 1
        print()
