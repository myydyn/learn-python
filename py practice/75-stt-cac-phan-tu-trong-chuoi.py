# Viết hàm với tham số truyền vào là danh sách bất kỳ. 
# Hiển thị các phần tử ra màn hình kèm với số thứ tự phía trước.

def loser(s):
    #Su dung ham enumerate de them mot bo dem vao truoc moi doi tuong
    for soThuTu, giatri in enumerate(s):
        print(soThuTu, giatri)

s =  input('nhap chuoi s: ').split()
loser(s)
