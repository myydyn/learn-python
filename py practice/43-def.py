def taller(name1, height1, name2, height2):
    if height1>height2:
        return name1
    return name2
try:
    name1, height1 = input('enter the 1_st name and age (cm), separating by a space: ').split()
    name2, height2 = input('enter the 2_st name and age (cm), separating by a space: ').split()
    #split chia chuỗi nhập vào thành một danh sách các chuỗi con mỗi khi nó gặp khoảng trắng (or ký tự phân tách mặc định)
    height1 = int(height1)
    height2 = int(height2)

    if height1 <1 or height2 <1:
        print('height has to greater than zero')
    elif height1 == height2:
        print('{} is as tall as {}.'.format(name1, name2))
    else:
        who_taller = taller(name1, height1, name2, height2)
        print('{} is taller.'.format(who_taller))
except:
    print('error input')
