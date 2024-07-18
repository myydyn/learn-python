try:
    #print('enter 3 measurements of lines and separate by space')
    a, b, c = map(float, input('nhap a b c ').split())

#try:
    if a+b>c and a+c>0 and b+c>a:
        print('{}, {}, {} are the sides of a triangle'.format(a,b,c))

    elif a <= 0 or b<=0 or c<=0:
        print('Cac canh cua tam giac phai lon hon 0!')

    else:
        print('{}, {}, {} are not the sides of a triangle'.format(a,b,c))

except:
    print('định dạng k hơp lệ')