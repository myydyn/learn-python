# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Sắp xếp danh sách theo thứ tự tăng dần (Không sử dụng hàm sắp xếp có sẵn).
# vd: 15 5 0 -8 -28 || output: -28.0 -8.0 0.0 5.0 15.0
def arraign(m):
    for i in range(len(m)):
        soNhoNhat = i
        for j in range(i+1, len(m)):
            if m[j] < m[soNhoNhat]:
                soNhoNhat = j
    #Doi vi tri phan tu thu i dang xet voi phan tu nho nhat
        m[i], m[soNhoNhat] = m[soNhoNhat], m[i]

m = input('nhap day so: ').split()
if len(m) == 0:
    print('DS rong')
else:
    try:
        danhSach = list(map(float, m))
        sapXep = arraign(danhSach)
        print(*danhSach)
        
    except:
        print('error')
# sap xep vi tri cac phan tu trong khoang