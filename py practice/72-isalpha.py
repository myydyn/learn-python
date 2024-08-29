# Viết hàm với tham số truyền vào là chuỗi s. 
# Trả về số lượng từ vừa chứa ký tự, vừa chứa chữ số trong chuỗi s.
# VD: --Kteam-- **1** _K2_Team >> output: 1

def money(s):
    moon = s.split()
    dem = 0
    for word in moon:
        digit = False
        char = False

        for letter in word:
            if letter.isdigit():
                digit = True
            if letter.isalpha():
                char = True
        if digit and char:
            dem += 1
            
    return dem

s = input('nhap s: ')

print('so luong = {}'.format(money(s)))