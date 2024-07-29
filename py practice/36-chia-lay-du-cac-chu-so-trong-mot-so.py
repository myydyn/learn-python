is_it = False
try:
    n = int(input('enter a natural number from 2 digits and more '))
    is_it = True
except:
    print('invalid input')
if is_it:
    if n<=9:
        print('n>9, pls replay')
    else:
        s1 = 0
        s2 = 0
        
        while n>0:
            last_num = n%10
            if last_num % 2 ==0:
                s1 = s1 + last_num
            else:
                s2 = s2 +last_num
            s = s1*s2
            n = n // 10
        print(s)
