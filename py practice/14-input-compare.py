print('The year at the moment and your height now')
year1, height1 = input().split()
height1 = int(height1)

print('The year in 5 years ago and your heigh at that time')
year2, height2 = input().split()
height2 = int(height2)

if height1 > height2:
    print('In {} you are higher than {}'.format(year1, year2), 'is', height1 - height2)

else:
    print('In {}, you are not taller than {}'.format(year1, year2))