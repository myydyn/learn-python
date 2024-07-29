is_it = False
try:
    n = int(input('enter n to get n!, n= '))
    is_it = True
except:
    print('invalid value')
if is_it:
    if n<0:
        print('pls enter a negative value')
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
            #result = result*i
        print(result)

