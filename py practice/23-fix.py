# ispossible = False
try:
    with open("bai23.1.inp", "r") as file_inp:
        doc_file1 = file_inp.readline()

    a, b, c = map(float, doc_file1.split())
    # ispossible = True

    # except FileNotFoundError:
    #    thongbao = 'k tìm thấy file input'

    # except:
    # thongbao = 'đầu vào k hợp lệ'

    # if ispossible:
    if a <= 0 or b <= 0 or c <= 0:
        thongbao = "các cạnh phải lớn hơn 0"
    elif (a + b) > c and a + c > b and c + b > a:
        aa = a * a
        if aa == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b:
            loaitamgiac = "vuông"
        elif a == b == c:
            loaitamgiac = "đều"
        elif a == b or b == c or a == c:
            loaitamgiac = "cân"
        elif a * a > b * b + c * c or b * b > a * a + c * c or c * c > a * a + b * b:
            loaitamgiac = "tù"
        else:
            loaitamgiac = "nhọn"
        thongbao = "{}, {}, {} la ba canh cua mot tam giac {}".format(
            a, b, c, loaitamgiac
        )
    else:
        thongbao = "{}, {}, {} kh la ba canh cua mot tam giac {}".format(a, b, c)

except FileNotFoundError:
    thongbao = "k tìm thấy file input"

except:
    thongbao = "đầu vào k hợp lệ"

with open("bai23.1.out", "w") as file_out:
    file_out.write(thongbao)
