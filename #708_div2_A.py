for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    sor = sorted(arr)
    ans = sorted(set(arr))
    for i in ans:
        sor.remove(i)
    print(*ans, *sor)

    # nums = [0 for _ in range(101)]
    # for i in arr:
    #     nums[i] += 1

    # ans = []
    # for i in range(101):
    #     if nums[i]:
    #         ans.append(i)
    #         nums[i] -= 1
    # for i in range(101):
    #     ans += [i]*nums[i]

    # print(*ans)
