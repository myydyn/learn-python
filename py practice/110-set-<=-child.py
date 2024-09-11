# Kiểm tra set Y có là tập con của setX hay không. 
# (Với tham số là setX; Set Y bất kỳ)
# đầu ra: hiển thị True nếu set Y là tập con của set X. Ngược lại hiển thị False
# in: kteam 2021 free education
#     2021 education
# out: True

def set_con(x, y):
    # Trong Python, toán tử <= giữa hai tập hợp có nghĩa là kiểm tra 
    # xem tất cả các phần tử của tập hợp y có nằm trong tập hợp x 
    # hay không. Nếu đúng, kết quả là True, ngược lại là False.
    return y <= x
x = set(input('nhap x: ').split())
y = set(input('nhap y: ').split())

print(set_con(x, y))
