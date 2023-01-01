import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    op = input()

    for _ in range(m):
        l, r = map(int, input().split())

        mymax = 0
        mymin = 0

        x = 0
        for i in range(l-1):
            if op[i] == '+':
                x += 1
                if x > mymax:
                    mymax = x
            elif op[i] == "-":
                x -= 1
                if x < mymin:
                    mymin = x

        for i in range(r, n):
            if op[i] == '+':
                x += 1
                if x > mymax:
                    mymax = x
            elif op[i] == "-":
                x -= 1
                if x < mymin:
                    mymin = x
        print(mymax-mymin+1)







###2차

# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     op = input()

#     for _ in range(m):
#         l, r = map(int, input().split())

#         mymax = 0
#         mymin = 0
        
#         x = 0
#         for i in range(l-1):
#             if op[i] == '+':
#                 x += 1
#                 if x > mymax:
#                     mymax = x
#             elif op[i] == "-":
#                 x -= 1
#                 if x < mymin:
#                     mymin = x

#         for i in range(r, n):
#             if op[i] == '+':
#                 x += 1
#                 if x > mymax:
#                     mymax = x
#             elif op[i] == "-":
#                 x -= 1
#                 if x < mymin:
#                     mymin = x
#         print(mymax-mymin+1)



### 1차
# import sys
# input = sys.stdin.readline

# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     op = input()

#     for _ in range(m):
#         l, r = map(int, input().split())

#         mymax = 0
#         mymin = 0

#         x = 0
#         # myset = {0}
#         for i in range(l-1):
#             if op[i] == '+':
#                 x += 1
#                 if x > mymax:
#                     mymax = x
#             elif op[i] == "-":
#                 x -= 1
#                 if x < mymin:
#                     mymin = x
#             # if x not in myset:
#             #     myset.add(x)

#         for i in range(r, n):
#             if op[i] == '+':
#                 x += 1
#                 if x > mymax:
#                     mymax = x
#             elif op[i] == "-":
#                 x -= 1
#                 if x < mymin:
#                     mymin = x
#             # if x not in myset:
#             #     myset.add(x)
#         # print(len(myset))
#         print(mymax-mymin+1)