# 원소가 k 보다 크면 count 1
# 원소 두개 합친게 8이면 count 1

for _ in range(int(input())):
    n, k = map(int, input().split())
    students = list(map(int, input().split())) + [0]
    students.sort(reverse=True)

    count = 0
    i = 0
    j = n
    while i < j:
        if students[i] >= k:
            count += 1
            i += 1
        else:
            if students[i] + students[j] >= k:
                i += 1
                count += 1
            j -= 1
    print(count)        
        