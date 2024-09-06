# Viết hàm trả về danh sách gồm các phần tử không trùng lặp trong hai danh sách.
# vd: Kteam Free Chao Ban         || output: Kteam Chao Nam Moi 2021
#     Ban Nam Moi Free 2021       ||

def xoaTrung(s, m):
    sKhongm = [i for i in s if i not in m]
    mKhongs = [j for j in m if j not in s]
    gop = sKhongm + mKhongs
    return gop

s = input('nhap dong 1: ').split()
m = input('nhap dong 2: ').split()
if len(s) and len(m) == 0:
    print('ds rong')
else:
    rieng = xoaTrung(s, m)
    print(*rieng)


