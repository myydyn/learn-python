# cách k mở file mà nhập từ phím
#print('Your name: ')
#name = input()
#print('Your age: ')
#age = int(input())

#print('In 20 years later', name, "'s age is", (age + 20))
#print('Vao 20 nam nua, tuoi cua {} se la {}'.format(name, age + 20))

#-------------------

with open('Bai1.10.inp', 'r') as Inp_file: # with_open_as: mở file có sẵn, đọc lệnh read 'r', và hành động sau 'as'
    name = Inp_file.readline().rstrip('\n') #readline: đọc 1 dòng, rstrip(\n) loại bỏ ký tự xuống dòng
    age = int(Inp_file.readline()) #readline; ép kiểu

with open('Bai1.10.out', 'w') as Out_file: # 'w' write: tạo file mới
    Out_file.write('Vao 20 nam nua tuoi cua {} se la {}'.format(name, age + 20))

#--------------------

# BAI MAU
    #Mo file voi mode='r' de doc file
    #with open('Bai1.10.inp', 'r') as fileInp:

    #Doc 1 dong du lieu tu file va luu vao bien ten
    #Su dung phuong thuc rstrip de loai bo ky tu xuong dong '\n'
    #ten = fileInp.readline().rstrip('\n')

    #Doc 1 dong du lieu tu file va luu vao bien tuoiHienTai
    #tuoiHienTai = int(fileInp.readline())

    #Mo file voi mode='w' de ghi file
    #with open('Bai1.10.out', 'w') as fileOut:

    #Ghi noi dung vao file theo mau
    #fileOut.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))