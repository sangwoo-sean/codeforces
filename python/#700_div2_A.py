for _ in range(int(input())):
    alph = list("abcdefghifklmnopqrstuvwxyz")
    case = list(input())
    alice = 1
    for i, letter in enumerate(case):
        if alice:
            for alp in alph:
                if alp != letter:
                    case[i] = alp
                    alice = 0
                    break
        else:
            for alp in reversed(alph):
                if alp != letter:
                    case[i] = alp
                    alice = 1
                    break
    print("".join(case))