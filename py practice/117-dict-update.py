# Trả về dict kết quả sau khi cập nhật dict có số phần tử ít hơn 
# cho dict có phần tử nhiều hơn. (Tham số là 2 dict). nếu dict bé có cùng key
# với dict lớn thì dict bé sẽ được cập nhật value cho các key trùng đó và thêm vào các cặp key-value chưa có

# in: 
    # key dict1:        1 2 3 4
    # value dict1:      m h b b
    # key dict1:        a b c
    # value dict1:      11 12 13
# out: {'1': 'm', '2': 'h', '3': 'b', '4': 'b', 'a': '11', 'b': '12', 'c': '13'}


def nhap_dic():
    listKey = input('nhap key: ').split()
    listValue = input('nhap value: ').split()

    if len(listKey) != len(listValue):
        print('Vui long nhap so luong key va value bang nhau!')
        return None
    
    dictKq = dict(zip(listKey, listValue))
    print(dictKq)
    return dictKq

def update_dic(dictA, dictB):
    if len(dictA) < len(dictB):
        dictB.update(dictA)
        return dictB
    dictA.update(dictB)
    return dictA
dictA = nhap_dic()
dictB = nhap_dic()

if dictA is not None and dictB is not None:
    kq = update_dic(dictA, dictB)
    print(kq)

