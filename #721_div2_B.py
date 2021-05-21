for _ in range(int(input())):
    n = int(input())
    s = list(input())
    zeros = s.count("0")
    if zeros % 2 == 0 or zeros == 1:
        print("BOB")
    else:
        print("ALICE")
