# Viết hàm trả về list số tự nhiên và list bình phương 
# các số tự nhiên nhỏ hơn n (Với n là tham số tự nhiên)
# VD: 6 >> output 
                # 0 1 2 3 4 5
                # 0 1 4 9 16 25


def money(n):
    #Khoi tao list su dung List Comprehension
    list = [i for i in range(n)]
    square = [i*i for i in range(n)]
    return list, square

try:
    n = int(input('nhap n = '))
    if n < 0:
        print('n has to greater than 0, pls replay')
    else:
        list, square = money(n)
        print('{}\n{}'.format(list, square))

except:
    print('invalid input, pls replay')