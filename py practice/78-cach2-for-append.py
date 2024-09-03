# Viết hàm với tham số truyền vào là một danh sách các số nguyên. 
# Trả về danh sách các phần tử lẻ.
# vd: -2 -3 2 7 6 8 19 8 8 6 || output: -3 7 19

def cool(gour):
    sole = []
    for i in gour:
        if i%2 !=0:
            sole.append(i)
    return sole

gour = input('nhap day so: ').split()
if len(gour)==0:
    print('danh sach rong')
else:
    try:
        danhSach = list(map(int, gour))
        sole = cool(danhSach)
        print('day so le: {}'.format(sole))
    except:
        print('pla..pla')
