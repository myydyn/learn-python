# Viết hàm trả về list các ký tự theo thứ tự 
# đảo ngược của chuỗi s. (Với tham số là chuỗi s)
# vd: 

def backForWard(s):
    #Su dung constructor list de khoi tao list tu chuoi
    letterList = list(s)
    letterReverse = letterList[::-1]
    return letterReverse

s = input('nhap chuoi s: ')
letterReverse = backForWard(s)
#Su dung Unpacking arguments de hien thi danh sach
print(*letterReverse)