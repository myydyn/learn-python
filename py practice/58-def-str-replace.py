def str(s):
    if len(s)<3 or s[-3:] != 'ing':
        s += 'ing'
    else:
        s = s[:-3] + 'ly'
    return s

s = input()

print(str(s))

#def modify_string(s):
#    if len(s) < 3 or not s.endswith('ing'):
#        s += 'ing'
#    else:
#        s = s.replace('ing', 'ly')
#    return s
#s = input()
#print(modify_string(s))
