try:
    print('nhap a va b')
    a = int(input())
    b = int(input())
    if a>b:
        print('So thu nhat k được lon hon so thu hai!')
    else:
        tong = 0
        for i in range(a,b+1):
            tong += i
        print('tong cac so trong khoang a va b là: ',tong)
except:
    print('có lỗi đầu vào')