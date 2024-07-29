is_it = False
try:
    x = float(input('enter  x= '))
    n = int(input('enter n= '))
    is_it = True

except:
    print('invalid input')

if is_it:
    S = 1
    factorial = 1
    if n == 0:
        print(1)
    elif n<0:
        print('pls enter n as a nature number')
    else:
        for i in range(1, 2*n+1):
            factorial *=i
            if i%2 ==0:
                S += pow(x, i)/factorial
            else:
                S -= pow(x, i)/factorial
            
        print('{:.5f}'.format(S))   

