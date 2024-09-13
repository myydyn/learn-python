# Trả về kết quả gồm chuỗi các key được nối với nhau bằng dấu "-" và 
# tổng các value. (Tham số là 1 dict)

# đầu vào
    # Gồm hai dòng:
    # Dòng đầu tiên chứa các phần tử của danh sách key là chuỗi. Các phần tử cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của danh sách value là các số nguyên. Các phần tử cách nhau bởi khoảng trắng

# đầu ra
    # Gồm ba dòng:
    # Dòng đầu tiên hiển thị dict được nhập từ bàn phím
    # Dòng thứ hai hiển thị chuỗi các key được nối với nhau bằng dấu “-”
    # Dòng thứ ba hiển thị tổng của các value
# in: toan van anh
#     8 9 10 
# out:    {'toan': 8, 'van': 9, 'anh': 10}
#         toan-van-anh
#         27

def nhap_dict():
    key = input('nhap key: ').split()
    try:
        value = list(map(int, input('nhap value: ').split()))
    except:
        print('Vui long nhap value la so nguyen!')
        return None
    
    if len(key) != len(value):
        print('Vui long nhap so luong key va value bang nhau!')
        return None
    dictA = dict(zip(key, value))
    return dictA

def tinh_tong(dictA):
    #Su dung phuong thuc keys() de lay ra danh sach cac key cua dict
    listKey = dictA.keys()
    chuoiKey = '-'.join(listKey)
    #Su dung phuong thuc values() de lay ra danh sach cac value cua dict
    listValue = dictA.values()
    sumValue = sum(listValue)
    return chuoiKey, sumValue

dictA = nhap_dict()
if dictA is not None:
    print(dictA)
    chuoiKey, tongValue = tinh_tong(dictA)
    print(chuoiKey)
    print('tong: {}'.format(tongValue))
