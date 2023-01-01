n, q = map(int, input().split())
ns = list(map(int, input().split()))
qs = list(map(int, input().split()))

for x in qs:
    idx = ns.index(x)
    num = ns[idx]
    print(idx+1, end=" ")
    ns[1:idx+1] = ns[:idx]
    ns[0] = num


# n,q=map(int,input().split())
# a=list(map(int,input().split()))
# t=list(map(int,input().split()))
# mp={}
# for i in range(n):
#     if a[i] not in mp:
#         mp[a[i]]=i+1
# for q in t:
#     for k in mp:
#         if mp[k]<mp[q]:
#             mp[k]+=1
#     print(mp[q],end=' ')
#     mp[q]=1
