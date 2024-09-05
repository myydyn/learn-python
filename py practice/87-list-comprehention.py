# Viết hàm với tham số truyền vào là hai danh sách số thực có cùng kích thước. 
# Trả về danh sách kết quả bằng cách nhân lần lượt số đầu tiên của danh sách 1 
# với số cuối cùng của danh sách 2 cho tới hết danh sách.
# vd: 1 2 3 4 5      || output: 1.0 4.0 9.0 16.0 25.0
#     5 4 3 2 1      ||

def nhanCheo(n, m):
    #Su dung Comprehension va ham zip() de ghep 2 chuoi
    kq = [i*j for i, j in zip(n, m[::-1])]
    return kq

n = input('nhap day 1: ').split()
m = input('nhap day 2: ').split()

if len(n) != len(m):
    print('Vui long nhap hai danh sach cung kich thuoc!')

else:
    try:
        day1 = list(map(float, n))
        day2 = list(map(float, m))
        kq = nhanCheo(day1, day2)
        print(*kq)
    
    except:
        print('Vui long nhap cac phan tu la so thuc!')