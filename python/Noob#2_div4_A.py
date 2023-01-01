for _ in range(int(input())):
    n = int(input())
    op = [int(i) for i in input()]

    ones = sum(op)
    zeros = n-ones
    if ones > zeros: # 1이 더 많으면 : 왼쪽으로 돌면
        result = (ones-zeros) % 4
        answer = ["E", "N", "W", "S"]
        answer = answer[result]
    else:
        result = (zeros-ones) % 4
        answer = ["E", "S", "W", "N"]
        answer = answer[result]

    print(answer)