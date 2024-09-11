# Viết hàm với tham số truyền vào là một danh sách. 
# Trả về set các phần tử xuất hiện trong danh sách đã cho.
# in: mot 2 ba $ mot 3 2 || out: ba 2 3 mot $

def liet_ke(s):
    kq = set(s)
    return kq
s = input('nhap: ').split()
kq = liet_ke(s)
print(*kq)
