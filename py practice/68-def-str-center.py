def text(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

def f_text(s):
    raw = s.split('.')
    max = 0
    for i in raw:
        i = text(i)
        if len(i) > max:
            max = len(i)

    for i in raw:
        i = text(i)
        print(i.center(max))

s = input()    
f_text(s)