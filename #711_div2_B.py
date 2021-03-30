from collections import Counter

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, w = map(int, input().split())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    li = sorted(list(counter.keys()), reverse=True)

    ans = 0
    while n > 0:
        ans += 1
        curr = w
        for i in li:
            # 공간이 부족하다면 현재층 남은칸에 들어갈 수 있는 블럭의 갯수, 블럭이 다 들어가도 공간이 충분하다면 블럭의 갯수
            many = min(curr//i, counter[i])
            curr -= many*i  # 현재층 남은칸 = 그 층에 넣으려는 블럭갯수 * 블럭크기
            counter[i] -= many  # 채운만큼 블럭갯수 차감
            n -= many  # while문 종료를 위해 채운만큼 n 차감
    print(ans)

    # 시간초과
    # arr.sort(reverse=True)

    # for i in range(n):
    #     for j in range(n):
    #         if box[j] >= arr[i]:
    #             box[j] -= arr[i]
    #             break

    # print(n-box.count(w))
