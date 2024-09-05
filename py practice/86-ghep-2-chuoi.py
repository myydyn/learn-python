# Viết hàm với tham số truyền vào là hai danh sách cùng kích thước: danh sách tên và danh sách quốc tịch. 
# Hiển thị ra màn hình tên và quốc tịch tương ứng với vị trí trong danh sách.
# vd: Julia, Chloe, Tracy, James  || output: Julia - Viet Nam
#     Viet Nam, Y, My, Phap       ||         Chloe - Y
#                                 ||         Tracy - My
#                                 ||         James - Phap

def xoaSpace(s):
#Su dung phuong thuc strip() de xoa khoang trang o dau va cuoi chuoi
    s = s.strip(' ')
    # su dung while de lap cho het khoang trang thua
    while '  ' in s:
        # su dung replace(a, b) de thay the 2 khoang trang thanh 1
        s = s.replace('  ', ' ')
    return s

def inDanhSach(ten, ethnicity):
    # list comprehention ket hop voi ham xoa khoang trang
    ten = [xoaSpace(t) for t in ten]
    ethnicity = [xoaSpace(q) for q in ethnicity]
    #Su dung vong lap for voi ham zip(a, b) de ghep 2 chuoi voi nhau
    for t, q in zip(ten, ethnicity):
        print(t + ' - ' + q)

#Su dung ham split(',') de cat chuoi tai moi dau ','
ten = input('nhap ten: ').split(',')
ethnicity = input('nhap quoc tich: ').split(',')

if len(ten) != len(ethnicity):
    print('loi')
else:
    inDanhSach(ten, ethnicity)
