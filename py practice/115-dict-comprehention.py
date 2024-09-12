# Trả về dict gồm các key là số tự nhiên nhỏ hơn n và value tương ứng 
# là bình phương của key. (Với tham số tự nhiên n)
# in: 5     || out: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

def dict_n(n):
    dic = {i:i*i for i in range(n)}
    return dic

try:
    n = int(input('nhap so nguyen n: '))
    if n < 0:
        print('Vui long nhap so nguyen duong!')
    else:
        print(dict_n(n))
except:
    print('Dinh dang dau vao khong hop le!')
    