# Định dạng đầu vào
# Gồm 1+M dòng:
    # Dòng đầu tiên chứa hai giá trị M, N cách nhau bởi khoảng trắng.
    # M dòng tiếp theo, mỗi dòng chứa N phần tử, các phần tử cách nhau bởi khoảng trắng
# Định dạng đầu ra
    # Gồm M dòng, mỗi dòng hiển thị N phần tử của danh sách. 
    # Các phần tử cách nhau bởi khoảng trắng.

# Ví dụ: Input 1:            ||Output 1: 
#1    3 4                    ||       N N N N     
#2    N N N N                ||       nam sau bay tam
#3    nam sau bay tam        ||       9 muoi 11 12
#4    9 muoi 11 12           ||

def nhapDanhSach(m, n):
    hang = []
    for i in range(m):
        i = input().split()
        if len(i) != n:
            print('so luong phan tu trong hang phai = n')
            return None
        hang.append(i)
    return hang

def inDanhSach(danhSach):
    if danhSach:
        for i in danhSach:
            print(*i)

try:
    m, n = map(int, input('nhap m n = ').split())
    if m <= 0 or n <= 0:
        print('m va n phai nguyen duong')
    else:
        danhSach = nhapDanhSach(m, n)
        if danhSach is not None:
            inDanhSach(danhSach)
    
except:
    print('loi du lieu dau vao')
    