# Viết hàm với tham số truyền vào là một danh sách hai chiều kích thước MxN. 
# Trả về danh sách hai chiều chuyển vị (cột thành hàng, hàng thành cột).
# vd: 
# input: 
#  m n =  3 4
        # 1 2 3 4
        # nam sau bay tam
        # 9 muoi 11 12
# output:
        # 1 nam 9
        # 2 sau muoi
        # 3 bay 11
        # 4 tam 12

def nhapDanhSach(m, n):
    hang = []
    for i in range(m):
        row = input().split()
        if len(row) != n:
            print('danh sach khong dung kich thuoc')
            return None
        hang.append(row)
    return hang

def inDanhSach(danhSach):
    if danhSach:
        for i in danhSach:
            print(*i)

def danhSachChuyenViTri(danhSach):
    empty = []
    #So dong cua danh sach moi bang so cot cua danh sach cu va nguoc lai
    m = len(danhSach[0])
    n = len(danhSach)
    #Su dung vong lap for duyet tung cot da chuyen cua danh sach 2 chieu
    for i in range(m):
        cot = [danhSach[j][i] for j in range(n)]
        empty.append(cot)
    return empty

try:
    m, n = map(int, input('nhap: ').split())
    if m <=  0 or n <= 0:
        print('nguyen duong')
    else:
       #Goi ham nhap danh sach va truyen vao tham so kich thuoc M, N
       danhSach = nhapDanhSach(m, n)
       if danhSach is not None:
           #Goi ham va truyen vao tham so la danh sach 2 chieu
           dsChuyenVi = danhSachChuyenViTri(danhSach)
           inDanhSach(dsChuyenVi)

except:
    print('k hop le')      
