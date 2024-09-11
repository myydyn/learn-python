# Viết hàm với tham số truyền vào là một set bất kỳ. 
# Trả về set sau khi đã xóa các phần tử chỉ chứa chữ số.
# in: 1 kteam2021 3 4 free 5 6 education 
# out: {'kteam2021', 'education', 'free'}

def xoa_ptu(s):
    m = s.copy()
    for i in s:
        if i.isdigit():
            m.remove(i)
    return m
s = input('nhap: ').split()
danhSach = set(s)
print(xoa_ptu(danhSach))

