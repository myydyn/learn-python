# Trả về dict gồm key là các ký tự và value là số lần xuất hiện của 
# ký tự trong chuỗi s. (Tham số là chuỗi S)
# in: Hello   || out: {'H': 1, 'e': 1, 'l': 2, 'o': 1}

def dict_list(s):
    dictS = {}
    for i in s:
        # Nếu ký tự i đã có trong dictS, giá trị của khóa đó sẽ được tăng lên 1.
        if i in dictS:
            dictS[i] += 1
        else:
            dictS[i] = 1
    return dictS

s = input('nhap chuoi s: ')
print(dict_list(s))
