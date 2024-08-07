def str(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s
s = input()

print(str(s))