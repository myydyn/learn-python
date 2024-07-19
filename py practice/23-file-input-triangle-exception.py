with open('bai23.1.inp', 'r') as file_inp:
    doc_file = file_inp.readline().rsplit('\n')
a, b, c = map(float, doc_file.split())
loaitamgiac = None
if a<=0 or b<=0 or c <=0:
    thongbao = 'phai lon hon 0'
    
    if (a+b)>c and (a+c)>b and (b+c)>a:
        if a==b==c:
            loaitamgiac = 'đều'
        elif a==b or b==c or a==c:
            loaitamgiac = 'cân'
        elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
            loaitamgiac = 'vuông' 
        else:
            loaitamgiac = 'thường'
    if loaitamgiac != None:
        with open('bai23.1.out', 'w') as out_file:
            out_file.write(loaitamgiac)
        
    else:
        with open('bai23.1.out', 'w') as file_out:
            file_out.write('co loi đầu vào')




print('{}, {}, {} là 3 cạnh tam giác'.format(a,b,c))