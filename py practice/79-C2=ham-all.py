# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Kiểm tra xem danh sách có phải là danh sách giảm không.
# vd: 15 5 0 -8 -28 || output: True

def pull(m):
    # dung hàm all() kết hợp vòng lặp for 
    ketqua = all(m[i] >= m[i+1] for i in range(len(m)-1))
    return ketqua

m = input('nhap day so: ').split()
if len(m) == 0:
    print('ds rong')
else:
    try:
        danhSach = list(map(float, m))
        print(pull(danhSach))
    except:
        print('out')