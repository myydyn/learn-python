def sum_n(n):
    if n:
        return n + sum_n(n-1)
    return 0
try:
    n = int(input('enter n= '))
    if n<0:
        print('n is a positive number, pls')
    else:
        print(sum_n(n))
except:
    print('invalid input')

