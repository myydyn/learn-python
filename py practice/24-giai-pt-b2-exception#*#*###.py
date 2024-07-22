import math
with open('bai24.1.inp', 'r') as file_inp:
    type = file_inp.readline().split()
    print(type)
    ketluan = None
    if type == '1':
        pt_b1 = file_inp.readline()
        a, b = map(float, pt_b1.split())
        
        if a==0==b:
            ketluan = 'pt {}x {} = 0 có vô số nghiệm'.format(a,b)
        elif a==0 and b!=0:
            ketluan = 'pt {}x {} = 0 vô nghiệm'.format(a,b)
        elif b==0 and a!=0:
            ketluan = 'pt {}x {} = 0 có nghiệm là x=0'.format(a,b)
        else:
            ketluan = 'pt {}x {} = 0 có nghiệm là x={}'.format(a, b, -b/a)
    elif type == '2':
        pt_b2 = file_inp.readline()
        a, b, c = map(float, pt_b2.split())
        denta = b*b-4*a*c
        if a==0:
            if b==0:
                if c==0:
                    ketluan = 'pt {}x^2 {}x {} = 0 có vô số nghiệm'.format(a,b,c)
                else:
                    ketluan = 'pt {}x^2 {}x {} = 0 vô nghiệm'.format(a,b,c)
            elif b!=0:
                if c==0:
                    ketluan = 'pt {}x^2 {}x {} = 0 có nghiệm duy nhất là x=0'.format(a,b,c)
                else:
                    ketluan = 'pt {}x^2 {}x {} = 0 có nghiệm duy nhất là x={}'.format(a,b,c,-c/b)

        elif denta > 0:
            x1 = float(-b + math.sqrt(denta))/(2*a)
            x2 = float(-b - math.sqrt(denta))/(2*a)
            ketluan = 'pt {}x^2 {}x {} = 0 có 2 nghiệm phân biệt là:\n x1={};\nx2={}'.format(a,b,c,x1,x2)
        
        elif denta == 0:
            x = float(-b/2*a)
            ketluan = 'pt {}x^2 {}x {} = 0 có nghiệm kép là:\n x={}'.format(a,b,c,x)
        
        else:
            ketluan = 'pt {}x^2 {}x {} = 0 vô nghiệm'.format(a,b,c)
    elif FileNotFoundError:
        ketluan = 'lỗi k tìm thấy file'
    else:
        ketluan = 'có lỗi đầu vào'
with open('bai24.1.out', 'w') as file_out:
    file_out.write(ketluan)
