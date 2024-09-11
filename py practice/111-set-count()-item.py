# Hiển thị số lần xuất hiện của các ký tự trong chuỗi s. 
# (Với tham số là chuỗi s).
# in: Hello
# out: hiển thị theo định dạng “‘{ký tự}’: {số lần xuất hiện}; ”
#     'H': 1; 'e': 1; 'l': 2; 'o': 1;

def dem_ky_tu(s):
    kyTu = set(s)
    for i in kyTu:
        dem = s.count(i)
        print("'{}': {}; ".format(i, dem), end='')

s = input('nhap: ')
dem_ky_tu(s)
