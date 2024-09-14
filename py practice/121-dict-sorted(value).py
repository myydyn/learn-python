# Trả về dict kết quả đã sắp xếp theo giá trị key tăng dần. 
# (Tham số là 1 dict)

# đầu vào
    # Gồm hai dòng:
    # Dòng đầu tiên chứa các phần tử của danh sách key là các số nguyên. Các phần tử cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của danh sách value. Các phần tử cách nhau bởi khoảng trắng
# đầu ra
    # Gồm hai dòng:
    # Dòng đầu tiên hiển thị dict được nhập từ bàn phím
    # Dòng thứ hai hiển thị dict đã được sắp xếp theo giá trị key tăng dần

# in:   1 3 5 2 4
#       mot ba nam hai bon
# out:  {1: 'mot', 3: 'ba', 5: 'nam', 2: 'hai', 4: 'bon'}
#       {1: 'mot', 2: 'hai', 3: 'ba', 4: 'bon', 5: 'nam'}


def nhap_dict():
    try:
        key = list(map(int, input('nhap key: ').split()))
    except:
        print('key la so nguyen')
        return None
    
    value = input('nhap value: ').split()
    if len(key) != len(value):
        print('nhap so phtu cua key va value bang nhau')
        return None
    else:
        dictA = dict(zip(key, value))
        return dictA
    
def sapXep(dictA):
    #Su dung phuong thuc keys() de lay ra danh sach cac key cua dict
    #Su dung phuong thuc sorted() de sap xep cac key theo thu tu tang dan
    listKey = sorted(dictA.keys())
    dictKq = {}
    for i in listKey:
        dictKq[i] = dictA[i]
    return dictKq

dictA = nhap_dict()
if dictA is not None:
    kq = sapXep(dictA)
    print(dictA)
    print(kq)
    