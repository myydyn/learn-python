# Viết hàm với tham số truyền vào là một danh sách hai chiều (dài x rộng) kích thước MxN. 
# Trả về danh sách phần tử có độ dài lớn nhất của mỗi hàng. 
# vd:   3 4                         || output: Kteam Chuc khang
#       Kteam chao nam 2021         ||
#       Chuc mung nam moi           ||
#       An khang thinh vuong        ||

def nhapDanhSach(m, n):
    danhSachDaiRong = []
    for i in range(m):
        #Nhap du lieu moi hang tu ban phim va cat thanh list cac phan tu
        # tạo ra list gồm m phần tử tương ứng m hàng
        hang = input().split()   
        #Kiem tra kích thước các hàng xem có bằng n không
        if len(hang) != n:
            print('cac hang khong cung kich thuoc')
            return None
        danhSachDaiRong.append(hang)
    return danhSachDaiRong

def phTuDaiNhat(s):
    #Su dung List Comprehension liet ke Danh sach do dai cac phan tu
    dsDoDai = [len(d) for d in s]
    #Tim phan tu dai nhat
    maxDoDai = max(dsDoDai)
    #Tim vi tri dau tien cua phan tu dai nhat
    viTriMaxDoDai = dsDoDai.index(maxDoDai)
    #Tra ve gia tri phan tu dai nhat
    return s[viTriMaxDoDai]

def phTuDaiNhatMoiHang(danhSachDaiRong):
    # Tạo một danh sách mới chứa các phần tử dài nhất của mỗi hàng
    dsPhTuDaiNhatMoiHang = [phTuDaiNhat(hang) for hang in danhSachDaiRong]
    return dsPhTuDaiNhatMoiHang

# chuong trinh chinh nhap lieu
try:
    m, n = map(int, input('nhap m n: ').split())
    if m <= 0 or n <= 0:
        print('m va n nguyen duong')
    else:
        # Nhap danh sach tu nguoi dung
        danhSachDaiRong = nhapDanhSach(m, n)
        if danhSachDaiRong:
            # Tìm và in danh sách các phần tử dài nhất trong mỗi hàng
            ketQua = phTuDaiNhatMoiHang(danhSachDaiRong)
            print(*ketQua)
except:
    print('dau vao k hop le')