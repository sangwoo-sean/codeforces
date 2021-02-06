n, m = 10, 5
planks = [7, 3, 2, 1, 7, 9, 4, 2, 7, 9]
desire = [9, 9, 2, 1, 4, 9, 4, 2, 3, 9]
painter = [9, 9, 7, 4, 3]

for _ in range(int(input())):
    n, m = map(int, input().split())
    planks = list(map(int, input().split()))
    desire = list(map(int, input().split()))
    painter = list(map(int, input().split()))

    answer = []
    lastpaint = painter[-1]
    if lastpaint not in desire:
        print("NO")
        continue
    lasti = desire.index(lastpaint) +1

    for j in range(m-1):
        color = painter[j]
        done = False
        for i in range(n):
            if color == desire[i] and color != planks[i]:
                planks[i] = color
                answer.append(i+1)
                done = True
                break
        if not done:
            answer.append(lasti)
    
    answer = answer+[lasti]
    print("YES")
    print(" ".join(str(i) for i in answer))

