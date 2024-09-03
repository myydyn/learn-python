# Viết hàm với tham số truyền vào là một danh sách các số nguyên. 
# Trả về danh sách các phần tử lẻ.
# vd: -2 -3 2 7 6 8 19 8 8 6 || output: -3 7 19

def pretty(D):
    # Sử dụng List Comprehension kết hợp với vòng lặp for
    soLe = [i for i in D if i %2 != 0]
    return soLe

danhSach = input('nhap day so: ').split()

if len(danhSach) == 0:
    print('danh sach rong')
else:
    try:
        D = list(map(int, danhSach))
        sole = pretty(D)
        #Unpacking arguments
        print(*sole)

    except:
        print('pla...pla...pla')
