is_it = False
try:
    n = int(input('enter n = '))
    is_it = True
except:
    print('invalid input')

if is_it: #cách 1 tự code
    if n<0:
        print('n has to bigger than 1')
    elif n<2:
        print('{} is a not prime number'.format(n))
    else:
        s = 0
        for i in range(1,n//2+1):
            if n%i==0:
                s += i
        if s > 1:
            print('{} is a not prime number'.format(n))
        else:
            print('{} is a prime number'.format(n))

    #cách 2 upgrade c1==kteam
is_it = False
try:
    n = int(input('Enter n = '))
    is_it = True
except ValueError:
    print('Invalid input')

if is_it:
    if n < 0:
        print('n has to be bigger than or equal to 0')
    elif n < 2:
        print('{} is not a prime number'.format(n))
    else:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            print('{} is a prime number'.format(n))
        else:
            print('{} is not a prime number'.format(n))
