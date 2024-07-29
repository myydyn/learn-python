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
        bring_back = 0 #số đảo ngược
        while n>0:
            last_num = n%10    # chữ số cuối = n chia 10 lấy dư
            bring_back = bring_back*10 + last_num
            n = n//10 #bỏ dần hàng đơn vị của n
        print(bring_back)