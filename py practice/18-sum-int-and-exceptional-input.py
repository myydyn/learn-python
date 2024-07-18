try:
    print('nhập phép tính với các phần tử cách nhau 1 khoảng trắng')
    a, phetinh, b = input().split()
    a = float(a)
    b = float(b)
    
    ketqua = None

    if phetinh == '+':
        ketqua = a+b

    elif phetinh == '-':
        ketqua = a-b

    elif phetinh == '*':
        ketqua = a*b
        
    elif phetinh == ':':
        if b == 0:
            print('so chia phai khac 0')
        else:
            ketqua = a/b
    
    if ketqua != None:
        print("{} {} {} = {}".format(a, phetinh, b, ketqua))    
except:
    print('đầu vào k hợp lệ')
