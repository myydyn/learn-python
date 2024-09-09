# Viết hàm với tham số truyền vào là số tự nhiên n. 
# Trả về tuple gồm hai phần tử là: số tự nhiên n và tuple chứa n số tự nhiên n.
# vd: n = 5 || output: (5, (5, 5, 5, 5, 5))

def tuple_value(n):
    # tuple(n for _ in range(n)) là một comprehension để tạo ra một tuple.
    # Mỗi lần lặp, nó sẽ thêm giá trị n vào tuple.
    # Nếu muốn in "$" thay vì "n" thì code 'tuple("$" for _ in range(n))'
    ongGiaTri = tuple(n for _ in range(n))

    kq = (n, ongGiaTri)
    return kq

try:
    n = int(input('nhap n = '))
    if n < 0:
        print('n la so tu nhien')
    else:
        print(tuple_value(n))
except:
    print('dau vao k hop le')
    