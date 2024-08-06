def string(s, a, b):
    junior = s[a:b+1]
    funior_flip = junior[::-1]
    return funior_flip

s = input()
a, b =  map(int, input().split())

try:
    if a<0 or b<0:
        print('natural plz')
    elif a>b:
        print('a<=b pls')
    elif a >= len(s) or b >= len(s):
        print('a and b iz not greater than string length')
    else:
        print(string(s, a, b))
except:
    print('your the most beautiful')
        
    