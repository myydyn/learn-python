# Trả về set sau khi đã thêm các phần tử của list. 
# (Với tham số là 1 set & 1 list bất kỳ)
# in: 1 2 3 4 5      || out: {'5', '4', '2', '7', '3', '6', '1'}
#     1 1 2 2 6 6 7  ||

def add_set(s, m):
    for i in m:
        s.add(i)
    return s

s = set(input('nhap cac phtu cua set: ').split())
m = list(input('nhap cac phtu cua list: ').split())

print(add_set(s, m))
