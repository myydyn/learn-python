is_it = False
try:
    n = int(input('enter n = '))
    is_it = True
except:
    print('invalid input')

if is_it:
    if n<0:
        print('n is nagative number')
    else:
        for i in range(1, n+1):
            if n % i ==0:
                print(i, end=' ')