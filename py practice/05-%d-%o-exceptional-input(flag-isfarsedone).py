#print('nhap vao mot so')

#try:
#    p1 = int(input())
#    print('So thap phan %d trong he bat phan la %o' % (p1, p1))

#except:
#    print('dau vao k hop le')


# ĐẶT CỜ ISPARSEDONE
print('nhap vao mot so')
isFarseDone = False
try:
    p1 = int(input())
    isFarseDone = True

except:
    print('dau vao k hop le')

if isFarseDone:
    print('So thap phan %d trong he bat phan la %o' % (p1, p1))