# Viết hàm với tham số truyền vào là một tuple và một gia tri bất kỳ.
# Trả về tuple vị trí các phần tử của tuple bằng với giá trị tham số truyền vào, neu gia tri do co xuat hien trong tuple.
# vd input: 1 kteam True kteam 3.5
#           kteam
#    output: (1, 3)

def in_vi_tri(s, m):
    viTri = tuple(i for i, ptu in enumerate(s) if ptu == m)
    return viTri

s = input('nhap tuple: ').split()
m = input('nhap mot phan tu bat ky cua tuple: ')
ong = tuple(s)
print(in_vi_tri(ong, m))