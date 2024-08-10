def sentence(s):
    result = ''
    lst = s.split()
    for i in lst:
        if (len(i) > len(result) or len(i) == len(result) and i < result):
            result = i
    return result
s = input()
print(sentence(s))
