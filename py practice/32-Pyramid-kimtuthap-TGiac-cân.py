is_it = False
try:
    n = int(input('enter a negative number not zero: n= '))
    is_it = True
except:
    print('invalid input')

if is_it:
    if n<0:
        print('pls enter a negative value')
    else:
        A_ASCII_code = 65
        for i in range(n):
             #Tinh toan khoang trang dau moi dong
            space = " "*(((n-i)*2)-1)
            print(space, end=' ')
            #Su dung vong lap for de in cac ky tu tren mot dong
            for j in range(2*i+1):
                #Chuyen tu ma ascii sang ky tu
                letter = chr(A_ASCII_code)
                print(letter, end=' ')
                #Tang ma ascii len 1 de duyet ky tu tiep theo
                A_ASCII_code +=1
                #Neu ky tu vuot qua chu Z thi quay lai ky tu A ban dau
                if chr(A_ASCII_code) > 'Z':
                    A_ASCII_code = 65
            print()

# bài toán in có thể chia thành 2 phần cơ bản:
# 1. Phần thứ nhất là [in các khoảng trắng bên TRÁI các chữ cái] + phần thứ 2 là [in các chữ cái]
#vòng lặp FOR thứ nhất có biến i là để in các KHOẢNG TRẮNG
#vòng lặp FOR thứ 2 có biến j là để in các CHỮ CÁI, và nó nằm bên TRONG vòng I
#trong LOOP thứ nhất có biểu thức:
    #space = " "*(((n-i)*2)-1) 
        # có (n-i)*2, nhân 2 là vì khi i tăng dần và n không đổi thì SL các chữ cái tăng dần, mà mỗi chữ cái tương ứng với 2 khoảng trắng (chỗ end=' ' phía dưới có thêm 1 space giữa chúng) nên phải X2 lên
        # có thể không cần trừ 1 phía sau, hình Pyramid chỉ dịch vào 1 vị trí so với có trừ 1