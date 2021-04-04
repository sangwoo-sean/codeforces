for _ in range(int(input())):
    s = input()
    if s.count("a") == len(s):
        print("NO")
        continue

    print("YES")
    ans = "a"+s
    if ans == ans[::-1]:
        ans = s+"a"
    print(ans)
