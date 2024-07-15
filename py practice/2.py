## CAU TRUC 'TRY' - 'EXCEPT'

try:
    print('nhap so 1st')
    so_1 = int(input())
    print('nhap so 2nd')
    so_2 = int(input())
    tong = so_1 + so_2
    print('tong 2 so vua nhap la', tong)

except:
    print('gia tri khong phu hop aka it is not suitable')