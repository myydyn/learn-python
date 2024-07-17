print('nhap chuoi la 1 day so, cach nhau 1 dau cach')
chuoi_day_so = input()
tach_chuoi = chuoi_day_so.split()
#isFarseDone = False
try:
#    tach_chuoi = chuoi_day_so.split()
    ep_kieu_so = map(int, tach_chuoi)
    tong = sum(ep_kieu_so)
    print('tong la', tong)
#    isFarseDone = True
except:
    print('k hop le')

#if isFarseDone:
#    print('tong la', sum(tong))
