# đầu vào
    # Gồm hai dòng:
    # Dòng đầu tiên chứa các phần tử của set X, cách nhau bởi khoảng trắng
    # Dòng thứ hai chứa các phần tử của set Y, cách nhau bởi khoảng trắng

# đầu ra
    # Gồm hai dòng:
    # Dòng thứ nhất hiển thị các phần tử chứa trong set X mà không chứa trong set Y, cách nhau bởi khoảng trắng
    # Dòng thứ hai hiển thị các phần tử chứa trong set Y mà không chứa trong set X, cách nhau bởi khoảng trắng
# vd:
    # Kteam Free Chao Education
    # Education Nam Moi Free 2021
# output:
    # {'Kteam', 'Chao'}
    # {'2021', 'Moi', 'Nam'}

def money(x, y):
    justX  = x - y
    justY = y - x
    return justX, justY

x = set(input('nhap set x: ').split())
y = set(input('nhap set y: ').split())

justX, justY = money(x, y)
print(justX)
print(justY)
