def str(s1, s2):
    s2_split = s2[::-1]
    str_max = max(len(s1), len(s2))
    str_split  = ''
    
    for i in range(str_max):
        if i < len(s1):
            str_split += s1[i]
        if i < len(s2):
            str_split += s2_split[i]
    return str_split

s1 = input()
s2 = input()
print(str(s1, s2))
