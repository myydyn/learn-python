# Viết hàm với tham số truyền vào là một danh sách các số nguyên.
#  Trả về danh sách các phần tử là số nguyên tố.
#  vd: 5 3 -6 7 9 -10 22 11 || output: 5 3 7 11


# Cach 1: dung 2 ham
import math

def ktSoNgynto(m):
    if m < 1:
        return False
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            return False
    return True

def dsSoNguyen(n):
    # Sử dụng List Comprehension kết hợp với vòng lặp for 
    # và goi hàm kt_so_nguyen_to để khởi tạo list
    nguyenTo = [i for i in n if ktSoNgynto(i)]
    return nguyenTo

daySo = input('nhap day so: ').split()
if len(daySo) == 0:
    print('DS rong')
else:
    try:
        tachChuoi = list(map(int, daySo))
        nguyenTo = dsSoNguyen(tachChuoi)
        print(*nguyenTo)
    except:
        print('pla...pla')
