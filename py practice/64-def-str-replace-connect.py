#DIY
def str(s):
    s = s.strip()
    while ' ' in s:
        return s.replace(' ', '-')
s = input()
print(str(s))

