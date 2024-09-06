# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Trả về trung bình cộng và hai danh sách: một danh sách gồm các số nhỏ hơn 
# và một danh sách gồm các số lớn hơn hoặc bằng trung bình cộng của danh sách được truyền vào.
# vd: 1 2 3 4 5 6 7 8      || output: 4.5
#                          ||         1.0 2.0 3.0 4.0
#                          ||         5.0 6.0 7.0 8.0

def phanTach(n):
    trungBinh = sum(n) / len(n)
    be = [i for i in n if i < trungBinh]
    lon = [i for i in n if i >= trungBinh]
    return trungBinh, be, lon

n  = input('nhap day so: ').split()
if len(n) == 0:
    print('ds rong')
else:
    try:
        danhSach = list(map(float, n))
        trungBinh, be, lon = phanTach(danhSach)
        print(trungBinh)
        print(*be)
        print(*lon)

    except:
        print('Vui long nhap cac phan tu la so thuc!')

    