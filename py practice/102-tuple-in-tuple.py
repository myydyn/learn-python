# Viết hàm với tham số truyền vào Dòng đầu tiên chứa số nguyên n không âm là số phần tử của tuple.
# n dòng tiếp theo, dòng thứ i chứa các phần tử của tuple con thứ i, các phần tử cách nhau bởi khoảng trắng.
# Trả về Dòng đầu tiên hiển thị tuple người dùng nhập vào. Dòng thứ hai hiển thị tuple 
# với từng phần tử trong tuple đó là tổng của mỗi tuple con mà người dùng nhập vào.
# vd: 3                 || output:
    # -5 3 5            ||          ((-5, 3, 5), (-4, -5, -6), (0,))
    # -4 -5 -6          ||          (3, -15, 0)
    # 0                 ||

def tong_ptu(tupleSoNguyen):
    tupleTong= tuple(sum(i) for i in tupleSoNguyen)
    return tupleTong

try:
    n = int(input('nhap n = '))
    danhSach = []
    for _ in range(n):
        # chuyển đổi chuỗi nhập vào thành các số nguyên.
        x = map(int, input('nhap tuple: ').split())
        # Mỗi lần nhập, dữ liệu được chuyển thành một bộ (tuple) rồi thêm vào danh sách danhSach
        danhSach.append(tuple(x)) 
    # chuyển list danhSach chứa các bộ (tuple) thành một bộ giá trị lớn hơn (tuple của tuple).
    tupX = tuple(danhSach)
    print(tupX)
    tong = tong_ptu(tupX)
    print(tong)

except:
    print('Dinh dang dau vao khong hop le!')
