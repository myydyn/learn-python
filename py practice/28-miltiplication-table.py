is_true = False
try:
    print('enter N, with N is the value of miltiplication table')
    n = int(input())
    is_true = True
except:
    print('input value is error')
if is_true:
    if 1<= n <=9:
        x = 0
        for i in range(1,11):
            x = n*i
            print('{} * {} = {}'.format(n,i,x))
    else:
        print('Just miltiplication from 1 to 9')
