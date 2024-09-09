# Viết hàm với tham số truyền vào là một tuple bất kỳ. 
# Trả về tuple số phần tử bằng 0 và số ký tự 0 có trong tuple đó.
# vd input: 0 0Kteam0 0 Free Education 0     || output: (3, 5)

def sweetHeart(s):
    zero = s.count('0')
    dem = [ptu.count('0') for ptu in s]
    # print(dem) || [1, 2, 1, 0, 0, 1]
    return zero, sum(dem)

ong = tuple(input('nhap: ').split())
# print(ong) || ('0', '0Kteam0', '0', 'Free', 'Education', '0')
print(sweetHeart(ong))
    