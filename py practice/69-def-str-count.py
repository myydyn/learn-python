# 68-Viết hàm truyền vào tham số là chuỗi s. Hiển thị số lần xuất hiện của các ký tự trong chuỗi s.
# VD Input 1: Hello --> Output 1: 'H': 1; 'e': 1; 'l': 2; 'o': 1;

def kyTuKoTrung(s):
    kq = ''
    for i in s:
        if i not in kq:
            kq += i
    return kq

def demKyTu(s):
    chuoiKoTrung = kyTuKoTrung(s)
    for i in chuoiKoTrung:
        dem = s.count(i)
        print(" '{}': {}; ".format(i, dem), end=' ')

print('nhap chuoi s: ')
s = input()

print('so lan xuat hien cua cac ky tu la: ')
demKyTu(s)
