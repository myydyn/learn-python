def text(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s
def f_text(s):
    raw = s.split('.')
    for i in raw:
        i = text(i)
        print(i.title())
s = input()
f_text(s)
