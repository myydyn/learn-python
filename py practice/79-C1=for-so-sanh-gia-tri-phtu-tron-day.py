# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Kiểm tra xem danh sách có phải là danh sách giảm không.
# vd: 15 5 0 -8 -28 || output: True

def kiemTraDS(m):
    # c1: Sử dụng vòng lặp for
    # so sanh gia tri tung phan tu trong danh sach
    for i in range(len(m) - 1):
        if m[i] < m[i+1]:
            return False
    return True

m = input('nhap day so: ').split()
if len(m) == 0:
    print('ds rong')
else:
    try:
        danhSach = list(map(float, m))
        print(kiemTraDS(danhSach))
        # print(kq)
    except:
        print('haizz')
    