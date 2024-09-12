# Trả về dict gồm các key là số tự nhiên nhỏ hơn n và value tương ứng 
# là bình phương của key. (Với tham số tự nhiên n)
# in: 5     || out: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#       code thu cong

def dic(n):
    kq = dict()
    for i in range(n):
        kq[i] = i*i
    return kq

try:
    n = int(input('nhap n= '))
    if n < 0:
        print('nhap so nguyen duong')
    else:
        kq = dic(n)
        print(kq)
except:
    print('k hop le')

