def sum(*agrs):
    s = 0
    for i in agrs:
        s +=i
    return s
print("1 + 2 + 3 = {}".format(sum(1, 2, 3)))
print("1 + 2 + 3 + 4 + 5 = {}".format(sum(1, 2, 3, 4, 5)))