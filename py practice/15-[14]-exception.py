try:
    print('The year at the moment and your height now')
    year1, height1 = input().split()
    height1 = int(height1)

    print('The year in 5 years ago and your heigh at that time')
    year2, height2 = input().split()
    height2 = int(height2)

    if height1 > height2:
        print('In {} you are higher than {}'.format(year1, year2), 'is', height1 - height2)

    elif height1 <= 0 or height2 <= 0:
        print('chieu cao phai lon hon 0')

    elif height1 < height2:
        print('In {} you are lower than {}'.format(year1, year2), 'is', height2 - height1)

    else:
        print('In {}, you are the same height with {}'.format(year1, year2))

except:
    print('định dạng đầu vào k hợp le')