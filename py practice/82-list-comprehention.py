# Viết hàm với tham số truyền vào là một danh sách, cac phan tu cach boi khoang trang 
# Trả về danh sách các phần tử xuất hiện duy nhất trong danh sách đã cho.
# vd: mot 2 ba $ mot 3 2 || output: ba $ 3

def kiemTra(s):
    duyNhat = [i for i in s if s.count(i) == 1]
    return duyNhat
nhapLieu = input('Nhap du lieu: ').split()
duyNhat = kiemTra(nhapLieu)
print(*duyNhat)