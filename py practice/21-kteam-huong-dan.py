#Nhap so do ba canh tu ban phim
#Su dung ham map() va float de ep kieu du lieu sang so thuc
a, b, c = map(float, input().split())

#Dung cau lenh re nhanh de kiem tra dieu kien cac tam giac
#Kiem tra dieu kien la ba canh cua tam giac
if a+b>c and a+c>b and b+c>a:
   #Kiem tra tam giac vuong
   if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
       loaiTamGiac = 'vuong'
   #Kiem tra tam giac deu
   elif a==b and b==c:
       loaiTamGiac = 'deu'
   #Kiem tra tam giac can
   elif a==b or a==c or b==c:
       loaiTamGiac = 'can'
   #Kiem tra tam giac tu
   elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
       loaiTamGiac = 'tu'
   #Cac truong hop con lai la tam giac nhon
   else:
       loaiTamGiac = 'nhon'
   #Xuat thong bao theo yeu cau
   print('{}, {}, {} la ba canh cua mot tam giac {}'.format(a, b, c, loaiTamGiac))
else:
   print("{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c))
