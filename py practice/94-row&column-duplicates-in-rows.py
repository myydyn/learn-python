# Viết hàm với tham số truyền vào là một danh sách hai chiều kích thước MxN. 
# Trả về danh sách phần tử xuất hiện ở tất cả các hàng.
# vd: input
        # 3 5
        # Kteam chao nam moi 2021 
        # How Kteam 2021 Chuc mung 
        # Chao mung Kteam nam 2021
# output: Kteam 2021

def nhapDanhSach(m, n):
    hang = []
    for i in range(m):
        row = input().split()
        if len(row) != n:
            print('kich thuoc khong dung')
            return None
        hang.append(row)
    return hang

def xuatHien(s):
    trung = []
    for i in s[0]:
        for j in s[1:]:
            if i not in j:
                break
        else:
            trung.append(i)
    return trung

try:
    m, n = map(int, input('nhap m va n: ').split())
    if m <= 0 or n <= 0:
        print('m va n phai la so nguyen duong')
    else:
        danhSach = nhapDanhSach(m, n)
        if danhSach is not None:
            kyTuTrung = xuatHien(danhSach)
            print(*kyTuTrung)

except:
    print('loi du lieu dau vao')
    