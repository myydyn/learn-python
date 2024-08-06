def string_check(s1, s2):
    if s2 in s1:
        print(s1.count(s2))
    else:
        print('string "{}" does not in "{}"'. format(s2, s1))

s1 = input()
s2 = input()

string_check(s1, s2)