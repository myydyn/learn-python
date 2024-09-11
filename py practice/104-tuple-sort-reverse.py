# Viết hàm với tham số truyền vào là một tuple các số thực. 
# Viết hàm trả về tuple đã được sắp xếp theo thứ tự giảm dần.
# input: 5 6 9 1.23 -5 10 0
# output: (10.0, 9.0, 6.0, 5.0, 1.23, 0.0, -5.0)

def tup_decrease(tupX):
    # cấu trúc sắp xếp bằng hàm sorted(giaTri, reverse=True), reverse: giảm
    kq = tuple(sorted(tupX, reverse=True))
    return kq

try:
    tupX = tuple(map(float, input('nhap: ').split()))
    print(tup_decrease(tupX))
except:
    print('dau vao k hop le')

# hàm sort đảo ngược có thể code như sau: tupX.sort(reverse=True)