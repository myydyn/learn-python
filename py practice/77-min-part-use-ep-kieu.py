# Viết hàm trả về phần tử có giá trị nhỏ nhất không dùng hàm min. 
# (Với tham số là danh sách số thực).
# vd: 5 6 -3.6 7.8 || output: -3.6

def liberty(m):
    nhoNhat = m[0]
    for i in m:
        if i < nhoNhat:
            nhoNhat = i
    return nhoNhat
m = input('nhap danh sach day cac so thuc: ').split()
try:
    if len(m) == 0:
        print('danh sach rong')
    if len(m) > 0:
        m = list(map(float, m))
        nhoNhat = liberty(m)
        print('gia tri nho nhat la: {}'.format(nhoNhat))
except:
    print('stupid')
