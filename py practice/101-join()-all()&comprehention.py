# Viết hàm với tham số truyền vào là một tuple các phần tử chỉ bao gồm chữ số. 
# Trả về số nguyên được tạo ra từ các phần tử theo thứ tự trong tuple đó.
# vd input: 0 0 00 12 3 00  || output: 12300

def tuple_to_int(tupleX):
    # ghép lại thành một chuỗi duy nhất bằng hàm ''.join(tupleX).
    # chuỗi sẽ được chuyển thành một số nguyên bằng hàm int(). 
    number = int(''.join(tupleX))
    return number

X = input('nhap: ').split()
# Hàm isdigit() được gọi trên từng phần tử trong danh sách X để kiểm tra 
# xem mỗi phần tử có phải là chuỗi chỉ bao gồm các ký tự số không. 
# Hàm all() sẽ trả về True nếu tất cả các phần tử trong danh sách đều là số, ngược lại sẽ trả về False.
kiemTraDauVao = all(i.isdigit() for i in X)

if kiemTraDauVao:
    ketQua = tuple_to_int(X)
    print(ketQua)
else:
    print('Dinh dang dau vao khong hop le!')
