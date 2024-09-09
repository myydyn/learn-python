# Viết hàm với tham số truyền vào là một tuple gồm các số thực. 
# Trả về giá trị lớn nhất, giá trị nhỏ nhất, số phần tử của tuple.
# vd input: -2.5 7 9 0       || output: 9.0
#                                       -2.5
#                                       4

def tupleSoThuc(m):
    lonNhat = max(m)
    nhoNhat = min(m)
    so = len(m)
    return lonNhat, nhoNhat, so

m = input('nhap cac so thuc: ').split()
try:
    if len(m) == 0:
        print('ds rong')
   
    else:
        ong = tuple(map(float, m))
        lonNhat, nhoNhat, dai = tupleSoThuc(ong)
        print(lonNhat)
        print(nhoNhat)
        print(dai)

except:
    print('Vui long nhap cac phan tu la so thuc!')
  