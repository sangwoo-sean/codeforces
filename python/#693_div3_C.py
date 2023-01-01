# 내 처음 풀이 ( 시간초과 ) = 한 원소당 끝까지 계산을 다 해봐야하기때문
import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range(t):
    a = int(input())
    mylist = list(map(int, input().split()))
 
    mylist.insert(0, 0)
    mymax = 0    
    for i in range(1, a+1):
        score = 0
        while i < a+1:
            score += mylist[i]
            i += mylist[i]
 
        if mymax < score :
            mymax = score
    print(mymax)


# 솔루션 해설
# t=int(input())
# for _ in range(t):
#     n=int(input()) # 5
#     A=map(int,input().split())
#     for i in range(n-1,-1,-1): # 4, 3, 2, 1, 0
#         if i+A[i]>=n: # 맨뒤에 원소들일때
#             A[i]=A[i] # 그 값 그대로 고정
#         else: # 1번이상 점프를 하는 원소들이면
#             A[i]=A[i]+A[i+A[i]]  # 다음 점프했을때의 값이랑 더함
#     print(max(A))


# 동적프로그래밍 문제
# i 번째에 도착했을때 총 몇번의 점프를 했을까를 생각해야함
# 뒤에부터 차례대로 구하면, 앞의 원소들은 그 다음꺼랑만 더하면 답이기때문