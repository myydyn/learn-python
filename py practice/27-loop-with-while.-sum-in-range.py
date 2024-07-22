is_right = False
print('nhap a va b')
try:
    a = int(input())
    b = int(input())
    is_right = True
except:
    print('dau vao k hop le')    

if is_right:
    if a> b:
        print('a k được lớn hơn b')
    else:
        i = a
        total = 0
        while i <= b:
            #i += 1  #k được tăng i trước phép toán cho total, phải total trước mới xong 1 vòng lặp. Sau đó mới bắt đầu giá trị mới của i
            total += i
            i += 1
        print(total)
            