# Viết hàm với tham số truyền vào là chuỗi s. 
# Trả về số lượng chữ số, số lượng ký tự, số lượng ký hiệu và chuỗi s 
# được sắp xếp thành ba phần theo thứ tự chữ số, ký tự, ký hiệu.

# VD: --Kteam-- 1000++ Khoa hoc 
# output: 
        # 4
        # 12
        # 9
        # 1000KteamKhoahoc---- ++ 

def digitCharSymbol(s):
    # tachChuoi = s.split()
    chuSo = ''
    kyTu = ''
    kyHieu = ''

    for i in s:
        if i.isdigit():
            chuSo += i
        if i.islower() or i.isupper():
            kyTu += i
        else:
            kyHieu += i
    chuoiMoi = chuSo + kyTu + kyHieu
    return len(chuSo), len(kyTu), len(kyHieu), chuoiMoi

s = input()
chuSo, kyTu, kyHieu, chuoiMoi = digitCharSymbol(s)
print('SL digit = {}\nSL character = {}\nSl symbol = {}\nChuoi moi: {}'.format(chuSo, kyTu, kyHieu, chuoiMoi))