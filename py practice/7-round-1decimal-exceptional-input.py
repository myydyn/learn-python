isFarseDone = False
print('nhap mot so thap phan D tu ban phim')
so1 = input()
print('nhap so chu so thap phan ban muon lam tron')
so2 = input()

try:
    D = float(so1)
    m = int(so2)
    #print('so sau khi lam tron la: ' '{0:.{1}f}'.format(D, m))
    isFarseDone = True

except:
    print('dinh dang dau vao k hop le')

if isFarseDone:
    print('so sau khi lam tron la: ' '{0:.{1}f}'.format(D, m))