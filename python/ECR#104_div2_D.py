n = 41
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             if k == (i**2 - j) and i**2 + j**2 == k**2 and i <= j <= k:
#                 print(i, j, k)

for _ in range(int(input())):
    n = int(input())

    i = 0
    while True:
        if i**2 + (i+1)**2 <= n:
            result = i
        else:
            break
        i += 1
    print(result)
