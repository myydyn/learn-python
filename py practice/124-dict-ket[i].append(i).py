# Trả về dict kết quả bằng cách gom nhóm các phần tử giống nhau 
# của list theo mẫu. (Tham số là 1 danh sách)
# vd:
# in: 1 2 1 2 3 4 5  || out: {'1': ['1', '1'], '2': ['2', '2'], '3': ['3'], '4': ['4'], '5': ['5']}
# in: kteam kteam kteam || out: {'kteam': ['kteam', 'kteam', 'kteam']}


def tao_dict(s):
    dictKq = {}
    for i in s:
        if i in dictKq:
            dictKq[i].append(i)
        else:
            dictKq[i] = [i]
    return dictKq
s = input('nhap chuoi s: ').split()
print(tao_dict(s))
