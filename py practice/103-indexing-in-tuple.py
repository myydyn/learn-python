# Viết hàm với tham số truyền vào là tuple X, tuple Y, số nguyên dương k.
# Trả về tuple kết quả bằng cách thêm các phần tử của tuple Y vào vị trí k của tuple X.
# vd: input
        # 0 1 2 3 4
        # kteam 2021
        # 3
# output: ('0', '1', '2', 'kteam', '2021', '3', '4')


def chen(tupX, tupY, k):
    # Sử dụng Indexing và cắt tuple để thực hiện yêu cầu đề bài
    kq = tupX[:k] + tupY + tupX[k:]
    return kq
x = input('nhap tuple X: ').split()
y = input('nhap tuple Y: ').split()
tupX = tuple(x)
tupY = tuple(y)

# tupX = tuple(input('nhap tuple X: ').split())

try:
    k = int(input('nhap k = '))
    if k < 0 or k > len(tupX):
        print('k nguyen duong va nho hon hoac bang so phan tu cua tuple X!')
    else:
        print(chen(tupX, tupY, k))
except:
    print('Dinh dang dau vao khong hop le!')
    