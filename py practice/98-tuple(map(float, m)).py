# Viết hàm với tham số truyền vào là một tuple gồm các số thực. 
# Trả về giá trị lớn nhất, giá trị nhỏ nhất, số phần tử của tuple.
# vd input: -2.5 7 9 0       || output: 9.0
#                                       -2.5
#                                       4

def tupleSoThuc(m):
    return max(m), min(m), len(m)

m = input('nhap cac so thuc: ').split()
try:
    if len(m) == 0:
        print('ds rong')
   
    else:
        ong = tuple(map(float, m))
        kq = tupleSoThuc(ong)
        print(*kq, sep='\n')

except:
    print('Vui long nhap cac phan tu la so thuc!')
  