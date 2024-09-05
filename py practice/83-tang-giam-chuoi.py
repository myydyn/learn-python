# Viết hàm với tham số truyền vào là một danh sách và số tự nhiên n. 
# Trả về danh sách có n phần tử bằng cách lặp lại các phần tử trong danh sách được truyền vào.
# vd: "1 hai 3 bon nam" VÀ n = 7 || output: 1 hai 3 bon nam 1 hai

def yeuCau(s, n):
    #Su dung ham len() de lay so luong phan tu cua danh sach
    soPhanTu = len(s)
    #Tinh toan so lan toi thieu can lap lai danh sach
    chenhLech = int(n // soPhanTu) + 1
    #Su dung toan tu * de lap danh sach voi so lan mong muon
    chuoiMoi = s*chenhLech
    #Cat danh sach cho dung n phan tu
    dieuChinh = chuoiMoi[:n]
    return dieuChinh

# Dùng hàm input() và hàm split() để
# nhập và cắt chúng thành danh sách các phần tử
s = input('Nhap chuoi: ').split()
if len(s) == 0:
    print('DS rong')
else:
    try:
        n = int(input('Nhap do dai chuoi n = '))
        chuoiMoi = yeuCau(s, n)
        print(*chuoiMoi)
    except:
        print('loi')
        