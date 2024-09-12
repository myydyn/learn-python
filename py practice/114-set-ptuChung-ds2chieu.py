# Trả về set các phần tử xuất hiện ở tất cả các hàng. 
# (Với tham số là danh sách 2 chiều MxN)

# đầu vào
    # Dòng đầu tiên chứa hai giá trị M, N cách nhau bởi khoảng trắng.
    # M dòng tiếp theo, mỗi dòng chứa N phần tử, các phần tử cách nhau bởi khoảng trắng

# đầu ra
    # 1 dong hiển thị set các phần tử xuất hiện ở tất cả các hàng, 
    # các phần tử cách nhau bởi khoảng trắng.
# input:
    # 3 5
    # Kteam chao nam moi 2021 
    # How Kteam 2021 Chuc mung 
    # Chao mung Kteam nam 2021
# output
    # {'2021', 'Kteam'}

def fighting(m, n):
    danhSach = []
    for i in range(m):
        hang = input('nhap cac hang: ').split()
        # kiem tra so phtu trong moi hang co = n ko (so cot da nhap ban dau)
        if len(hang) != n:
            print('Danh sach 2 chieu khong dung kich thuoc')
            return None
        danhSach.append(hang)
    return danhSach

def set_ptu_chung(danhSach):
    # Biến setHang0 lưu trữ tập hợp các phần tử của hàng đầu tiên.
    setHang0 = set(danhSach[0])
    #Phương thức intersection() được sử dụng để lấy giao của setHang0 
    # với tất cả các hàng còn lại trong danh sách (danhSach).
    #Su dung list comprehension de liet ke cac hang
    #Su dung ky thuat Unpacking agruments de truyen nhieu tham so cho ham
    setPtuChung = setHang0.intersection(*[hang for hang in danhSach])
    return setPtuChung

try: 
    m, n = map(int, input('nhap m va n: ').split())
    if m <= 0 or n <= 0:
        print('kich thuoc danh sach la so nguyen duong!')
    else:
        danhSach2chieu = fighting(m, n)
        if danhSach2chieu is not None:
            setPtuChung = set_ptu_chung(danhSach2chieu)
            print(setPtuChung)
except:
    print('k hop le')
