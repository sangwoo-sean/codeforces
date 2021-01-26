### 다른정답해설
# from collections import Counter
# import sys
# input = sys.stdin.readline

# def nC2(n):
#     return n*(n-1)//2

# for _ in range(int(input())):
#     a, b, k = map(int, input().split())
#     boys = list(map(int, input().split()))
#     girls = list(map(int, input().split()))

#     bc = Counter(boys)
#     gc = Counter(girls)

#     total = nC2(k) # 모든 경우의 수 : 주어진 모든 쌍에서 2쌍을 고르는 수
#     bad = 0
#     for i in range(a):
#         bad += nC2(bc[i+1]) # 중복되는 두쌍을 고르는 수
#     for i in range(b):
#         bad += nC2(gc[i+1]) # 중복되는 두쌍을 고르는 수

#     print(total - bad)


## 정답해설
import sys
input = sys.stdin.readline
from collections import Counter

for _ in range(int(input())):
    a, b, k = map(int, input().split())

    b_input = list(map(int, input().split()))
    g_input = list(map(int, input().split()))
    pairs = zip(b_input, g_input)

    boys = Counter(b_input)
    girls = Counter(g_input)

    count = 0
    for a, b in pairs:
        count += k - boys[a] - girls[b] + 1 # 각각의 순서쌍에 대해, 전체 쌍 - 남자가 같은경우 - 여자가 같은경우 +1(남자 여자가 둘다 같은경우 자기자신을 두번 빼므로 1을더해야 자기자신을 한번만 뺌)
        print(count) # 결과는 자기와 쌍을 이룰 수 있는 쌍들의 개수
    
    print(count // 2) # 서로 쌍으로 지목하는 경우가 중복되므로 나누기 2


# # 시간초과
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     a, b, k = map(int, input().split())

#     boys = list(map(int, input().split()))
#     girls = list(map(int, input().split()))
    
#     pairs = [[boys[i], girls[i]] for i in range(k)]
    
#     count = 0
#     for i in range(k):
#         for j in range(i+1, k):
#             if pairs[i][0] == pairs[j][0] or pairs[i][1] == pairs[j][1]:
#                 continue
#             count += 1
#             print(pairs[i], pairs[j])
#     print(count)