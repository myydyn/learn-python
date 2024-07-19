isright = False
try:
    a, b, c = map(float, input('nhập độ dài 3 đoạn thẳng a, b, c: ').split())
    isright = True

except:
    print('dau vao k hop le')

if isright:

    if (a+b)>c and (a+c)>b and(b+c)>a:
        if a==b==c:
            print('tam giác đều')
        elif a==b:
            print('tam giác ABC cân tại C')
        elif a==c:
            print('tam giác ABC cân tại B')
        elif b==c:
            print('tam giác ABC cân tại A')
        elif (a**2+b**2)==c**2:
            print('tam giác vuông tại C')
        elif (a**2+c**2)==b**2:
            print('tam giác vuông tại B')
        elif (c**2+b**2)==a**2:
            print('tam giác vuông tại A')
        elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
            print('{}, {}, {} là độ dài 3 cạnh tam giác tù'.format(a, b, c))
        else:
            print('{}, {}, {} là độ dài 3 cạnh tam giác nhọn'.format(a, b, c))
    else:
        print('{}, {}, {} k là độ dài 3 cạnh tam giác'.format(a, b, c))