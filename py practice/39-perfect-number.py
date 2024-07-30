is_it = False
try:
    n = int(input('enter n = '))
    is_it = True
except:
    print('invalid input')

if is_it:
    if n<=0:
        print('n is positive number')
    else:
        s = 0
        for i in range(1,n//2+1): #Do ước của một số không bao giờ lớn hơn số đó chia 2 (trừ chính nó).
            if n%i==0:
                s += i
        if s == n:
            print('{} is a perfect number'.format(n))
        else:
            print('{} is not a perfect number'.format(n))