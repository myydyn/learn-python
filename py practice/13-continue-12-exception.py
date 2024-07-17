try:
    with open('bai1.13.inp', mode='r') as inp_file:
        #lst = inp_file.read().splitlines()
        lst = inp_file.read().split()
        str = ' '.join(lst)

    with open('bai1.13.out', mode='w') as out_file:
        out_file.write(str)

except FileNotFoundError:
    with open('bai1.13.out', mode='w') as out_file:
        out_file.write('k tìm thấy file')


#link to search more about 'split' https://chatgpt.com/share/33ed0879-044e-4dbb-92b1-4abf0bcd5aaa
# To sum up:
    #slpit: tách chuỗi thành các phần tử, cú pháp: str.split(sep=None, maxsplit=-1)
        #trong đó: 
            #str: chuỗi cần tách; 
            #sep=None(optinal): dấu hiệu tách, nếu k nhập mặc định là space
            #maxsplit=-1(optional): muốn tách mấy lần, nếu k nhập tách tối đa
    #splitlines: tách chuỗi theo các dòng (dựa trên ký tự xuống dòng), cú pháp: str.splitlines(keepends=False)
        #'click link to more details'

    
