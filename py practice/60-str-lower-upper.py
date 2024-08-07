def str(s):
    if len(s) == 0:
        return ''
    if s[0].islower():
        return s.lower()
    if s[0].isupper():
        return s.upper()
    return s

s = input()
print(str(s))
    