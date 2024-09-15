# Trả về dict kết quả đã sắp xếp theo giá trị VALUE tăng dần. 
# (Tham số là 1 dict)

# đầu vào
    # Gồm hai dòng:
    # Dòng đầu tiên chứa các phần tử của danh sách key. Các phần tử cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của danh sách value là các số nguyên. Các phần tử cách nhau bởi khoảng trắng
# đầu ra
    # Gồm hai dòng:
    # Dòng đầu tiên hiển thị dict được nhập từ bàn phím
    # Dòng thứ hai hiển thị dict đã được sắp xếp theo giá trị key tăng dần


def nhap_dict():
    lstKey = input('nhap chuoi key: ').split()
    try:
        lstValue = list(map(int, input('nhap chuoi value: ').split()))
    except:
        print('nhap so nguyen')
        return None
    if len(lstKey) != len(lstValue):
        print('Vui long nhap so luong key va value bang nhau!')
        return None
    dictA = dict(zip(lstKey, lstValue))
    return dictA

def sort_dict_by_value(dictA):
    # Chuyển từ điển dictA thành danh sách các cặp (key, value).
    listItem = dictA.items()
    lsItemSort = sorted(listItem, key=lambda item: item[1])
    dictKQ = dict(lsItemSort)
    return dictKQ

dictA = nhap_dict()

if dictA is not None:
    print(dictA)
    print(sort_dict_by_value(dictA))


# Ví dụ cụ thể giai thich LAMBDA:

# Giả sử từ điển ban đầu có dạng:
    # python
    # dictA = {'a': 5, 'b': 2, 'c': 8}

# Khi bạn gọi dictA.items(), nó trả về danh sách các cặp:
    # python
    # [('a', 5), ('b', 2), ('c', 8)]

# Giờ đây, sorted(listItem, key=lambda item: item[1]) sẽ hoạt động như sau:
    # item[1] là phần tử thứ hai của mỗi cặp, tức là các giá trị 5, 2, 8.
    # Hàm sorted() sẽ sắp xếp danh sách dựa trên các giá trị này. Kết quả sẽ là:
        # python
        # [('b', 2), ('a', 5), ('c', 8)]

# Danh sách sau khi sắp xếp được chuyển đổi lại thành từ điển:
    # python
    # {'b': 2, 'a': 5, 'c': 8}

