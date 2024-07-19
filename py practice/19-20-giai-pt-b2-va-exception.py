print('nhap vao cac he số a b c của pt dạng aX^2+bX+c=0')
Iscapable = False
try:
    a, b, c = map(float,input().split())
    Iscapable = True
except:
    print('đầu vào k hợp lệ')
if Iscapable:
    if a ==0:
        print('a phải khác 0')

    elif c == b == 0:
        print('pt có nghiệm duy nhất x = 0')

    else:
        alpha = b**2-4*a*c
        x =-b/(2*a)
        x1=(-b + alpha**0.5)/2*a
        x2=(-b - alpha**0.5)/2*a

        if alpha==0:
            print('pT có nghiệm kép x1=x2= ', x)

        elif alpha>0:
            print('PT có 2 nghiệm phân biệt x1={} và x2={}'.format(x1, x2))

        elif alpha<0:
            print('PT vô nghiệm')
    