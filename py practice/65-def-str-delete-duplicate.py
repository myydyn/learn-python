def dup_fix(s):
    result = ''
    for i in s:
        if i not in result:
            result += i
    return result
s = input()
print(dup_fix(s))
    