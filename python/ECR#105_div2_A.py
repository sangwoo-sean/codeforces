def check(stry):
    result = 0
    for i in stry:
        if i == "(":
            result += 1
        else:
            result -= 1
        if result < 0:
            return False
    return result == 0


def solve(string):
    if string[0] == string[-1]:
        return "NO"

    first = string[0]
    last = string[-1]
    string = string.replace(first, "(").replace(last, ")")
    case1 = string.replace("A", "(").replace("B", "(").replace("C", "(")
    case2 = string.replace("A", ")").replace("B", ")").replace("C", ")")

    if check(case1) or check(case2):
        return "YES"
    return "NO"


for _ in range(int(input())):
    string = input()
    print(solve(string))
