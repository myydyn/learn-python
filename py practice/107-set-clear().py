# Viết hàm với tham số truyền vào là một set bất kỳ. 
# Trả về set rỗng nếu set có chẵn phần tử.

def set_condition(s):
    if len(s) % 2 == 0:
        s.clear()
    return s

s = input('nhap: ').split()
if len(s) == 0:
    print('ds rong')
else:
    tapHop = set(s)
    kq = set_condition(tapHop)
    print(kq)
