# Viết hàm truyền vào tham số là chuỗi s. 
# Hiển thị các câu của chuỗi s, mỗi câu nằm trên một dòng. 
# Các câu đã được xóa khoảng trắng thừa và căn giữa theo câu dài nhất.


def text(s):
    s = s.strip()
    while '  ' in s:
        s = s.replace('  ', ' ')
    return s

def text_center(s):
    raw = s.split('.')
    max_len = 0
    for i in raw:
        i = text(i)
        if len(i) > max_len:
            max_len = len(i)

    for i in raw:
        i = text(i)
        print(i.center(max_len))

s = input()    
text_center(s) #kteam thiếu dòng này để xuất kq