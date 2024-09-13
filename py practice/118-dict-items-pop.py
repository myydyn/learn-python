# Trả về dict kết quả sau khi loại bỏ các phần tử 
# có value trùng nhau (Tham số là 1 dict)

# đầu vào
    # Gồm hai dòng:
    # Dòng đầu tiên chứa các phần tử của danh sách key. Các phần tử cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của danh sách value. Các phần tử cách nhau bởi khoảng trắng
# đầu ra
    # Gồm một dòng duy nhất hiển thị dict theo yêu cầu đề bài

# in:   1 2 3 4 5
#       1 1 2 2 3
# out: {'1': '1', '3': '2', '5': '3'}

def nhap_dict():
    listKey = input('nhap key: ').split()
    listValue = input('nhap value: ').split()
    if len(listKey) != len(listValue):
        print('nhap sl key value bang nhau')
        return None
    kq = dict(zip(listKey, listValue))
    return kq

def xoa_trung(dictA):
    # Sử dụng danh sách listValue để lưu trữ các value
    listValue = list()
    #Su dung phuong thuc copy de copy cac phan tu cua dictA
    dictKq = dictA.copy()
    # vòng lặp for và phương thức items() để duyệt qua các phần tử của dict kết quả.
    for key, value in dictA.items():
        if value in listValue:
            #Su dung phuong thuc pop de bo di phan tu co key
            dictKq.pop(key)
        else:
            listValue.append(value)
    return dictKq
# đoạn hàm này tư duy sẽ là 

dictA = nhap_dict()
if dictA is not None:
    print(xoa_trung(dictA))
