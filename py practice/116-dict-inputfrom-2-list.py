# Trả về dict gồm các phần tử là key và value tương ứng từ hai danh sách đầu vào.
# đầu vào
    # Gồm hai dòng:
    # Dòng 1 chứa các phần tử của danh sách key. Các phần tử cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của danh sách value. Các phần tử cách nhau bởi khoảng trắng
# đầu ra
    # Dòng đầu tiên hiển thị dict theo yêu cầu đề bài.
    # N dòng tiếp theo mỗi dòng hiển thị một phần tử của dict theo định dạng:
# vd:
    # in: 1 2 3     
    #     mot hai ba
    # out: '1': 'mot', '2': 'hai', '3': 'ba'}
            # 1: mot
            # 2: hai
            # 3: ba

def dic(x, y):
    #Cach 1: Them thu cong mot phan tu vao dict
    # dictKetQua = dict()
    # for i in range(len(listKey)):
    #     dictKetQua[listKey[i]] = listValue[i]
    
    #Cach 2: Su dung Constructor Dict ket hop voi ham zip 
    kq = dict(zip(x, y))
    return kq

x = input('nhap các phần tử của danh sách key: ').split()
y = input('nhap các phần tử của danh sách value: ').split()

if len(x) != len(y):
    print('Vui long nhap so luong key va value bang nhau!')
else:
    kq = dic(x, y)
    print(kq)
    #Su dung phuong thuc items() de lay tuple cac (key, value) cua dict
    for key, value in kq.items():
        print(f'{key}: {value}')
