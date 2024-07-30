is_it = False
try:
    n = int(input('enter n = '))
    is_it = True
except:
    print('invalid input')

if is_it:
    if n<0:
        print('n is positive number')
    elif 1<=n<=2:
        print('F(n) = 1')
    else:
        f_1, f_2 = 1, 1
        for i in range(n-2):
            f_1, f_2 = f_2, f_1 + f_2
        print('F(n)= ', f_2)