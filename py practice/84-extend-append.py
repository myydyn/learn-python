# Viết hàm với tham số truyền vào là một danh sách và số nguyên dương n. 
# Trả về danh sách kết quả bằng cách chèn phần tử “Kteam” vào các VI TRI chia hết cho n.
# vd: '1 2 3 4 5 6 7 8' n=3  || output: 1 2 3 Kteam 4 5 6 Kteam 7 8

def themPhanTu(s, n):
    kq = []
    #Duyet cac phan tu cua danh sach voi buoc nhay la n
    for i in range(0, len(s), n):
        #Ham extend() them tung phan tu cua mot iterable vao cuoi danh sach
        # thêm vào ds kq rỗng các phần tử từ i đến (i+n) bỏ khúc sau, các lần lặp sau tương tự gom lại là đủ, xong có dư chữ cuối phải pop nó ra
        # kiểu là ghép từng đoạn, từng khúc với nhau. Đoạn này chỉ mới cắt nhỏ chuỗi s ban đầu chưa thêm 'kteam' vào
        kq.extend(s[i:i+n])
        #Ham append() them phan tu 'kteam' vao cuoi danh sach
        kq.append('kteam')
    #Ham pop() bo di mot phan trong dach sach, mac dinh la phan tu cuoi cung
    kq.pop()
    return kq

s = input('Nhap chuoi: ').split()
if len(s) == 0:
    print('ds rong')
else:
    try:
        n = int(input('nhap n = '))
        kq =  themPhanTu(s, n)
        print(*kq)
    except:
        print('loi')

