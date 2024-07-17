# bài tự làm bị LỖI, output sai yêu cầu
#try:
#    with open('bai1.11.inp', 'r') as inp_file:
#
#        try:
#            name = inp_file.readline().split('\n')
#            age = int(inp_file.readline())

#            with open('bai1.11.out', 'w') as out_file:
#                out_file.write('Vao 20 nam nua, tuoi cua {} se la {}'.format(name, age + 20))
#        except:
#            print('dau vao k hop le')

#except:
#    print('k tim thay file')

# bài hướng dẫn
try:
    with open('bai1.11.inp', 'r') as inp_file:
        name = inp_file.readline().rsplit('\n')
        age = int(inp_file.readline())

    with open('bai1.11.out', 'w') as out_file:
        out_file.write('{} 20 năm nữa sẽ {} tuoi'.format(name, age + 20))

except FileNotFoundError:
    with open('bai1.11.out', 'w') as out_file:
        out_file.write('k tim thay file')

except:
    with open('bai1.11.out', 'w') as out_file:
        out_file.write('dau vao k hop le')