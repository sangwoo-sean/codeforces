from collections import Counter


n = 6
balls = [1, 1, 1, 2, 3, 4, 7]

for _ in range(int(input())):
    n = int(input())
    balls = list(map(int, input().split()))
    ball_count = Counter(balls)

    print(max(ball_count.values()))