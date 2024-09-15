# kiểm tra xem các từ trong 1 chuỗi đó có tồn tại trong từ điển không. 
# Nếu có, thay thế bằng giá trị (value) tương ứng từ từ điển, 
# nếu không thì giữ nguyên. (Tham số là 1 chuỗi & 1 dict)
# đầu vào
    # Gồm ba dòng:
        # Dòng đầu tiên chứa chuỗi cần thay thế.
        # Dòng thứ hai chứa các phần tử của danh sách key. Các phần tử cách nhau bởi khoảng trắng
        # Dòng thứ ba chứa các phần tử của danh sách value. Các phần tử cách nhau bởi khoảng trắng

# đầu ra
#   Gồm hai dòng:
        # Dòng đầu tiên hiển thị dict các từ thay thế.
        # Dòng thứ hai hiển thị chuỗi sau đi đã thay thế theo yêu cầu đề bài

# in:   hai khong hai mot
#       khong mot hai ba bon nam sau
#       0 1 2 3 4 5 6

# out:  {'khong': '0', 'mot': '1', 'hai': '2', 'ba': '3', 'bon': '4', 'nam': '5', 'sau': '6'}
#       2 0 2 1


def nhap_dict():
    listKey = input('nhap chuoi key: ').split()
    listValue = input('nhap chuoi value: ').split()
    if len(listKey) != len(listValue):
        print('so luong key-value phai bang nhau')
        return None
    
    dictA = dict(zip(listKey, listValue))
    return dictA

def thay_the(chuoiCanThayThe, dictA):
    listChuoi = chuoiCanThayThe.split()
    listKQ = []
    for i in listChuoi:
        #i đầu tiên là khóa đc tìm kiếm trong từ điển dictA. 
        # Nếu i tồn tại trong dictA, nó sẽ trả về giá trị-vâlue tương ứng với khóa i.

        # i thứ hai là giá trị mặc định (nếu k nhập mặc định là None), 
        # sẽ được trả về giá trị chuỗi ban đầu nếu không trùng với key của dictionary.
        listKQ.append(dictA.get(i,i))
    chuoiKQ = ' '.join(listKQ)
    return chuoiKQ

chuoiCanThayThe = input('nhap chuoi can thay the: ')
dictA = nhap_dict()
print(dictA)
print(thay_the(chuoiCanThayThe, dictA))

