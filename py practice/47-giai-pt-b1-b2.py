import math
def pt_b1(a, b):
    if a == 0:
        if b == 0:
            return 'pt vo so nghiem'
        return 'pt vo nghiem'
    return 'pt co 1 nghiem: x= {}'.format(-b/a)

def pt_b2(a, b, c):
    if a == 0:
        return pt_b1(b, c)
    delta = b*b - 4*a*c
    if delta >0:
        x1 = math.sqrt(delta)/2*a
        x2 = -(math.sqrt(delta))/2*a
        return 'pt co 2 nghiem phan biệt:\n x1= {}; x2= {}'.format(x1, x2)
    if delta == 0:
        x = -b/(2*a)
        return 'pt có nghiệm kép x= {}'.format(x)
    return 'pt vô nghiệm'
try:
    function = input()
    if function == '1':
        a, b = map(float, input().split())
        print(pt_b1(a, b))
    elif function == '2':
        a, b, c = map(float, input().split())
        print(pt_b2(a, b, c))

    else:
        print("Vui long chon mot trong hai chuc nang:\n1. Giai phuong trinh bac nhat\n2. Giai phuong trinh bac hai")
    
except:
    print("Dinh dang dau vao khong hop le!")