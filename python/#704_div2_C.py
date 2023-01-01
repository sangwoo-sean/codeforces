n, m = map(int, input().split())
s = input()
t = input()
left, right = [], []
i, j = 0, 0

while i < m and j < n:
    if t[i] == s[j]:
        right.append(j)
        i += 1
    j += 1

i, j = m-1, n-1
while i >= 0 and j >= 0:
    if t[i] == s[j]:
        left.append(j)
        i -= 1
    j -= 1
left.reverse()

ans = 0
for i in range(m-1):
    ans = max(ans, left[i+1]-right[i])
print(ans)
