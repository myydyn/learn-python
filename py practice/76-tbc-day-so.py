# Viết hàm với tham số truyền vào là một danh sách các số thực. 
# Trả về trung bình cộng của danh sách đó.
# vd: 5 6 3.6 7.8 || output: 5.6

def fight(lst):
    tong = sum(lst)
    soPhanTu = len(lst)
    trBinh = tong / soPhanTu
    return trBinh

lst = input('nhap cac so thuc, cach nhau 1 dau cach ').split()
if len(lst) == 0:
    print('danh sach rong')
else:
    try:
        #Ep kieu du lieu sang so thuc
        dsSo = list(map(float, lst))
        trBinh = fight(dsSo)
        print('trung binh cong cua day = {}'.format(trBinh))

    except:
        print('stupid')