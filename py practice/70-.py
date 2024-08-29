# Viết hàm với tham số truyền vào là chuỗi s. 
# Trả về tổng và trung bình cộng của các từ là số tự nhiên trong chuỗi s.
#VD: Toan 5 Ly 6 Hoa 7 ---> 18 \n 6.0

def tongTrungBinh(s):
    danhSachTu = s.split()
    
    dem = 0
    tong = 0
    
    for i in danhSachTu:
        if i.isdigit():
            tong += int(i)
            dem += 1

    if dem == 0:
        return 0, 0
    trungBinh = tong / dem
    return tong, trungBinh

s = input()
tong, trungBinh = tongTrungBinh(s)
print('tong = {}\ntrung binh cong = {}'.format(tong, trungBinh))