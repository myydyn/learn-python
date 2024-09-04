# Viết hàm với tham số truyền vào là một danh sách các số nguyên.
#  Trả về danh sách các phần tử là số nguyên tố.
#  vd: 5 3 -6 7 9 -10 22 11 || output: 5 3 7 11


# Cach 1: dung 1 ham
import math

def soNguyenTo(m):
    lst = []
    for n in m:
        if n > 1:
            isPrime = True
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    isPrime = False
                    break
            if isPrime:
                lst.append(n)
    return lst

m = input('nhap day so: ').split()
if len(m) == 0:
    print('DS rong')
else:
    try:
        danhSach = list(map(int, m))
        print(soNguyenTo(danhSach))

    except:
        print('Vui lòng nhập vào các số nguyên hợp lệ.')
