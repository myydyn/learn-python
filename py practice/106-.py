# Viết hàm với tham số truyền vào là một set gồm các số thực. 
# Trả về giá trị lớn nhất, giá trị nhỏ nhất và tổng các phần tử của set.
# in:  -2.5 7 9 0
# out:  9.0
#       -2.5
#       13.5

def set_off(s):
    return max(s), min(s), sum(s)

s = input('nhap: ').split()
if len(s) == 0:
    print('ds rong')
else:
    try: 
        epKieu = set(map(float, s))
        kq = set_off(epKieu)
        print(epKieu)
        print(*kq, sep='\n')

    except:
        print('loi nhap lieu')
