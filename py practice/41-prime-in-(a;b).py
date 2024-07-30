import math
isit = False
try:
    a = int(input('a= '))
    b = int(input('b= '))
    isit = True
except:
    print('invalid input')

if isit:
    if a<=0 or b<=0:
        print('a, b have to be positive number')
    elif a>b:
        print('a has to smaller than b')
    else:
        for i in range(a, b+1):
            if i>1:
                for j in range(2, int(math.sqrt(i))+1):
                    if i%j==0:
                        break
                else:
                    print(i, end=' ')

