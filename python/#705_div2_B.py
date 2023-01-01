import sys
input = sys.stdin.readline

nope = [3, 4, 6, 7, 9]


def check(time, h, m):
    for i in nope:
        if str(i) in time:
            return False
    time = time.replace("2", "@").replace("5", "2").replace("@", "5")
    time = list(reversed(time))
    hh = int("".join(time[:2]))
    mm = int("".join(time[2:]))
    if hh >= h or mm >= m:
        return False

    return True


def add_time(time):
    hh = int(time[:2])
    mm = int(time[2:])
    mm = (mm + 1) % m
    if mm == 0:
        hh = (hh + 1) % h

    if hh < 10:
        hh = "0" + str(hh)
    else:
        hh = str(hh)
    if mm < 10:
        mm = "0" + str(mm)
    else:
        mm = str(mm)
    return hh+mm


for _ in range(int(input())):
    h, m = map(int, input().split())
    time = input().rstrip()
    time = time.replace(":", "")
    if check(time, h, m):
        print(time[:2] + ":" + time[2:])
    else:
        while not check(time, h, m):
            time = add_time(time)
        print(time[:2] + ":" + time[2:])


# int version solution
# import sys
# input = sys.stdin.readline
# nope = "34679"

# def check(ch, cm, h, m):
#     ch, cm = covert(ch, cm)
#     time = ch+cm

#     for i in nope:
#         if i in time:
#             return False
#     time = time.replace("2", "@").replace("5", "2").replace("@", "5")
#     time = list(reversed(time))
#     hh = int("".join(time[:2]))
#     mm = int("".join(time[2:]))
#     if hh >= h or mm >= m:
#         return False
#     return True


# def add_time(ch, cm, h, m):
#     cm = (cm + 1) % m
#     if cm == 0:
#         ch = (ch + 1) % h
#     return ch, cm


# def covert(ch, cm):
#     if ch < 10:
#         ch = "0" + str(ch)
#     else:
#         ch = str(ch)
#     if cm < 10:
#         cm = "0" + str(cm)
#     else:
#         cm = str(cm)
#     return ch, cm


# for _ in range(int(input())):
#     h, m = map(int, input().split())
#     ch, cm = map(int, input().split(":"))

#     if check(ch, cm, h, m):
#         ch, cm = covert(ch, cm)
#         print(ch+":"+cm)
#     else:
#         while not check(ch, cm, h, m):
#             ch, cm = add_time(ch, cm, h, m)
#         ch, cm = covert(ch, cm)
#         print(ch+":"+cm)
