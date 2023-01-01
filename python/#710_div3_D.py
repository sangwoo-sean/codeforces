from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    counter = Counter(arr)
    maxe = max(counter.values())
    print(max(n % 2, n-(n-maxe)*2))
    # 일단 n이 홀수이면 모든조건을 만족해도 1개가 남을수있음
    # 제일 개수가 많은것 빼고는 나머지들은 다 어떻게든 없앨 수 있음 => 개수젤많은것 vs 나머지
    # 그러면 나머지 개수만큼 지울수있으니 n - 나머지*2, 나머지 = n-maxe
