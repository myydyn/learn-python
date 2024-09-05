# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Trả về giá trị, số lượng và vị trí xuất hiện của phần tử lớn nhất trong danh sách.
# vd: -5 3.5 9 2 -3.75 6 9 9 3.375 9 || output: 9.0 \n 4 \n 2 6 7 9

def lonNhat(n):
    x = max(n)
    # trong n đếm giá trị x
    dem = n.count(x)
# list comprehention: trong vòng lặp lập danh sách có điều kiện 
    viTri = [i for i in range(0, len(n)) if n[i] == x]
    return x, dem, viTri

n = input('nhap day so: ').split()
if len(n) == 0:
    print('ds rong')
else:
    try:
        danhSach = list(map(float, n))
        x, dem, viTri = lonNhat(danhSach)
        print(x)
        print(dem)
        print(*viTri)
    except:
        print('loi')
