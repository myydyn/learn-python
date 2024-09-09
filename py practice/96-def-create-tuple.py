# Viết hàm với tham số truyền vào là số tự nhiên n. 
# Khởi tạo và hiển thị tuple chứa n số tự nhiên đầu tiên ra màn hình.
# vd: input: n = 5 || output: (0, 1, 2, 3, 4)

def tupleSoTuNhien(n):
    ong = tuple(i for i in range(n))
    print(ong)

n = int(input('nhap n = '))
try:
    if n < 0:
        print('n la so nguyen duong')
    else:
        tupleSoTuNhien(n)
        
except:
    print('dau vao k hop le')